#File Name : CAN_appli.py
#Author : Tanguy SIMON
#Project : BE Interdisciplinaire ESPE
#Abstract : functions to manage the CAN communication
############################################################################
import RPi.GPIO as GPIO
import can
import time
import os
import numpy as np
import queue
from threading import Thread
from DATA import *
############################################################################
def PICAN_LED_init() :
	led = 22
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(led,GPIO.OUT)
	GPIO.output(led,False)
	return
	
# CAN receive thread
def can_rx_task(bus,q):
	while True:
		message = bus.recv()
		q.put(message)			# Put message into queue
			
def CAN_init() :
	print('Bring up CAN0....')
	# Bring up can0 interface at 500kbps
	os.system("sudo /sbin/ip link set can0 up type can bitrate 500000")
	time.sleep(0.1)
	
	try:
		bus = can.interface.Bus(channel='can0', bustype='socketcan_native')
	except OSError:
		print('Cannot find PiCAN board.')
		GPIO.output(led,False)
		exit()
	
	q = queue.Queue()	
	t = Thread(target = can_rx_task,args = (bus,q,))	# Start receive thread
	t.start()

	return bus, q

def CAN_deinit() :
	print('Bring down CAN0....')
	os.system("sudo /sbin/ip link set can0 down")
	return
	
class c_CAN_Message :
	"""Structure of a CAN message"""
	def __init__(self, _ID, _Length, _Data):
		self.ID = _ID
		self.Length = _Length
		self.Data = _Data

def CAN_Send_msg(CAN_Msg,bus) :
        GPIO.output(22,True)
        msg = can.Message(arbitration_id=CAN_Msg.ID,data=CAN_Msg.Data,extended_id=True)
        bus.send(msg)
        GPIO.output(22,False)
        return
	
def CAN_Receive_msg(bus,q) :
	message = q.get()
	CAN_Msg = c_CAN_Message(message.arbitration_id, len(message.data), message.data) #creates object of class CAN_Message
	return CAN_Msg
	
def CAN_RX_Parser(CAN_Msg,SData): #see CAN BUS FRAME DESCRIPTOR on the dropbox for details about the cAN frames.
    if (CAN_Msg.ID == LSW_MMS_LDATA1_ID) :
        if(CAN_Msg.Data[1] == 1):
            SData.LoadStatusTable[CAN_Msg.Data[0]] = 'PV'
            #print('load '+str(CAN_Msg.Data[0])+' to PV')
        else:
            SData.LoadStatusTable[CAN_Msg.Data[0]] = 'EDF'
            #print('load '+str(CAN_Msg.Data[0])+' to EDF')
        # updating the load power sum
        SData.f32_LSW_Power = 0.0
        for i in range(0,5):
            if SData.LoadStatusTable[i] == 'PV' :
                SData.f32_LSW_Power += SData.LoadSPowerTable[i] #add the power consumed by connected loads
                
    if('PV' not in SData.LoadStatusTable):
        SData.AllLoadsDisconnected = True
    else:
        SData.AllLoadsDisconnected = False
            
    if('EDF' not in SData.LoadStatusTable):
        SData.AllLoadsConnected = True
    else:
        SData.AllLoadsConnected = False
            
    if (CAN_Msg.ID == LSW_MMS_LDATA2_ID) :
        SData.LoadSPowerTable[CAN_Msg.Data[0]] = CAN_Msg.Data[3] #apparent power
        #Total LSW power
        SData.f32_LSW_Power = 0.0
        for i in range(0,5):
            if SData.LoadStatusTable[i] == 'PV' :
                SData.f32_LSW_Power += SData.LoadSPowerTable[i] #add the power consumed by connected loads
    
    if (CAN_Msg.ID == BMS_MMS_SOC_ID) :
        SData.u8_BatteryLevel = CAN_Msg.Data[0]

    if (CAN_Msg.ID == BMS_MMS_PWR_ID) :
        #f32_BatteryPower = int.from_bytes(CAN_Msg.Data[0], byteorder = 'little')
        if CAN_Msg.Data[1]:
            SData.f32_BatteryPower = -CAN_Msg.Data[0]
        else:
            SData.f32_BatteryPower = CAN_Msg.Data[0]
        
    if (CAN_Msg.ID == MPPT_MMS_PWR_ID) :
        SData.f32_MPPT_Power = CAN_Msg.Data[0]
        if SData.f32_MPPT_Power > 0 :
            SData.MPPT_on = True
        else:
            SData.MPPT_on = False
        
    if (CAN_Msg.ID == MPPT_MMS_STAT_ID) :
        if(CAN_Msg.Data[0]):
        	SData.MPPT_Enabled = True
        else:
        	SData.MPPT_Enabled = False
        	
    if (CAN_Msg.ID == BMS_MMS_STAT_ID) :
        if(CAN_Msg.Data[0]):
        	SData.BMS_Enabled = True
        else:
        	SData.BMS_Enabled = False
        	
    if (CAN_Msg.ID == INV_MMS_STAT_ID) :
        if(CAN_Msg.Data[0]):
        	SData.INV_Enabled = True
        else:
        	SData.INV_Enabled = False
        	
    if (CAN_Msg.ID == LSW_MMS_STAT_ID) :
        if(CAN_Msg.Data[0]):
        	SData.LSW_Enabled = True
        else:
        	SData.LSW_Enabled = False
        	
    if (CAN_Msg.ID == BMS_MMS_OCH_ID) :
        if(CAN_Msg.Data[0]):
        	SData.BMS_OCH = True
        else:
        	SData.BMS_OCH = False
    
    if (CAN_Msg.ID == BMS_MMS_UCH_ID) :
        if(CAN_Msg.Data[0]):
        	SData.BMS_UCH = True
        else:
        	SData.BMS_UCH = False
        	
    if (CAN_Msg.ID == BMS_MMS_OT_ID) :
        if(CAN_Msg.Data[0]):
        	SData.BMS_OT = True
        else:
        	SData.BMS_OT = False

    return SData

def Log_Data(SData):
    W_line_file_csv('logs/charge1.csv',[(SData.date_time).strftime("%d/%m/%Y"),SData.date_time.strftime("%H:%M:%S"),0,SData.LoadStatusTable[0],0,0,0,0,SData.LoadSPowerTable[0],0,0])
    W_line_file_csv('logs/charge2.csv',[(SData.date_time).strftime("%d/%m/%Y"),SData.date_time.strftime("%H:%M:%S"),1,SData.LoadStatusTable[1],0,0,0,0,SData.LoadSPowerTable[1],0,0])
    W_line_file_csv('logs/charge3.csv',[(SData.date_time).strftime("%d/%m/%Y"),SData.date_time.strftime("%H:%M:%S"),2,SData.LoadStatusTable[2],0,0,0,0,SData.LoadSPowerTable[2],0,0])
    W_line_file_csv('logs/charge4.csv',[(SData.date_time).strftime("%d/%m/%Y"),SData.date_time.strftime("%H:%M:%S"),3,SData.LoadStatusTable[3],0,0,0,0,SData.LoadSPowerTable[3],0,0])
    W_line_file_csv('logs/charge5.csv',[(SData.date_time).strftime("%d/%m/%Y"),SData.date_time.strftime("%H:%M:%S"),4,SData.LoadStatusTable[4],0,0,0,0,SData.LoadSPowerTable[4],0,0])
    W_line_file_csv('logs/mppt.csv',   [(SData.date_time).strftime("%d/%m/%Y"),SData.date_time.strftime("%H:%M:%S"),SData.f32_MPPT_Power,1,SData.MPPT_Enabled])
    W_line_file_csv('logs/battery.csv',[(SData.date_time).strftime("%d/%m/%Y"),SData.date_time.strftime("%H:%M:%S"),str(SData.u8_BatteryLevel),str(abs(SData.f32_BatteryPower)),np.sign(SData.f32_BatteryPower),str(SData.MPPT_Enabled),str(SData.BMS_OCH),str(SData.BMS_UCH),str(SData.BMS_OT)])
    
def SW_Loads(LoadNum,LoadPos,bus):
	#LoadNum in [0:4]
	#LoadPos in [PV,EDF]
	if(LoadPos == 'EDF'):
		pos = 0
	elif(LoadPos == 'PV'):
		pos=1
	Data = [LoadNum,pos]
	CAN_Msg = c_CAN_Message(MMS_LSW_SWLOADS_ID,MMS_LSW_SWLOADS_LENGTH,Data) #building CAN object
	CAN_Send_msg(CAN_Msg,bus)#sending message
	
def Turn_MPPT(ON,bus):
	#send can message to MPPT	
	if(ON):
		Data = [1]
	else:
		Data = [0]
	CAN_Msg = c_CAN_Message(MMS_MPPT_ON_ID,MMS_MPPT_ON_LENGTH,Data) #building CAN object
	CAN_Send_msg(CAN_Msg,bus)#sending message
	
def Enable_MPPT(b_Enable,bus):
	#send can message to MPPT	
	if(b_Enable):
		Data = [1]
	else:
		Data = [0]
	CAN_Msg = c_CAN_Message(MMS_MPPT_EN_ID,MMS_MPPT_EN_LENGTH,Data) #building CAN object
	CAN_Send_msg(CAN_Msg,bus)#sending message
	
def Enable_BMS(b_Enable,bus):
	#send can message to MPPT	
	if(b_Enable):
		Data = [1]
	else:
		Data = [0]
	CAN_Msg = c_CAN_Message(MMS_BMS_EN_ID,MMS_BMS_EN_LENGTH,Data) #building CAN object
	CAN_Send_msg(CAN_Msg,bus)#sending message
	
def Enable_INV(b_Enable,bus):
	#send can message to MPPT	
	if(b_Enable):
		Data = [1]
	else:
		Data = [0]
	CAN_Msg = c_CAN_Message(MMS_INV_EN_ID,MMS_INV_EN_LENGTH,Data) #building CAN object
	CAN_Send_msg(CAN_Msg,bus)#sending message
	
def Enable_LSW(b_Enable,bus):
	#send can message to MPPT	
	if(b_Enable):
		Data = [1]
	else:
		Data = [0]
	CAN_Msg = c_CAN_Message(MMS_LSW_EN_ID,MMS_LSW_EN_LENGTH,Data) #building CAN object
	CAN_Send_msg(CAN_Msg,bus)#sending message
			
#CAN IDs
MPPT_MMS_STAT_ID = 		0x4211
BMS_MMS_STAT_ID = 		0x4311
INV_MMS_STAT_ID = 		0x4411
LSW_MMS_STAT_ID =		0x4511
MPPT_MMS_PWR_ID = 		0x3212
BMS_MMS_SOC_ID = 		0x3313
BMS_MMS_PWR_ID =		0x3312 
LSW_MMS_LDATA1_ID =		0x3514
LSW_MMS_LDATA2_ID =		0x351A
MMS_MPPT_EN_ID = 		0x1120
MMS_BMS_EN_ID =		0x1130
MMS_INV_EN_ID =		0x1140
MMS_LSW_EN_ID =		0x1150
MMS_MPPT_ON_ID =	0x2125
MMS_BMS_SWINV_ID =		0x1126
MMS_LSW_SWLOADS_ID =	0x2156
BMS_MMS_OCH_ID =		0x1317
BMS_MMS_UCH_ID =		0x1318
BMS_MMS_OT_ID =		0x1319

#CAN message lenghts

MPPT_MMS_STAT_LENGTH = 		1
BMS_MMS_STAT_LENGTH = 		1
INV_MMS_STAT_LENGTH = 		1
LSW_MMS_STAT_LENGTH =		1
MPPT_MMS_PWR_LENGTH = 		2
BMS_MMS_SOC_LENGTH = 		1
BMS_MMS_PWR_LENGTH =		2 
LSW_MMS_LDATA1_LENGTH =		8
LSW_MMS_LDATA2_LENGTH =		8
MMS_MPPT_EN_LENGTH = 		1
MMS_BMS_EN_LENGTH =			1
MMS_INV_EN_LENGTH =			1
MMS_LSW_EN_LENGTH =			1
MMS_MPPT_ON_LENGTH =		1
MMS_BMS_SWINV_LENGTH =		1
MMS_LSW_SWLOADS_LENGTH =		2
BMS_MMS_OCH_LENGTH =		1
BMS_MMS_UCH_LENGTH =		1
BMS_MMS_OT_LENGTH =			1


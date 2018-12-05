#File Name : CAN_appli.py
#Author : Tanguy SIMON
#Project : BE Interdisciplinaire ESPE

############################################################################
import RPi.GPIO as GPIO
import can
import time
import os
import numpy













############################################################################
def PICAN_LED_init() :
	led = 22
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(led,GPIO.OUT)
	GPIO.output(led,True)
	return
	
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
	return

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

def CAN_Send_msg(CAN_Msg) :
	msg = can.Message(arbitration_id=CAN_Msg.ID,CAN_Msg.Data,extended_id=True)
	bus.send(msg)
	return
	
def CAN_Receive_msg() :
	message = bus.recv()	# Wait until a message is received.
	CAN_Msg = c_CAN_Message(message.arbitration_id, len(message.data), message.data) #creates object of class CAN_Message
	return CAN_Msg
	
def CAN_RX_Parser(CAN_Msg):
	if CAN_Msg.ID == LSW_MMS_LDATA1_ID :
		#place method to fill in load balancer data class
	if CAN_Msg.ID == LSW_MMS_LDATA2_ID :
		#place method to fill in load balancer data class


			
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
MMS_MPPT_MAXPWR_ID =	0x2125
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
MMS_MPPT_MAXPWR_LENGTH =		2
MMS_BMS_SWINV_LENGTH =		1
MMS_LSW_SWLOADS_LENGTH =		8
BMS_MMS_OCH_LENGTH =		1
BMS_MMS_UCH_LENGTH =		1
BMS_MMS_OT_LENGTH =			1

#test code section
bus=CAN_init()
PICAN_LED_init()
Active_power = 0
Reactive_power = 100
Load_Apower_data = [0,0,0,0,0]
Load_Rpower_data = [60,60,60,60,60]
Load_Switch_status = [1,0,1,1,0]
while(True):
	time.sleep(0.7)
	Active_power +=1
	if (Active_power == 50):
		Active_power = 0
	Load_Apower_data = [Active_power*2,Active_power+3,Active_power,Active_power/2,Active_power+5]
	
	Reactive_power -=1
	if (Reactive_power == 0):
		Reactive_power = 60
	Load_Rpower_data = [Reactive_power*2,Reactive_power+3,Reactive_power,Reactive_power/2,Reactive_power+5]

	if(Reactive_power == 14 or Reactive_power == 58):
		Load_Switch_status[2] = not Load_Switch_status[2]
		Load_Switch_status[0] = not Load_Switch_status[0]
	for i in [0:4]:
		myMsg = c_CAN_Message(LSW_MMS_LDATA1_ID,LSW_MMS_LDATA1_LENGTH,[int8(i),int8(Load_Switch_status[i]),int16(FFFF),int16(Load_Rpower_data[i]),int16(Load_Apower_data[i])])
		time.sleep(0.5)
		CAN_Send_msg(myMsg)


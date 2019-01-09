#File Name : System_Emulator.py
#Author : Tanguy SIMON
#Project : BE Interdisciplinaire ESPE
#abstract : this codes aims to simulate the other modules of the system (MPPT, BMS, LSW). 
#It can receive CAN messages and act accordingly
############################################################################
from CAN_appli import *
import numpy as np
import can
import time

############################################################################
MPPT_PWR = 50
u8_BatteryLevel = 50
f32_BatteryPower = 0.0
f32_MPPT_Power = MPPT_PWR
f32_LSW_Power = 0.0
MPPT_Enabled = 0

bus,CAN_msg_queue=CAN_init()
PICAN_LED_init()
Load_Spower_data = [10,4,5,20,2]
Load_Switch_status = [0,0,0,0,0]
counter = 0
while(True):
    time.sleep(0.001)
    counter = (counter + 1)%700
    #define Parser for emulator
    CAN_Msg = None 
    if CAN_msg_queue.empty() != True:	# Check if there is a message in queue
        CAN_Msg = CAN_Receive_msg(bus,CAN_msg_queue) #read CAN message
        if(CAN_Msg.ID == MMS_LSW_SWLOADS_ID):
            Load_Switch_status[CAN_Msg.Data[0]] = CAN_Msg.Data[1]
            print('received SW_LOAD '+str(CAN_Msg.Data[0])+' to '+str(CAN_Msg.Data[1]))
        if(CAN_Msg.ID == MMS_MPPT_EN_ID):
            MPPT_Enabled = CAN_Msg.Data[0]
            print('received MPPT_EN : '+ str(MPPT_Enabled))
     
    if MPPT_Enabled :
        f32_MPPT_Power = MPPT_PWR
    else:
        f32_MPPT_Power = 0
    #Total LSW power
    f32_LSW_Power = 0.0
    for i in range(0,5):
        f32_LSW_Power += (Load_Spower_data[i]*Load_Switch_status[i]) #add the power consumed by connected loads
     
    #Battery power
    f32_BatteryPower = f32_LSW_Power-f32_MPPT_Power
    if f32_BatteryPower < 0 :
        sign = 1
    else:
        sign = 0
    #Battery level integration
    u8_BatteryLevel -= 0.0001*f32_BatteryPower
    if u8_BatteryLevel > 100 :
        u8_BatteryLevel = 100
    if u8_BatteryLevel < 0 :
        u8_BatteryLevel = 0
     
    if counter == 100 :
        #send battery power  
        #myMsg = c_CAN_Message(BMS_MMS_PWR_ID,BMS_MMS_PWR_LENGTH,[int(abs(f32_BatteryPower)).to_bytes(2,byteorder = 'little'),sign.to_bytes(1,byteorder = 'little')])
        myMsg = c_CAN_Message(BMS_MMS_PWR_ID,BMS_MMS_PWR_LENGTH,[int(abs(f32_BatteryPower)),sign])
        CAN_Send_msg(myMsg,bus)

    if counter == 200 :
        #send battery level
        myMsg = c_CAN_Message(BMS_MMS_SOC_ID,BMS_MMS_SOC_LENGTH,int(u8_BatteryLevel).to_bytes(1,byteorder = 'little'))
        CAN_Send_msg(myMsg,bus)
     
    if counter == 300 :
        #send load Apparent power   
        for i in range(0,5):#send load Apparent power
            myMsg = c_CAN_Message(LSW_MMS_LDATA2_ID,LSW_MMS_LDATA2_LENGTH,[np.uint8(i),np.uint8(0),np.uint16(0),np.uint16(Load_Spower_data[i]),np.uint16(0)])
            time.sleep(0.1)#5Hz
            CAN_Send_msg(myMsg,bus)
    
    if counter == 400 :
        #send load status	
        for i in range(0,5):#send load status
            myMsg = c_CAN_Message(LSW_MMS_LDATA1_ID,LSW_MMS_LDATA1_LENGTH,[np.uint8(i),np.uint16(Load_Switch_status[i]),np.uint8(0),np.uint16(0),np.uint16(0)])
            time.sleep(0.1)#5Hz
            CAN_Send_msg(myMsg,bus)
	
    if counter == 500 :
        #send MPPT power  
        myMsg = c_CAN_Message(MPPT_MMS_PWR_ID,MPPT_MMS_PWR_LENGTH,[int(f32_MPPT_Power)])
        CAN_Send_msg(myMsg,bus)
    
    if counter == 600 :
        #send send MPPT status
        myMsg = c_CAN_Message(MPPT_MMS_STAT_ID,MPPT_MMS_STAT_LENGTH,[np.uint8(MPPT_Enabled)])
        CAN_Send_msg(myMsg,bus)
    
    print('Battery level : '+str(u8_BatteryLevel))
    print('Battery power : '+str(f32_BatteryPower))
    print('LSW power : '+str(f32_LSW_Power))

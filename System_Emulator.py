#File Name : System_Emulator.py
#Author : Tanguy SIMON
#Project : BE Interdisciplinaire ESPE
#abstract : this codes aims to simulate the other modules of the system (MPPT, BMS, LSW). 
#It can receive CAN messages and act accordingly
############################################################################
import CAN_appli as cn









############################################################################
u8_BatteryLevel = 50
f32_BatteryPower = 0.0
f32_MPPT_Power = 31.0
f32_LSW_Power = 0.0
MPPT_Enabled = 0

bus=cn.CAN_init()
cn.PICAN_LED_init()
Load_Spower_data = [10,5,4,2,20]
Load_Switch_status = [0,0,0,0,0]
while(True):
	time.sleep(0.001)
	#define Parser for emulator
	CAN_Msg = cn.CAN_Receive_msg(bus) #read CAN messages
	
	if(CAN_Msg.ID == cn.MMS_LSW_SWLOADS_ID):
        Load_Switch_status[CAN_Msg.Data[0]] = CAN_Msg.Data[1]
     
     if(CAN_Msg.ID == cn.MMS_MPPT_EN_ID):
        MPPT_Enabled = CAN_Msg.Data[0]
     
     #Total LSW power
     f32_LSW_Power = 0.0
     for i in range(0,4):
          f32_LSW_Power += (Load_Spower_data[i]*Load_Switch_status[i]) #add the power consumed by connected loads
     
     #Battery level integration
     u8_BatteryLevel += 0.001*(f32_MPPT_Power-f32_LSW_Power)
        
	for i in range(0,4):#send load Apparent power
		myMsg = cn.c_CAN_Message(cn.LSW_MMS_LDATA2_ID,cn.LSW_MMS_LDATA2_LENGTH,[np.uint8(i),np.uint8(0),np.uint16(0),np.uint16(Load_Spower_data[i]),np.uint16(0)])
		time.sleep(0.2)#5Hz
		cn.CAN_Send_msg(myMsg)
		
	for i in range(0,4):#send load status
		myMsg = cn.c_CAN_Message(cn.LSW_MMS_LDATA2_ID,cn.LSW_MMS_LDATA2_LENGTH,[np.uint8(i),np.uint16(Load_Switch_status[i]),np.uint8(0),np.uint16(0),np.uint16(0)])
		time.sleep(0.2)#5Hz
		cn.CAN_Send_msg(myMsg)
	
	myMsg = cn.c_CAN_Message(cn.MPPT_MMS_STAT_ID,cn.MPPT_MMS_STAT_LENGTH,[np.uint8(MPPT_Enabled)])
	time.sleep(0.2)#5Hz
	cn.CAN_Send_msg(myMsg)
	


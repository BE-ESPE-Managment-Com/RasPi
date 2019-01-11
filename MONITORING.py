#File Name : MONITORING.py
#Author : Tanguy SIMON
#Project : BE Interdisciplinaire ESPE
#Abstract : Algorithms for the monitoring function
#NB : "connected" means the load is connected to the PV, disconnected means it is connected to EDF
###############################IMPORTS#####################################
import time
from CAN_appli import *
##############################DEFINES######################################
MAX_BATTERY_LEVEL = 95
MIN_BATTERY_LEVEL = 5
OK_BATTERY_LEVEL_H = 80
OK_BATTERY_LEVEL_L = 20

MIN_LOAD_POWER = 0
MAX_LOAD_POWER = 100

PRECISION_LOAD_BALANCING = 5 #VA

###############################VARIABLES###################################
s_Battery_State = "OK" # "LOW" "HIGH"
u8_BatteryLevel = 50
f32_BatteryPower = 0.0
AllLoadsConnected = False
AllLoadsDisconnected = True
f32_MPPT_Power = 0.0
f32_LSW_Power = 0.0
LoadStatusTable = ['EDF','EDF','EDF','EDF','EDF']
LoadSPowerTable = [0.0,0.0,0.0,0.0,0.0]
MPPT_Enabled = False
bus = 0
############################################################################""
class c_System_Data :
	"""Structure all system data"""
	def __init__(self):
		self.s_Battery_State = "OK" # "LOW" "HIGH"
		self.u8_BatteryLevel = 50
		self.f32_BatteryPower = 0.0
		self.AllLoadsConnected = False
		self.AllLoadsDisconnected = True
		self.f32_MPPT_Power = 0.0
		self.f32_LSW_Power = 0.0
		self.LoadStatusTable = ['EDF','EDF','EDF','EDF','EDF']
		self.LoadSPowerTable = [0.0,0.0,0.0,0.0,0.0]
		self.MPPT_Enabled = False
		self.BMS_Enabled = False
		self.INV_Enabled = False
		self.LSW_Enabled = False

def b_InitSystem():
    err = False
    PICAN_LED_init()
    bus,q = CAN_init()
    
    #init of other modules
    
    Enable_BMS(True,bus)
    for i in range(0,20): #BMS init
        time.sleep(1)#wait 1s
        Enable_BMS(True,bus)
        if CAN_msg_queue.empty() != True:	# Check if there is a message in queue
            if (CAN_Msg.ID == BMS_MMS_STAT_ID) :
                if(CAN_Msg.Data[0]):
                        SData.BMS_Enabled = True
                        break
                else:
                        SData.BMS_Enabled = False
    if not BMS_Enabled :
        print('ERR BMS NOT RESPONDING')
        print('20s timeout exceeded')
        raise "Initialisation error" #terminate program
    
    for i in range(0,20): #LSW and INV init
        time.sleep(0.5)#wait 0.5s
        Enable_INV(True,bus)
        time.sleep(0.5)#wait 0.5s
        Enable_LSW(True,bus)
        
        if CAN_msg_queue.empty() != True:	# Check if there is a message in queue
            if (CAN_Msg.ID == INV_MMS_STAT_ID) :
                if(CAN_Msg.Data[0]):
                        SData.INV_Enabled = True
                        break
                else:
                        SData.INV_Enabled = False
                        
            if (CAN_Msg.ID == LSW_MMS_STAT_ID) :
                if(CAN_Msg.Data[0]):
                        SData.LSW_Enabled = True
                else:
                        SData.LSW_Enabled = False
                        
    if not INV_Enabled :
        print('INV BMS NOT RESPONDING')
        print('20s timeout exceeded')
        raise "Initialisation error" #terminate program
    if not LSW_Enabled :
        print('ERR LSW NOT RESPONDING')
        print('20s timeout exceeded')
        raise "Initialisation error" #terminate program
    
    return err,bus,q

def u8_Load_Choice_Algorithm(ConnectTo, f32_power_batt, LoadStatusTable, LoadSPowerTable):
	#get load power data
        Matching_load_num = 'FF'
        Matching_load_power_diffence = 1000
        for i in range(0,5):
            #print(i)
            Load_power_difference = abs(LoadSPowerTable[i]-f32_power_batt)
            #print(Load_power_difference)
            if(Load_power_difference < Matching_load_power_diffence and LoadStatusTable[i] != ConnectTo):
                #print('yes')
                Matching_load_num = i
                Matching_load_power_diffence = Load_power_difference
            #else:
                #print('no')
                
        return Matching_load_num
			
def Connect_Load(bus,LoadStatusTable, LoadSPowerTable, f32_BatteryPower):
    #Load choice Algorithm
    LoadNum = u8_Load_Choice_Algorithm('PV',abs(f32_BatteryPower),LoadStatusTable, LoadSPowerTable)
    if LoadNum == 'FF':
        print('ERR NO LOAD TO CONNECT')
    
    else:
        #send CAN message to LSW to connect optimal load
        print("Connecting load "+str(LoadNum))
        SW_Loads(LoadNum,'PV',bus)
	
def Disconnect_Load(bus,LoadStatusTable, LoadSPowerTable, f32_BatteryPower):
    #Load choice Algorithm
    LoadNum = u8_Load_Choice_Algorithm('EDF',abs(f32_BatteryPower),LoadStatusTable, LoadSPowerTable)
    if LoadNum == 'FF':
        print('ERR NO LOAD TO DISCONNECT')
    
    else:
        #send CAN message to LSW to disconnect optimal load
        print("Disconnecting load "+str(LoadNum))
        SW_Loads(LoadNum,'EDF',bus)

def MainAlgorithm():
    SData = c_System_Data()
    bus = 0
    
    print("Initialising system...")
    InitErr,bus,CAN_msg_queue = b_InitSystem()
    if(InitErr):
        print("Initialisation error. Trying again...")
        time.sleep(1)#wait 1s
        print("Initialising system...")
        InitErr,bus,CAN_msg_queue = b_InitSystem()
        if(InitErr):
            print("Second initialisation error. System shut down...")
            raise "Initialisation error" #terminate program
    print("Initialisation done.")
    counter = 0
    while(True):
        time.sleep(0.05)#0.5ms
        counter += 1
        #check state of watchdogs (check that all modules are sending data on the CAN bus, i.e. the data is fresh and relevant)
        if CAN_msg_queue.empty() != True:	# Check if there is a message in queue
            SData = CAN_RX_Parser(CAN_Receive_msg(bus,CAN_msg_queue),SData) #read CAN message and parse it
                
        if(counter == 20):#1s
            counter = 0
            print('--------------entering main algo------------')
            #Main Algorithm
            #test battery level
            if(SData.u8_BatteryLevel > MAX_BATTERY_LEVEL):
                SData.s_Battery_State = "HIGH"
            elif(SData.u8_BatteryLevel < MIN_BATTERY_LEVEL):
                SData.s_Battery_State = "LOW"
            elif(SData.u8_BatteryLevel < OK_BATTERY_LEVEL_H and SData.u8_BatteryLevel > OK_BATTERY_LEVEL_L):
                SData.s_Battery_State = "OK"

            

            #code corresponding to different battery states
            if(SData.s_Battery_State == "HIGH"):
                #code for battery overcharge
                if(SData.f32_BatteryPower <= 0): #is battery Charging?
                    if(SData.AllLoadsConnected):
                        print("Disabling MPPT")
                        Enable_MPPT(False,bus)
                    else:
                        Connect_Load(bus,SData.LoadStatusTable,SData.LoadSPowerTable, SData.f32_BatteryPower)
            elif(SData.s_Battery_State == "LOW"):
                #code for battery undercharge
                if(not SData.MPPT_Enabled):
                    print("Enabling MPPT")
                    Enable_MPPT(True,bus)
                    if(not SData.AllLoadsDisconnected):
                        Disconnect_Load(bus,SData.LoadStatusTable,SData.LoadSPowerTable, SData.f32_BatteryPower)
                else:
                    if(SData.f32_BatteryPower >= 0): #is battery discharging?
                        if(not SData.AllLoadsDisconnected):
                            Disconnect_Load(bus,SData.LoadStatusTable,SData.LoadSPowerTable, SData.f32_BatteryPower)
                        else:
                            pass #if MPPT power > 0, all loads disconnected and battery still discharging there can be a problem.
                            #to be added when the rest is working for additionnal security

            elif(SData.s_Battery_State == "OK"):
                #code for battery ok
                if(not SData.MPPT_Enabled):
                    print("Enabling MPPT")
                    Enable_MPPT(True,bus)
                else:	
                    if(SData.f32_MPPT_Power > SData.f32_LSW_Power + PRECISION_LOAD_BALANCING):
                        print("Consumption to low compared to production")
                        if(not SData.AllLoadsConnected):
                            Connect_Load(bus,SData.LoadStatusTable,SData.LoadSPowerTable,SData.f32_BatteryPower)

                    elif(SData.f32_MPPT_Power < SData.f32_LSW_Power - PRECISION_LOAD_BALANCING):
                        print("Consumption to high compared to production")
                        if(not SData.AllLoadsDisconnected):
                            Disconnect_Load(bus,SData.LoadStatusTable,SData.LoadSPowerTable,SData.f32_BatteryPower)
                    else:
                        print("consumption equivalent to production +/-"+str(PRECISION_LOAD_BALANCING)+"VA")
            else:
                print("Undeclared battery state detected. System shut down...")
                raise "Undeclared state error" #terminate program
            
            print("Battery State : "+ SData.s_Battery_State)
            print('LSW power = '+str(SData.f32_LSW_Power))
            if SData.AllLoadsDisconnected :
                print('all loads disconnected')
            elif SData.AllLoadsConnected :
                print('all loads connected')
            print('battery level =  '+str(SData.u8_BatteryLevel))
            print('battery power =  '+str(SData.f32_BatteryPower))
            if SData.MPPT_Enabled :
                print('MPPT Enabled')
            else :
                print('MPPT Disabled')
            print('MPPT power =  '+str(SData.f32_MPPT_Power))
            print(SData.LoadStatusTable)
            print(SData.LoadSPowerTable)

MainAlgorithm()

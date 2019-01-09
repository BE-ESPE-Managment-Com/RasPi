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
def b_InitSystem():
    err = False
    PICAN_LED_init()
    bus,q = CAN_init()
    #insert code
    return err,bus,q

def u8_Load_Choice_Algorithm(ConnectTo, f32_power_delta, LoadStatusTable):
	#get load power data
        Matching_load_num = 'FF'
        Matching_load_power_diffence = 1000
        for i in range(0,5):
            Load_power_difference = abs(LoadSPowerTable[i]-f32_power_delta)
            if(Load_power_difference < Matching_load_power_diffence and LoadStatusTable[i] != ConnectTo):
                Matching_load_num = i
                Matching_load_power_diffence = Load_power_difference
                
        return Matching_load_num
			
def Connect_Load(bus,LoadStatusTable):
    #Load choice Algorithm
    LoadNum = u8_Load_Choice_Algorithm('PV',abs(f32_MPPT_Power - f32_LSW_Power),LoadStatusTable)
    if LoadNum == 'FF':
        print('ERR NO LOAD TO CONNECT')
    
    else:
        #send CAN message to LSW to connect optimal load
        print("Connecting load "+str(LoadNum))
        SW_Loads(LoadNum,'PV',bus)
	
def Disconnect_Load(bus,LoadStatusTable):
    #Load choice Algorithm
    LoadNum = u8_Load_Choice_Algorithm('EDF',abs(f32_MPPT_Power - f32_LSW_Power),LoadStatusTable)
    if LoadNum == 'FF':
        print('ERR NO LOAD TO DISCONNECT')
    
    else:
        #send CAN message to LSW to disconnect optimal load
        print("Disconnecting load "+str(LoadNum))
        SW_Loads(LoadNum,'EDF',bus)

def MainAlgorithm():
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
    LoadNum_S = 0
    LoadStat = 'EDF'
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
        time.sleep(0.0005)#0.5ms
        counter += 1
        #check state of watchdogs (check that all modules are sending data on the CAN bus, i.e. the data is fresh and relevant)
        if CAN_msg_queue.empty() != True:	# Check if there is a message in queue
            s_Battery_State,u8_BatteryLevel,f32_BatteryPower,AllLoadsConnected,AllLoadsDisconnected,f32_MPPT_Power,f32_LSW_Power,LoadStatusTable,LoadSPowerTable,MPPT_Enabled = CAN_RX_Parser(CAN_Receive_msg(bus,CAN_msg_queue),s_Battery_State,u8_BatteryLevel,f32_BatteryPower,AllLoadsConnected,AllLoadsDisconnected,f32_MPPT_Power,f32_LSW_Power,LoadStatusTable,LoadSPowerTable,MPPT_Enabled) #read CAN message and parse it
                
        if(counter == 200):#1s
            counter = 0
            print('--------------entering main algo------------')
            #Main Algorithm
            #test battery level
            if(u8_BatteryLevel > MAX_BATTERY_LEVEL):
                s_Battery_State = "HIGH"
            elif(u8_BatteryLevel < MIN_BATTERY_LEVEL):
                s_Battery_State = "LOW"
            elif(u8_BatteryLevel < OK_BATTERY_LEVEL_H and u8_BatteryLevel > OK_BATTERY_LEVEL_L):
                s_Battery_State = "OK"

            

            #code corresponding to different battery states
            if(s_Battery_State == "HIGH"):
                #code for battery overcharge
                if(f32_BatteryPower < 0): #is battery Charging?
                    if(AllLoadsConnected):
                        print("Disabling MPPT")
                        Enable_MPPT(False,bus)
                    else:
                        Connect_Load(bus,LoadStatusTable)
            elif(s_Battery_State == "LOW"):
                #code for battery undercharge
                if(not MPPT_Enabled):
                    print("Enabling MPPT")
                    Enable_MPPT(True,bus)
                    if(not AllLoadsDisconnected):
                        Disconnect_Load(bus,LoadStatusTable)
                else:
                    if(f32_BatteryPower > 0): #is battery discharging?
                        if(not AllLoadsDisconnected):
                            Disconnect_Load(bus,LoadStatusTable)
                        else:
                            pass #if MPPT power > 0, all loads disconnected and battery still discharging there can be a problem.
                            #to be added when the rest is working for additionnal security

            elif(s_Battery_State == "OK"):
                #code for battery ok
                if(not MPPT_Enabled):
                    print("Enabling MPPT")
                    Enable_MPPT(True,bus)
                else:	
                    if(f32_MPPT_Power > f32_LSW_Power + PRECISION_LOAD_BALANCING):
                        print("Consumption to low compared to production")
                        print('all loads connected :'+ str(AllLoadsConnected))
                        if(not AllLoadsConnected):
                            Connect_Load(bus,LoadStatusTable)

                    elif(f32_MPPT_Power < f32_LSW_Power - PRECISION_LOAD_BALANCING):
                        print("Consumption to high compared to production")
                        if(not AllLoadsDisconnected):
                            Disconnect_Load(bus,LoadStatusTable)
                    else:
                        print("consumption equivalent to production +/-"+str(PRECISION_LOAD_BALANCING)+"VA")
            else:
                print("Undeclared battery state detected. System shut down...")
                raise "Undeclared state error" #terminate program
            
            print("Battery State : "+ s_Battery_State)
            print('LSW power = '+str(f32_LSW_Power))
            if AllLoadsDisconnected :
                print('all loads disconnected')
            elif AllLoadsConnected :
                print('all loads connected')
            print('battery level =  '+str(u8_BatteryLevel))
            print('battery power =  '+str(f32_BatteryPower))
            if MPPT_Enabled :
                print('MPPT Enabled')
            else :
                print('MPPT Disabled')
            print('MPPT power =  '+str(f32_MPPT_Power))
            print(LoadStatusTable)
            print(LoadSPowerTable)

MainAlgorithm()

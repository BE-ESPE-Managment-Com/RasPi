#File Name : MONITORING.py
#Author : Tanguy SIMON
#Project : BE Interdisciplinaire ESPE
#Abstract : Algorithms for the monitoring function
#NB : "connected" means the load is connected to the PV, disconnected means it is connected to EDF
###############################IMPORTS#####################################
import time
import CAN_appli_sender as cn

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
LoadStatusTable = ["EDF","EDF","EDF","EDF","EDF"]
LoadSPowerTable = [0.0,0.0,0.0,0.0,0.0]
MPPT_Enabled = False
bus = 0
############################################################################""
def b_InitSystem():
    err = False
    cn.PICAN_LED_init()
    bus = cn.CAN_init()
    #insert code
    return err,bus

def u8_Load_Choice_Algorithm(ConnectTo, f32_power_delta):
	#get load power data
	Matching_load_power_diffence = 1000
	for i in range(0,4):
		Load_power_difference = abs(LoadSPowerTable[i]-f32_power_delta)
		if(Load_power_difference < Matching_load_power_diffence and LoadStatusTable[i] != ConnectTo):
			Matching_load_num = i
			Matching_load_power_diffence = Load_power_difference
			
	return Matching_load_num
			
def Connect_Load():
	#Load choice Algorithm
	LoadNum = u8_Load_Choice_Algorithm("PV",abs(f32_MPPT_Power - f32_LSW_Power))
	#send CAN message to LSW to connect optimal load
	SW_Loads(LoadNum,"PV",bus)
	
def Disonnect_Load():
	#Load choice Algorithm
	LoadNum = u8_Load_Choice_Algorithm("EDF",abs(f32_MPPT_Power - f32_LSW_Power))
	#send CAN message to LSW to disconnect optimal load
	SW_Loads(LoadNum,"EDF",bus)

def MainAlgorithm():
    print("Initialising system...")
    InitErr,bus = b_InitSystem()
    if(InitErr):
        print("Initialisation error. Trying again...")
        time.sleep(1)#wait 1s
        print("Initialising system...")
        InitErr = b_InitSystem()
        if(InitErr):
            print("Second initialisation error. System shut down...")
            raise "Initialisation error" #terminate program
    print("Initialisation done.")
    counter = 0
    while(True):
        time.sleep(0.001)#1ms
        counter += 1
        #check state of watchdogs (check that all modules are sending data on the CAN bus, i.e. the data is fresh and relevant)
        cn.CAN_RX_Parser(cn.CAN_Receive_msg(bus)) #read CAN messages
        
        if(counter == 1000):#1s
            counter = 0
            #Main Algorithm
            #test battery level
            if(u8_BatteryLevel > MAX_BATTERY_LEVEL):
                s_Battery_State = "HIGH"
            elif(u8_BatteryLevel < MIN_BATTERY_LEVEL):
                s_Battery_State = "LOW"
            elif(u8_BatteryLevel < OK_BATTERY_LEVEL_H and u8_BatteryLevel > OK_BATTERY_LEVEL_L):
                s_Battery_State = "OK"

            print("Battery State : "+ s_Battery_State)

            #code corresponding to different battery states
            if(s_Battery_State == "HIGH"):
                #code for battery overcharge
                if(f32_BatteryPower < 0): #is battery Charging?
                    if(AllLoadsConnected):
                        print("Disabling MPPT")
                        cn.Enable_MPPT(False,bus)
                    else:
                        Connect_Load()
            elif(s_Battery_State == "LOW"):
                #code for battery undercharge
                if(not MPPT_Enabled):
                    print("Enabling MPPT")
                    cn.Enable_MPPT(True,bus)
                    if(not AllLoadsDisconnected):
                        print("Disconnecting load")
                        Disonnect_Load()
                else:
                    if(f32_BatteryPower > 0): #is battery discharging?
                        if(not AllLoadsDisconnected):
                            print("Disconnecting load")
                            Disconnect_Load()
                        else:
                            pass #if MPPT power > 0, all loads disconnected and battery still discharging there can be a problem

            elif(s_Battery_State == "OK"):
                #code for battery ok
                if(not MPPT_Enabled):
                    print("Enabling MPPT")
                    cn.Enable_MPPT(True,bus)
                else:	
                    if(f32_MPPT_Power > f32_LSW_Power + PRECISION_LOAD_BALANCING):
                        print("Consumption to low compared to production")
                        print("Connecting load...")
                        Connect_Load()

                    elif(f32_MPPT_Power < f32_LSW_Power - PRECISION_LOAD_BALANCING):
                        print("Consumption to high compared to production")
                        print("Disconnecting load...")
                        Disconnect_Load()
                    else:
                        print("consumption equivalent to production +/-"+PRECISION_LOAD_BALANCING+"VA")
            else:
                print("Undeclared battery state detected. System shut down...")
                raise "Undeclared state error" #terminate program

MainAlgorithm()

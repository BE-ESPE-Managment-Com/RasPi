#File Name : MONITORING.py
#Author : Tanguy SIMON
#Project : BE Interdisciplinaire ESPE
#Abstract : Algorithms for the monitoring function. All power is Apparent power, in VA
#NB : "connected" means the load is connected to the PV, disconnected means it is connected to EDF
#TODO : Add slow, complete battery charge during weekends procedure (constant current, then constant voltage)
#       add emergency procedures for BMS alerts
###############################IMPORTS#####################################
import time
import datetime
from CAN_appli import *
##############################DEFINES######################################
MAX_BATTERY_LEVEL = 75
MIN_BATTERY_LEVEL = 55
OK_BATTERY_LEVEL_H = 70
OK_BATTERY_LEVEL_L = 60

MIN_LOAD_POWER = 0
MAX_LOAD_POWER = 100

PRECISION_LOAD_BALANCING = 5 #VA

ON = True
OFF = False
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
	"""Structure for all system data"""
	def __init__(self):
		self.date_time = datetime.datetime.now() #current real time date (not managed yet)
		self.s_Battery_State = "OK" # Battery charge status ("LOW", "OK", "HIGH") Managed with a hysteresis 
		# to prevent too rapid commutation of the switches)
		self.u8_BatteryLevel = 70 # battery charge percentage (usable is 50 to 80)
		self.f32_BatteryPower = 0.0 # battery power in VA, + is out of the battery, - is into the battery
		self.AllLoadsConnected = False #verification based on LSW module info (load status)
		self.AllLoadsDisconnected = True #verification based on LSW module info (load status)
		self.f32_MPPT_Power = 0.0 #MPPT power in VA. 
		self.f32_LSW_Power = 0.0 #Sum of the power consumed by all the loads connected
		self.f32_EDF_Power = 0.0 #for logging
		self.LoadStatusTable = ['EDF','EDF','EDF','EDF','EDF'] #EDF or PV
		self.LoadSPowerTable = [0.0,0.0,0.0,0.0,0.0] #power for each load (VA)
		self.MPPT_SW = ON #power switch between the battery and the inverter, controlled by the MPPT module. Not used yet (TODO : has to be added in case of emergency)
		self.MPPT_on = OFF #switching and harvesting power. Can be replaced with a max output power limit rather than shutin it off
		self.MPPT_Enabled = False #module status
		self.BMS_Enabled = False #module status
		self.INV_Enabled = False #module status
		self.LSW_Enabled = False #module status
		self.BMS_OCH = False #battery overcharge
		self.BMS_UCH = False #battery undercharge
		self.BMS_OT = False #battery over temperature

		
#########################################################################
# b_InitSystem
# Global PV system initialisation procedure. Checks that other modules
# are ready (sends Enable and waits for their status message). Test also 
# the CAN bus communication at the same time.
# Input Args : SData : system data class
# Output Args : err   : if initialisation error (one module did not respond)
# 			 bus   : for the CAN bus lower code layers
# 			 q     : CAN message queue (buffer)
#			 SData : system data  class, to return the module states
#########################################################################
def b_InitSystem(SData):
    err = False
    PICAN_LED_init()
    bus,q = CAN_init() # IMPORTANT : creation of a thread. a small program will be running in parallel to this one to bufferize the can messages when they arrive. (see CAN_init() in CAN_appli.py)
    
    #init of other modules
    
    Enable_BMS(True,bus)
    for i in range(0,20): #BMS init
        time.sleep(1)#wait 1s
        print('Init in process, please wait ')
        
        if SData.BMS_Enabled :
            break
        else:
            Enable_BMS(True,bus)
        while q.empty() != True:	# Check if there is a message in queue
            CAN_Msg = CAN_Receive_msg(bus,q)
            if (CAN_Msg.ID == BMS_MMS_STAT_ID) :
                if(CAN_Msg.Data[0]):
                        SData.BMS_Enabled = True
                        break
                else:
                        SData.BMS_Enabled = False
    if not SData.BMS_Enabled :
        print('ERR BMS NOT RESPONDING')
        print('20s timeout exceeded')
        return True,bus,q,SData #terminate program
    
    for i in range(0,30): #LSW and INV init
        if SData.INV_Enabled and SData.LSW_Enabled and SData.MPPT_Enabled :
            break
        time.sleep(1)#wait 1s
        print('Init in process, please wait ')
        if not SData.INV_Enabled:
            Enable_INV(True,bus)
        if not SData.LSW_Enabled:
            Enable_LSW(True,bus)
        if not SData.MPPT_Enabled:
            Enable_MPPT(True,bus)
        
        while q.empty() != True:	# Check if there is a message in queue
            CAN_Msg = CAN_Receive_msg(bus,q)
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
                        
            if (CAN_Msg.ID == MPPT_MMS_STAT_ID) :
                if(CAN_Msg.Data[0]):
                        SData.MPPT_Enabled = True
                else:
                        SData.MPPT_Enabled = False
                        
    if not SData.INV_Enabled :
        print('ERR INV NOT RESPONDING')
        print('20s timeout exceeded')
        return True,bus,q,SData #terminate program
    
    if not SData.LSW_Enabled :
        print('ERR LSW NOT RESPONDING')
        print('20s timeout exceeded')
        return True,bus,q,SData #terminate program
    
    if not SData.MPPT_Enabled :
        print('ERR MPPT NOT RESPONDING')
        print('20s timeout exceeded')
        return True,bus,q,SData #terminate program
    
    return err,bus,q,SData
    
#########################################################################
# u8_Load_Choice_Algorithm
# Algorithm for chosing the best load to fill the power delta, accoring to
# each load's power consumption (the load's power is measured even if they
# are connected to the EDF grid). This algo will be called for each load 
# connection/disconnection.
# Input Args : ConnectTo : 'PV' or 'EDF'. indicates if we want to resp. connect
#					  or disconnect a load.
#			f32_power_batt
#			LoadStatusTable
#			LoadSPowerTable
# Output Args : Matching_load_num : result of the algo. Load to be commuted
#########################################################################
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
        
#########################################################################
# Connect_Load
# to connect a load to the PV system.
#########################################################################		
def Connect_Load(bus,LoadStatusTable, LoadSPowerTable, f32_BatteryPower):
    #Load choice Algorithm
    LoadNum = u8_Load_Choice_Algorithm('PV',abs(f32_BatteryPower),LoadStatusTable, LoadSPowerTable)
    if LoadNum == 'FF':
        print('ERR NO LOAD TO CONNECT')
    
    else:
        #send CAN message to LSW to connect optimal load
        print("Connecting load "+str(LoadNum))
        SW_Loads(LoadNum,'PV',bus)

#########################################################################
# Disconnect_Load
# to connect a load to the EDF grid.
#########################################################################	
def Disconnect_Load(bus,LoadStatusTable, LoadSPowerTable, f32_BatteryPower):
    #Load choice Algorithm
    LoadNum = u8_Load_Choice_Algorithm('EDF',abs(f32_BatteryPower),LoadStatusTable, LoadSPowerTable)
    if LoadNum == 'FF':
        print('ERR NO LOAD TO DISCONNECT')
    
    else:
        #send CAN message to LSW to disconnect optimal load
        print("Disconnecting load "+str(LoadNum))
        SW_Loads(LoadNum,'EDF',bus)

#########################################################################
# MainAlgorithm
# 
#########################################################################
def Init_monitoring():
    SData = c_System_Data()
    bus = 0
    num_ligne = 0
    #Creation of data files for data logging
    Init_file_batt_csv('logs/battery.csv')
    Init_file_chargetot_csv('logs/charge_tot.csv')
    Init_file_charge_csv('logs/charge1.csv')
    Init_file_charge_csv('logs/charge2.csv')
    Init_file_charge_csv('logs/charge3.csv')
    Init_file_charge_csv('logs/charge4.csv')
    Init_file_charge_csv('logs/charge5.csv')
    Init_file_mppt_csv('logs/mppt.csv')
    
    Log_Data(SData) #store data in log files
    num_ligne += 1 #for HMI to read
        
    print("Initialising system...")
    InitErr,bus,CAN_msg_queue,SData = b_InitSystem(SData)
    if(InitErr):
        print("Initialisation error. Trying again...")
        time.sleep(1)#wait 1s
        print("Initialising system...")
        InitErr,bus,CAN_msg_queue,SData = b_InitSystem(SData)
        if(InitErr):
            print("Second initialisation error. System shut down...")
            raise SystemError("Initialisation error") #terminate program
    print("Initialisation done.")
    counter = 0
    return SData,bus,CAN_msg_queue,counter,num_ligne

def Monitoring(SData,bus,CAN_msg_queue,counter,num_ligne):    
    
    counter += 1
    #TODO : Add watchdogs and check their state (check that all modules are sending data on the CAN bus, i.e. the data is fresh and relevant). If one module stopped sending messages, de-enable it and relauch the initialisation procedure.
    if CAN_msg_queue.empty() != True:	# Check if there is a message in queue
        SData = CAN_RX_Parser(CAN_Receive_msg(bus,CAN_msg_queue),SData) #read CAN message and parse it
                    
    if(counter == 200):#1s
        counter = 0
        print('--------------entering main algo------------')
        #SData.time += 1
        
        #Upadte Time and date
        SData.date_time = datetime.datetime.now()
       
        
        Log_Data(SData) #store data in log files
        num_ligne += 1 #for HMI to read csv files
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
                    print("Stopping MPPT")
                    Turn_MPPT(OFF,bus)
                else:
                    Connect_Load(bus,SData.LoadStatusTable,SData.LoadSPowerTable, SData.f32_BatteryPower)
                    
        elif(SData.s_Battery_State == "LOW"):
            #code for battery undercharge
            if(not SData.MPPT_on):
                print("Starting MPPT")
                Turn_MPPT(ON,bus)
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
            if(not SData.MPPT_on):
                print("Starting MPPT")
                Turn_MPPT(ON,bus)
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
        
        print("Battery State : "+ SData.s_Battery_State)
        print('LSW power = '+str(SData.f32_LSW_Power))
        if SData.AllLoadsDisconnected :
            print('all loads disconnected')
        elif SData.AllLoadsConnected :
            print('all loads connected')
        print('battery level =  '+str(SData.u8_BatteryLevel))
        print('battery power =  '+str(SData.f32_BatteryPower))
        if SData.MPPT_on :
            print('MPPT started')
        else :
            print('MPPT stopped')
        print('MPPT power =  '+str(SData.f32_MPPT_Power))
        print(SData.LoadStatusTable)
        print(SData.LoadSPowerTable)
    return SData,bus,CAN_msg_queue,counter,num_ligne

#SData,bus,CAN_msg_queue,counter = Init_monitoring()
#while True:
#    time.sleep(0.005)
#    SData,bus,CAN_msg_queue,counter = Monitoring(SData,bus,CAN_msg_queue,counter)

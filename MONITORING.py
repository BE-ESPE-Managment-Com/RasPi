#File Name : MONITORING.py
#Author : Tanguy SIMON
#Project : BE Interdisciplinaire ESPE

###############################IMPORTS#####################################
import time					                        				

##############################DEFINES######################################
MAX_BATTERY_LEVEL = 95
MIN_BATTERY_LEVEL = 5
OK_BATTERY_LEVEL_H = 80
OK_BATTERY_LEVEL_L = 20

MIN_LOAD_POWER = 0
MAX_LOAD_POWER = 100

PRECISION_LOAD_BALANCING = 5 #VA

###############################VARIABLES###################################
s_Battery_State : "OK" # "LOW" "HIGH"

def b_InitSystem():
	bool err : False
	#insert code
	return err

def u8_Load_Choice_Algorithm(float f32_power_delta):
	#get load power data
	Matching_load_power_diffence = 1000
	for i in [0:4]:
		Load_power_difference = LoadPowerTable[i]-f32_power_delta
		if(Load_power_difference < Matching_load_power_diffence):
			Matching_load_num = i
			Matching_load_power_diffence = Load_power_difference
			
	return Matching_load_num
			
def Connect_Load():
	#Load choice Algorithm
	LoadNum = u8_Load_Choice_Algorithm(abs(f32_MPPT_Power - f32_LSW_Power))
	#send CAN message to LSW to connect optimal load
	SW_Loads(LoadNum,"PV")
	
def Disonnect_Load():
	#Load choice Algorithm
	LoadNum = u8_Load_Choice_Algorithm(abs(f32_MPPT_Power - f32_LSW_Power))
	#send CAN message to LSW to disconnect optimal load
	SW_Loads(LoadNum,"EDF")
	
def Enable_MPPT(bool b_Enable):
	#send can message to MPPT

def MainAlgorithm():
	print("Initialising system...")
	bool InitErr = b_InitSystem()#initialising
	if(InitErr):
		print("Initialisation error. Trying again...")
		time.sleep(1)#wait 1s
		print("Initialising system...")
		InitErr = b_InitSystem()
		if(InitErr):
			print("Second initialisation error. System shut down...")
			raise "Initialisation error" #terminate program
	print("Initialisation done.")
	
	#check state of watchdogs (check that all modules are sending data on the CAN bus, i.e. the data is fresh and relevant)
	#test battery level
	if(u8_BatteryLevel > MAX_BATTERY_LEVEL):
		s_Battery_State = "HIGH"
	elif(u8_BatteryLevel < MIN_BATTERY_LEVEL):
		s_Battery_State = "LOW"
	elif(u8_BatteryLevel < OK_BATTERY_LEVEL_H and u8_BatteryLevel > OK_BATTERY_LEVEL_L):
		s_Battery_State = "OK"
	else:
		#do not change current state (for hysteresis)
	print("Battery State : "+ s_Battery_State)
		
	#code corresponding to different battery states
	if(s_Battery_State == "HIGH"):
		#code for battery overcharge
		if(f32_BatteryPower > 0): #is battery discharging?
			#OK, do nothing
		else:
			if(AllLoadsConnected):
				print("Disabling MPPT")
				Enable_MPPT(False)
			else:
				Connect_Load()
	
	elif(s_Battery_State == "LOW"):
		#code for battery undercharge
		if(not MPPT_Enabled):
			print("Enabling MPPT")
			Enable_MPPT(True)
			if(not AllLoadsDisconnected):
				print("Disconnecting load")
				Disonnect_Load()
		else:
			if(f32_BatteryPower < 0): #is battery Charging?
				#OK, do nothing
			else:
				if(not AllLoadsDisconnected):
					print("Disconnecting load")
					Disconnect_Load()
				else:
					#if MPPT power > 0, all loads disconnected and battery still discharging there can be a problem
					
	elif(s_Battery_State == "OK"):
		#code for battery ok
		if(not MPPT_Enabled):
			print("Enabling MPPT")
			Enable_MPPT(True)
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

	

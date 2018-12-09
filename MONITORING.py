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

MIN_LOAD_POWER
MAX_LOAD_POWER
###########################################################################
def b_InitSystem():
	bool err : False
	#insert code
	return err
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
	

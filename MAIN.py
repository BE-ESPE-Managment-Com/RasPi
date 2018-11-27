#File Name : MAIN.py
#Author : Tanguy SIMON
#Project : BE Interdisciplinaire ESPE

############################################################################














###########################################################################
#							CLASSES						    #
###########################################################################
class Module_class :
	"""Generic class for all modules"""
	def __init__(self):
		self.Running = False
		self.Initialising = False
		self.Module_OK = True
		self.CAN_OK = True

	def Is_Running(self, info):
		self.Running = info
		if (self.Running):		
			print(self.__name__, "is active")
		else :
			print(self.__name__, "is inactive")

	def Is_Initialising(self, info):
		self.Initialising = info

	def Is_Module_OK(self, info):
		self.Module_OK = info

	def Is_CAN_OK(self, info):
		self.CAN_OK = info

class MPPT_Module(Module_class) :
	"""Specific subclass for MPPT subsystem"""
	def __init__(self):
		self.ID = 2
		self.PWR_Out = 0.0 #Watts	
		self.OC = False
		self.Limited_To = 100 #Pwr limit on its output (100=> not limited

	def W_PWR_Out(self, info):
		self.PWR_Out = info

	def W_OC(self, info):
		self.OC = info

	def W_Limited_To(self, info):
		self.Limited_To = info


class BMS_Module (Module_class) :
	"""Specific subclass for BMS subsystem"""
	def __init__(self):
		self.ID = 3
		self.PWR_Out = 0.0 #Watts	
		self.OC = False
		self.Battery_IN = False #is battery connected to network
		self.SoC = 50  #% of usable energy

	def W_PWR_Out(self, info):
		self.PWR_Out = info

	def W_OC(self, info):
		self.OC = info

	def W_Battery_IN(self, info):
		self.Battery_IN = info

	def W_SoC(self, info):
		self.SoC = info


class INV_Module (Module_class) :
	"""Specific subclass for INV subsystem"""
	def __init__(self):
		self.ID = 4
		self.Boost_OK = True #is boost output voltage ok
		self.INV_OK = True #is inverter output voltage ok

	def W_Boost_OK(self, info):
		self.Boost_OK = info

	def W_INV_OK(self, info):
		self.INV_OK = info


class LSW_Module (Module_class) :
	"""Specific subclass for LSW subsystem"""
	def __init__(self):
		self.ID = 5
		self.PWR_Out = {'L1' : 0.0,'L2' : 0.0,'L3' : 0.0,'L4' : 0.0,'L5' : 0.0,'L6' : 0.0,'L7' : 0.0,'L8' : 0.0}#Watts			
		self.Load_Stat = {'L1' : 'EDF','L2' : 'EDF','L3' : 'EDF','L4' : 'EDF','L5' : 'EDF','L6' : 'EDF','L7' : 'EDF','L8' : 'EDF'} #EDF/PV
		
		def W_PWR_Out(self, Load, PWR_val):
			self.PWR_Out[Load] = PWR_val
		
		def W_Load_Stat(self, Load, stat):
			self.Load_Stat[Load] = stat
			
			


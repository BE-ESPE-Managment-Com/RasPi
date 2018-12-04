#File Name : DATA.py
#Author : Tanguy SIMON / Amélie MEYER
#Project : BE Interdisciplinaire ESPE

###########################################################################
## CLASSES						    	 
###########################################################################

## CLASS DEFINITION FOR MODULES. Use: check initialisation and communication

class Module_class :

	def __init__(self):
		self.Running = False
		self.Initialising = False
		self.Module_OK = True
		self.CAN_OK = True
		self.ID = 0

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
		
	def Is_ID(self, info):
		self.ID = info

		
## CLASS DEFINITION FOR LOAD DATA. Use: store data acquired through the load balancer

class Load_Balancer_data_class :


	# INITIALISATION

	
	def __init__(self, __date = "", __time = "", __num = 0, __type = "", __current = 0, __voltage = 0, __active_power = 0, __reactive_power = 0, __apparent_power = 0, __power_factor = 0, __freq = 0):
		self.date = __date
		self.time = __time
		self.num = __num ## charge number
		self.type = __type ## "EDF" or "MPPT"
		self.current = __current ## RMS value (A)
		self.voltage = __voltage ## RMS value (V)
		self.active_power = __active_power ## (W)
		self.reactive_power = __reactive_power ## (VAR)
		self.apparent_power = __apparent_power ## (VA)
		self.power_factor = __power_factor
		self.freq = __freq ## (Hz)

		
	# METHODES SIMPLES 
	
	
	def Is_date(self, info):
		self.date = info

	def Is_time(self, info):
		self.time = info

	def Is_num(self, info):
		self.num = info
		
	def Is_type(self, info):
		self.type = info
	
	def Is_current(self, info):
		self.current = info

	def Is_voltage(self, info):
		self.voltage = info
		
	def Is_active_power(self, info):
		self.active_power = info

	def Is_reactive_power(self, info):
		self.reactive_power = info

	def Is_apparent_power(self, info):
		self.apparent_power = info

	def Is_power_factor(self, info):
		self.power_factor = info
		
	def Is_freq(self, info):
		self.freq = info
		
		
	# METHODES COMPLEXES

	
	def Update_date_time(self, __date, __time)
	"""Màj de l'objet avec la date et l'heure"""
		self.date = __date
		self.time = __time
	
	def Update_LB_data_msg_1(self, __num, __type, __current, __voltage, __active_power)
	"""Màj de l'objet avec les premières valeurs envoyées"""
		self.num = __num
		self.type = __type
		self.current = __current
		self.voltage = __voltage
		self.active_power = __active_power
	
	def Update_LB_data_msg_2(self, __power_factor, __reactive_power, __apparent_power, __freq)
	"""Màj de l'objet avec les secondes valeurs envoyées"""
		self.power_factor = __power_factor
		self.reactive_power = __reactive_power
		self.apparent_power = __apparent_power
		self.freq = __freq
		
	
## CLASS DEFINITION FOR POWERMETER DATA. Use: store data acquired through the powermeter

class Powermeter_data_class :

	# INITIALISATION

	def __init__(self):
	"""à completer"""

	# METHODES SIMPLES 
	"""à completer"""
	
	
	
###########################################################################
## GESTION DES FICHIERS						    	 
###########################################################################


## INITIALISATION DES FICHIERS

def Init_file_charge(): """à completer"""
	return


## ECRITURE D'UNE LIGNE DANS UN FICHIER

def W_line_file(nom_fichier, ligne_data):
	fichier = open(nom_fichier, "a")
	fichier.write(ligne_data)
	fichier.close()
	return
	
## AFFICHAGE D'UNE LIGNE DANS UN FICHIER

def D_line_file(nom_fichier, num_ligne):
	fichier = open(nom_fichier, "r")
	print fichier.readline(num_ligne)
	fichier.close()
	return
	
## AFFICHAGE D'UN FICHIER ENTIER

def D_file(nom_fichier):
	fichier = open(nom_fichier, "r")
	print fichier.read()
	fichier.close()
	return
	
	

###########################################################################
## GESTION DES DONNEES						    	 
###########################################################################


## MISE EN FORMAT LIGNE FICHIER CHARGE
"""à completer, le mettre directement dans les méthodes de l'objet Load_Balancer_data_class ?"""



## MISE EN FORMAT LIGNE FICHIER CHARGE TOTALE
"""à completer"""



## MISE EN FORMAT LIGNE FICHIER CHARGE MPPT
"""à completer"""


## MISE EN FORMAT LIGNE FICHIER POWERMETER
"""à completer"""



###########################################################################
## MANIPULATION DES DONNEES						    	 
###########################################################################


## CALCUL DE MOYENNE
"""à completer"""


## CALCUL DE RMS
"""à completer"""


## CALCUL DES VALEURS TOTALES CHARGES
"""à completer"""


## CALCUL DES VALEURS MPPT CHARGES
"""à completer"""

###########################################################################
## NOTES					    	 
###########################################################################


"""

class MPPT_Module(Module_class) :
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
	def __init__(self):
		self.ID = 3
		self.PWR_Out = 0.0 #Watts	
		self.OC = False
		self.SoC = 50  #% of usable energy

	def W_PWR_Out(self, info):
		self.PWR_Out = info

	def W_OC(self, info):
		self.OC = info

	def W_SoC(self, info):
		self.SoC = info


class INV_Module (Module_class) :
	def __init__(self):
		self.ID = 4
		self.Boost_OK = True #is boost output voltage ok
		self.INV_OK = True #is inverter output voltage ok

	def W_Boost_OK(self, info):
		self.Boost_OK = info

	def W_INV_OK(self, info):
		self.INV_OK = info


class LSW_Module (Module_class) :
	def __init__(self):
		self.ID = 5
		self.PWR_Out = {'L1' : 0.0,'L2' : 0.0,'L3' : 0.0,'L4' : 0.0,'L5' : 0.0,'L6' : 0.0,'L7' : 0.0,'L8' : 0.0} #Watts			
		self.Load_Stat = {'L1' : 'EDF','L2' : 'EDF','L3' : 'EDF','L4' : 'EDF','L5' : 'EDF','L6' : 'EDF','L7' : 'EDF','L8' : 'EDF'} #EDF/PV
		
		def W_PWR_Out(self, Load, PWR_val):
			self.PWR_Out[Load] = PWR_val
		
		def W_Load_Stat(self, Load, stat):
			self.Load_Stat[Load] = stat 

"""
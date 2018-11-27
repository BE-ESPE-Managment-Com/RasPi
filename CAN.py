#File Name : CAN.py
#Author : Tanguy SIMON
#Project : BE Interdisciplinaire ESPE

############################################################################















############################################################################
class CAN_Message :
	"""Structure of a CAN message"""
	def __init__(self, _ID, _Length, _Data):
		self.ID = _ID
		self.Length = _Length
		self.Data = _Data

MPPT_MMS_STAT = 0x421
BMS_MMS_STAT = 0x431
INV_MMS_STAT = 0x441
LSW_MMS_STAT = 0x451
MPPT_MMS_PWR = 0x322
BMS_MMS_SOC = 0x333
BMS_MMS_PWR = 0x332
LSW_MMS_LDATA = 0x354
MMS_MPPT_EN = 0x120
MMS_BMS_EN = 0x130
MMS_INV_EN = 0x140
MMS_LSW_EN = 0x150
MMS_MPPT_MAXPWR = 0x215
MMS_BMS_SWBATT = 0x116
MMS_LSW_SWLOADS = 0x216

def CAN_RX_Parser(Msg):
	if Msg.ID == MPPT_MMS_STAT :
		
	elif 




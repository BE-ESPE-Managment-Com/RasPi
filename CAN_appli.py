#File Name : CAN_appli.py
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
		
#CAN IDs
MPPT_MMS_STAT_ID = 	0x4211
BMS_MMS_STAT =		0x4311
INV_MMS_STAT =		0x4411
LSW_MMS_STAT =		0x4511
MPPT_MMS_PWR =		0x3212
BMS_MMS_SOC =		0x3313
BMS_MMS_PWR =		0x3312
LSW_MMS_LDATA =	0x3514
MMS_MPPT_EN =		0x1120
MMS_BMS_EN =		0x1130
MMS_INV_EN =		0x1140
MMS_LSW_EN =		0x1150
MMS_MPPT_MAXPWR =	0x2125
MMS_BMS_SWINV =	0x1126
MMS_LSW_SWLOADS =	0x2156
BMS_MMS_OCH =		0x1317
BMS_MMS_UCH =		0x1318
BMS_MMS_OT =		0x1319

#CAN message lenghts
MPPT_MMS_STAT_LENGTH =		1
BMS_MMS_STAT_LENGTH =		1
INV_MMS_STAT_LENGTH =		1
LSW_MMS_STAT_LENGTH =		1
MPPT_MMS_PWR_LENGTH =		2
BMS_MMS_SOC_LENGTH =		1
BMS_MMS_PWR_LENGTH =		2
LSW_MMS_LDATA_LENGTH =		8
MMS_MPPT_EN_LENGTH =		1
MMS_BMS_EN_LENGTH =			1
MMS_INV_EN_LENGTH =			1
MS_LSW_EN_LENGTH =			1
MMS_MPPT_MAXPWR_LENGTH =		2
MMS_BMS_SWBATT_LENGTH =		1
MMS_LSW_SWLOADS_LENGTH 		8
BMS_MMS_OCH_LENGTH =		1
BMS_MMS_UCH_LENGTH =		1
BMS_MMS_OT_LENGTH =			1

def CAN_RX_Parser(Msg):
	if Msg.ID == MPPT_MMS_STAT :
		
	elif 




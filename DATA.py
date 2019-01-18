# File Name : DATA.py
# Author : Amélie MEYER / Tanguy SIMON
# Project : BE Interdisciplinaire ESPE

###########################################################################
## IMPORT
###########################################################################

import csv

###########################################################################
## CLASSES
###########################################################################

## [UNUSED] CLASS DEFINITION FOR MODULES. Can be used for checking initialisation and communication

class Module_class:

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
        else:
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

class Load_Balancer_data_class:

    # INITIALISATION

    def __init__(self, __date="", __time="", __num=0, __type="", __current=0, __voltage=0, __active_power=0,
                 __reactive_power=0, __apparent_power=0, __power_factor=0, __freq=0):
        self.date = __date
        self.time = __time
        self.num = __num  ## load number (1 to 5)
        self.type = __type  ## "EDF" or "PV"
        self.current = __current  ## RMS value (A)
        self.voltage = __voltage  ## RMS value (V)
        self.active_power = __active_power  ## (W)
        self.reactive_power = __reactive_power  ## (VAR)
        self.apparent_power = __apparent_power  ## (VA)
        self.power_factor = __power_factor
        self.freq = __freq  ## (Hz)

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

    def Update_date_time(self, __date, __time):
        """Màj de l'objet avec la date et l'heure"""
        self.date = __date
        self.time = __time

    def Update_LB_data_msg_1(self, __num, __type, __current, __voltage, __active_power):
        """Màj de l'objet avec les premières valeurs envoyées"""
        self.num = __num
        self.type = __type
        self.current = __current
        self.voltage = __voltage
        self.active_power = __active_power

    def Update_LB_data_msg_2(self, __power_factor, __reactive_power, __apparent_power, __freq):
        """Màj de l'objet avec les secondes valeurs envoyées"""
        self.power_factor = __power_factor
        self.reactive_power = __reactive_power
        self.apparent_power = __apparent_power
        self.freq = __freq

    # AFFICHAGE SUR LA CONSOLE DE TOUS LES PARAMETRES

    def Display_everything(self):
        """Affichage de l'intégralité de l'objet"""
        print("Date: ",self.date)
        print("Time: ", self.time)
        print("Num: ", self.num)
        print("Type: ", self.type)
        print("Current: ", self.current, "A")
        print("Voltage: ", self.voltage, "V")
        print("Active Power: ", self.active_power, "W")
        print("Reactive Power: ", self.reactive_power, "VAR")
        print("Apparent Power: ", self.apparent_power, "VA")
        print("Power Factor: ", self.power_factor)
        print("Freq: ", self.freq, "Hz")

    # MISE EN FORMAT LIGNE POUR ECRITURE FICHIER CSV

    def Format_in_line(self):
        """Mise en format ligne CSV"""
        line = [str(self.date), str(self.time), str(self.num), str(self.type), str(self.current), str(self.voltage),
                str(self.active_power), str(self.reactive_power), str(self.apparent_power), str(self.power_factor),
                (self.freq)]
        return line

## CLASS DEFINITION FOR TOTAL LOADS. Use : store computed data

class LBtot_data_class:

    # INITIALISATION

    def __init__(self, __date="", __time="", __current_EDF=0, __current_PV=0, __voltage_EDF=0, __voltage_PV=0,
                 __active_power_EDF=0, __active_power_PV=0, __reactive_power_EDF=0, __reactive_power_PV=0,
                 __apparent_power_EDF=0, __apparent_power_PV=0):
        self.date = __date
        self.time = __time
        self.current_EDF = __current_EDF  ## EDF loads RMS value (A)
        self.current_PV = __current_PV  ## PV loads RMS value (A)
        self.voltage_EDF = __voltage_EDF  ## EDF loads RMS value (V)
        self.voltage_PV = __voltage_PV  ## PV loads RMS value (V)
        self.active_power_EDF = __active_power_EDF  ## EDF (W)
        self.active_power_PV = __active_power_PV  ## PV (W)
        self.reactive_power_EDF = __reactive_power_EDF  ## (VAR)
        self.reactive_power_PV = __reactive_power_PV  ## (VAR)
        self.apparent_power_EDF = __apparent_power_EDF  ## (VA)
        self.apparent_power_PV = __apparent_power_PV  ## (VA)

    # METHODES SIMPLES

    def Is_date(self, info):
        self.date = info

    def Is_time(self, info):
        self.time = info

    def Is_current_EDF(self, info):
        self.current_EDF = info

    def Is_current_PV(self, info):
        self.current_PV = info

    def Is_voltage_EDF(self, info):
        self.voltage_EDF = info

    def Is_voltage_PV(self, info):
        self.voltage_PV = info

    def Is_active_power_EDF(self, info):
        self.active_power_EDF = info

    def Is_active_power_PV(self, info):
        self.active_power_PV = info

    def Is_reactive_power_EDF(self, info):
        self.reactive_power_EDF = info

    def Is_reactive_power_PV(self, info):
        self.reactive_power_PV = info

    def Is_apparent_power_EDF(self, info):
        self.apparent_power_EDF = info

    def Is_apparent_power_PV(self, info):
        self.apparent_power_PV = info

    def Update_date_time(self, __date, __time):
        """Màj de l'objet avec la date et l'heure"""
        self.date = __date
        self.time = __time

    # AFFICHAGE SUR LA CONSOLE DE TOUS LES PARAMETRES

    def Display_everything(self):
        """Affichage de l'intégralité de l'objet"""
        print("Date: ", self.date)
        print("Time: ", self.time)
        print("Current EDF: ", self.current_EDF, "A")
        print("Current PV: ", self.current_PV, "A")
        print("Voltage EDF: ", self.voltage_EDF, "V")
        print("Voltage PV: ", self.voltage_PV, "V")
        print("Active Power EDF: ", self.active_power_EDF, "W")
        print("Active Power PV: ", self.active_power_PV, "W")
        print("Reactive Power EDF: ", self.reactive_power_EDF, "VAR")
        print("Reactive Power PV: ", self.reactive_power_PV, "VAR")
        print("Apparent Power EDF: ", self.apparent_power_EDF, "VA")
        print("Apparent Power PV: ", self.apparent_power_PV, "VA")

    # MISE EN FORMAT LIGNE POUR ECRITURE FICHIER CSV

    def Format_in_line(self):
        """Mise en format ligne CSV"""
        line = [str(self.date), str(self.time), str(self.current_EDF), str(self.current_PV), str(self.voltage_EDF),
                str(self.voltage_PV), str(self.active_power_EDF), str(self.active_power_PV),
                str(self.reactive_power_EDF), str(self.reactive_power_PV), str(self.apparent_power_EDF),
                str(self.apparent_power_PV)]
        return line

## CLASS DEFINITION FOR MPPT DATA. Use: store data acquired through the MPPT

class MPPT_data_class:

    # INITIALISATION

    def __init__(self, __date="", __time="", __power=0, __switch_state="", __state=""):
        self.date = __date
        self.time = __time
        self.power = __power  ## power output
        self.switch_state = __switch_state  ## "on" or "off"
        self.state = __state  ## "enabled" or "disabled"

    # METHODES SIMPLES

    def Is_date(self, info):
        self.date = info

    def Is_time(self, info):
        self.time = info

    def Is_power(self, info):
        self.power = info

    def Is_switch_state(self, info):
        self.switch_state = info

    def Is_state(self, info):
        self.state = info

    def Update_date_time(self, __date, __time):
        """Màj de l'objet avec la date et l'heure"""
        self.date = __date
        self.time = __time

    # AFFICHAGE SUR LA CONSOLE DE TOUS LES PARAMETRES

    def Display_everything(self):
        """Affichage de l'intégralité de l'objet"""
        print("Date: ", self.date)
        print("Time: ", self.time)
        print("Power: ", self.power, "W")
        print("Switch state: ", self.switch_state)
        print("State: ", self.state)


    # MISE EN FORMAT LIGNE POUR ECRITURE FICHIER CSV

    def Format_in_line(self):
        """Mise en format ligne CSV"""
        line = [str(self.date), str(self.time), str(self.power), str(self.switch_state), str(self.state)]
        return line



## CLASS DEFINITION FOR BATTERY DATA. Use: store data acquired through the BATTERY

class BATT_data_class:

    # INITIALISATION

    def __init__(self, __date="", __time="", __battery_level=0, __power=0, __sign=0, __state="", __overcharge="",
                 __undercharge="", __overtemperature=""):
        self.date = __date
        self.time = __time
        self.battery_level = __battery_level # (%)
        self.power = __power # power input/output
        self.sign =__sign # -1:charging or 1:discharging
        self.state = __state # "enabled" or "disabled"
        self.overcharge = __overcharge # "yes" or "no"
        self.undercharge = __undercharge # "yes" or "no"
        self.overtemperature = __overtemperature # "yes" or "no"

    # METHODES SIMPLES

    def Is_date(self, info):
        self.date = info

    def Is_time(self, info):
        self.time = info

    def Is_battery_level(self, info):
        self.battery_level = info

    def Is_power(self, info):
        self.power = info

    def Is_sign(self, info):
        self.sign = info

    def Is_state(self, info):
        self.state = info

    def Is_overcharge(self, info):
        self.overcharge = info

    def Is_undercharge(self, info):
        self.undercharge = info

    def Is_overtemperature(self, info):
        self.overtemperature = info

    def Update_date_time(self, __date, __time):
        """Màj de l'objet avec la date et l'heure"""
        self.date = __date
        self.time = __time


    # AFFICHAGE SUR LA CONSOLE DE TOUS LES PARAMETRES

    def Display_everything(self):
        """Affichage de l'intégralité de l'objet"""
        print("Date: ", self.date)
        print("Time: ", self.time)
        print("Battery level: ", self.battery_level, "%")
        print("Power: ", self.power, "W")
        print("Sign: ", self.sign)
        print("State:", self.state)
        print("Overcharge: ", self.overcharge)
        print("Undercharge: ", self.undercharge)
        print("Overtemperature: ", self.overtemperature)

    # MISE EN FORMAT LIGNE POUR ECRITURE FICHIER CSV

    def Format_in_line(self):
        """Mise en format ligne CSV"""
        line = [str(self.date), str(self.time), str(self.battery_level), str(self.power), str(self.sign),
                str(self.state), str(self.overcharge), str(self.undercharge),
                str(self.overtemperature)]
        return line



###########################################################################
## GESTION DES FICHIERS - VERSION TEXTE (UNUSED)
###########################################################################


## ECRITURE D'UNE LIGNE DANS UN FICHIER

def W_line_file(nom_fichier, ligne_data):
    with open(nom_fichier, 'a') as fichier:
        fichier.write(ligne_data)
    fichier.close()
    return


## AFFICHAGE D'UNE LIGNE DANS UN FICHIER

def D_line_file(nom_fichier, num_ligne):
    with open(nom_fichier, 'r') as fichier:
        print(fichier.readline(num_ligne))
    fichier.close()
    return


## AFFICHAGE D'UN FICHIER ENTIER

def D_file(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        print(fichier.read())
    fichier.close()
    return


###########################################################################
## GESTION DES FICHIERS - VERSION CSV (USED)
###########################################################################


## INITIALISATION DES FICHIERS CHARGES SIMPLE

def Init_file_charge_csv(nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        fieldnames = ['date','time','num','type','current','voltage','active_power','reactive_power','apparent_power',
                      'power_factor','freq']
        writer = csv.DictWriter(fichier, fieldnames = fieldnames, delimiter = ';')
        writer.writeheader()
    return

## INITIALISATION DU FICHIER CHARGES TOTALES

def Init_file_chargetot_csv(nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        fieldnames = ['date','time','current_EDF','current_PV','voltage_EDF','voltage_PV','active_power_EDF',
                      'active_power_PV','reactive_power_EDF','reactive_power_PV','apparent_power_EDF',
                      'apparent_power_PV']
        writer = csv.DictWriter(fichier, fieldnames = fieldnames, delimiter = ';')
        writer.writeheader()
    return

## INITIALISATION DU FICHIER DATA MPPT

def Init_file_mppt_csv(nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        fieldnames = ['date','time','power','switch_state','state']
        writer = csv.DictWriter(fichier, fieldnames = fieldnames, delimiter = ';')
        writer.writeheader()
    return

## INITIALISATION DU FICHIER DATA BATT

def Init_file_batt_csv(nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        fieldnames = ['date','time', 'battery_level', 'power','sign','state', 'overcharge', 'undercharge', 'overtemperature']
        writer = csv.DictWriter(fichier, fieldnames = fieldnames, delimiter = ';')
        writer.writeheader()
    return


## ECRITURE D'UNE LIGNE DANS UN FICHIER CSV
# ligne_data format: ['x1', 'x2', 'x3', ..., 'x11']

def W_line_file_csv(nom_fichier, ligne_data):
    with open(nom_fichier, 'a') as fichier:
        writer = csv.writer(fichier, delimiter=';')
        writer.writerow(ligne_data)
    fichier.close()
    return


## RECUPERATION D'UNE LIGNE D'UN FICHIER CSV CHARGE SIMPLE VERS UN OBJET LOAD

def G_line_file_charge_csv(nom_fichier, num_ligne):
    with open(nom_fichier, 'r') as fichier:
        reader = csv.reader(fichier, delimiter=';')
        rownum = 0
        info_charge = Load_Balancer_data_class()
        for row in reader:
            if (rownum == 0):
                header = row
            if (rownum == num_ligne):
                colnum = 0
                for col in row:
                    if (header[colnum]=='date'):
                        info_charge.Is_date(col)
                    if (header[colnum]=='time'):
                        info_charge.Is_time(col)
                    if (header[colnum]=='num'):
                        info_charge.Is_num(col)
                    if (header[colnum]=='type'):
                        info_charge.Is_type(col)
                    if (header[colnum]=='current'):
                        info_charge.Is_current(col)
                    if (header[colnum]=='voltage'):
                        info_charge.Is_voltage(col)
                    if (header[colnum]=='active_power'):
                        info_charge.Is_active_power(col)
                    if (header[colnum]=='reactive_power'):
                        info_charge.Is_reactive_power(col)
                    if (header[colnum] == 'apparent_power'):
                        info_charge.Is_apparent_power(col)
                    if (header[colnum] == 'power_factor'):
                        info_charge.Is_power_factor(col)
                    if (header[colnum] == 'freq'):
                        info_charge.Is_freq(col)
                    colnum += 1
            rownum += 1
    fichier.close()
    return info_charge

## RECUPERATION D'UNE LIGNE D'UN FICHIER CSV CHARGE TOTALE VERS UN OBJET LOADTOT

def G_line_file_chargetot_csv(nom_fichier, num_ligne):
    with open(nom_fichier, 'r') as fichier:
        reader = csv.reader(fichier, delimiter=';')
        rownum = 0
        info_charge = LBtot_data_class()
        for row in reader:
            if (rownum == 0):
                header = row
            if (rownum == num_ligne):
                colnum = 0
                for col in row:
                    if (header[colnum]=='date'):
                        info_charge.Is_date(col)
                    if (header[colnum]=='time'):
                        info_charge.Is_time(col)
                    if (header[colnum]=='current_EDF'):
                        info_charge.Is_current_EDF(col)
                    if (header[colnum]=='current_PV'):
                        info_charge.Is_current_PV(col)
                    if (header[colnum]=='voltage_EDF'):
                        info_charge.Is_voltage_EDF(col)
                    if (header[colnum]=='voltage_PV'):
                        info_charge.Is_voltage_PV(col)
                    if (header[colnum]=='active_power_EDF'):
                        info_charge.Is_active_power_EDF(col)
                    if (header[colnum]=='active_power_PV'):
                        info_charge.Is_active_power_PV(col)
                    if (header[colnum]=='reactive_power_EDF'):
                        info_charge.Is_reactive_power_EDF(col)
                    if (header[colnum]=='reactive_power_PV'):
                        info_charge.Is_reactive_power_PV(col)
                    if (header[colnum] == 'apparent_power_EDF'):
                        info_charge.Is_apparent_power_EDF(col)
                    if (header[colnum] == 'apparent_power_PV'):
                        info_charge.Is_apparent_power_PV(col)
                    colnum += 1
            rownum += 1
    fichier.close()
    return info_charge

## RECUPERATION D'UNE LIGNE D'UN FICHIER CSV MPPT DATA VERS UN OBJET MPPTDATA

def G_line_file_mppt_csv(nom_fichier, num_ligne):
    with open(nom_fichier, 'r') as fichier:
        reader = csv.reader(fichier, delimiter=';')
        rownum = 0
        info_charge = MPPT_data_class()
        for row in reader:
            if (rownum == 0):
                header = row
            if (rownum == num_ligne):
                colnum = 0
                for col in row:
                    if (header[colnum]=='date'):
                        info_charge.Is_date(col)
                    if (header[colnum]=='time'):
                        info_charge.Is_time(col)
                    if (header[colnum]=='power'):
                        info_charge.Is_power(col)
                    if (header[colnum]=='switch_state'):
                        info_charge.Is_switch_state(col)
                    if (header[colnum]=='state'):
                        info_charge.Is_state(col)
                    colnum += 1
            rownum += 1
    fichier.close()
    return info_charge

## RECUPERATION D'UNE LIGNE D'UN FICHIER CSV BATTERY DATA VERS UN OBJET BATTERYDATA

def G_line_file_battery_csv(nom_fichier, num_ligne):
    with open(nom_fichier, 'r') as fichier:
        reader = csv.reader(fichier, delimiter=';')
        rownum = 0
        info_charge = BATT_data_class()
        for row in reader:
            if (rownum == 0):
                header = row
            if (rownum == num_ligne):
                colnum = 0
                for col in row:
                    if (header[colnum]=='date'):
                        info_charge.Is_date(col)
                    if (header[colnum]=='time'):
                        info_charge.Is_time(col)
                    if (header[colnum]=='battery_level'):
                        info_charge.Is_battery_level(col)
                    if (header[colnum]=='power'):
                        info_charge.Is_power(col)
                    if (header[colnum]=='sign'):
                        info_charge.Is_sign(col)
                    if (header[colnum]=='state'):
                        info_charge.Is_state(col)
                    if (header[colnum]=='overcharge'):
                        info_charge.Is_overcharge(col)
                    if (header[colnum]=='undercharge'):
                        info_charge.Is_undercharge(col)
                    if (header[colnum]=='overtemperature'):
                        info_charge.Is_overtemperature(col)
                    colnum += 1
            rownum += 1
    fichier.close()
    return info_charge

## AFFICHAGE CONSOLE D'UNE LIGNE DANS UN FICHIER CSV

def D_line_file_csv(nom_fichier, num_ligne):
    with open(nom_fichier, 'r') as fichier:
        reader = csv.reader(fichier, delimiter=';')
        rownum = 0
        for row in reader:
            # save header row
            if rownum == 0:
                header = row
            elif (rownum == num_ligne):
                colnum = 0
                for col in row:
                    print(header[colnum], col)
                    colnum += 1
            rownum += 1
    fichier.close()
    return


## AFFICHAGE CONSOLE D'UN FICHIER CSV ENTIER

def D_file_csv(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        reader = csv.reader(fichier, delimiter=';')
        rownum = 0
        for row in reader:
            # save header row
            if rownum == 0:
                header = row
            else:
                colnum = 0
                for col in row:
                    print(header[colnum], col)
                    colnum += 1
            rownum += 1
    fichier.close()
    return


###########################################################################
## MANIPULATION DES DONNEES
###########################################################################


## RECUPERATION DES INDICES DU FICHIER CSV CORRESPONDANTS A UNE BANDE TEMPORELLE DONNEE
## Note: date format should be: dd/mm/yyyy
def G_linenumber(nom_fichier,date_inf,time_inf,date_sup,time_sup):
    line_inf=0
    line_sup=0
    with open(nom_fichier, 'r') as fichier:
        reader = csv.reader(fichier, delimiter=';')
        rownum = 0
        for row in reader:
            colnum = 0
            # get date and time from line
            for col in row:
                # using only date and time column
                if (colnum == 0):
                    date_line = col
                elif (colnum == 1):
                    time_line = col
                colnum += 1

            if (rownum != 0): # doesn't include header line

                # update line_inf
                earlier_year1 = (int(date_line[6:10]) < int(date_inf[6:10]))
                same_year1 = (int(date_line[6:10]) == int(date_inf[6:10]))
                earlier_month1 = (int(date_line[3:5]) < int(date_inf[3:5]))
                same_month1 = (int(date_line[3:5]) == int(date_inf[3:5]))
                earlier_day1 = (int(date_line[0:2]) < int(date_inf[0:2]))
                same_day1 = (int(date_line[0:2]) == int(date_inf[0:2]))
                earlier_hour1 = (int(time_line[0:2]) < int(time_inf[0:2]))
                same_hour1 = (int(time_line[0:2]) == int(time_inf[0:2]))
                earlier_minute1 =(int(time_line[3:5]) < int(time_inf[3:5]))
                same_minute1 = (int(time_line[3:5]) == int(time_inf[3:5]))

                if (earlier_year1 |
                   (same_year1 & earlier_month1) |
                   (same_year1 & same_month1 & earlier_day1) |
                   (same_year1 & same_month1 & same_day1 & earlier_hour1) |
                   (same_year1 & same_month1 & same_day1 & same_hour1 & earlier_minute1) |
                   (same_year1 & same_month1 & same_day1 & same_hour1 & same_minute1)):
                    line_inf += 1


                # update line_sup
                earlier_year2 = (int(date_line[6:10]) < int(date_sup[6:10]))
                same_year2 = (int(date_line[6:10]) == int(date_sup[6:10]))
                earlier_month2 = (int(date_line[3:5]) < int(date_sup[3:5]))
                same_month2 = (int(date_line[3:5]) == int(date_sup[3:5]))
                earlier_day2 = (int(date_line[0:2]) < int(date_sup[0:2]))
                same_day2 = (int(date_line[0:2]) == int(date_sup[0:2]))
                earlier_hour2 = (int(time_line[0:2]) < int(time_sup[0:2]))
                same_hour2 = (int(time_line[0:2]) == int(time_sup[0:2]))
                earlier_minute2 =(int(time_line[3:5]) < int(time_sup[3:5]))
                same_minute2 = (int(time_line[3:5]) == int(time_sup[3:5]))

                if (earlier_year2 |
                   (same_year2 & earlier_month2) |
                   (same_year2 & same_month2 & earlier_day2) |
                   (same_year2 & same_month2 & same_day2 & earlier_hour2) |
                   (same_year2 & same_month2 & same_day2 & same_hour2 & earlier_minute2) |
                   (same_year2 & same_month2 & same_day2 & same_hour2 & same_minute2)):
                    line_sup += 1
            rownum += 1
    fichier.close()
    return [line_inf,line_sup]


## CALCUL DES COURANTS TOTAUX. Note: chargex should be Load_Balancer_class type
def Calculate_current(charge1,charge2,charge3,charge4,charge5):
    charge_EDF = 0
    charge_PV = 0

    # charge1
    if (charge1.type=='EDF'):
        charge_EDF = charge_EDF + int(charge1.current)
    elif (charge1.type=='PV'):
        charge_PV = charge_PV + int(charge1.current)

    # charge2
    if (charge2.type=='EDF'):
        charge_EDF = charge_EDF + int(charge2.current)
    elif (charge2.type=='PV'):
        charge_PV = charge_PV + int(charge2.current)

    # charge3
    if (charge3.type=='EDF'):
        charge_EDF = charge_EDF + int(charge3.current)
    elif (charge3.type=='PV'):
        charge_PV = charge_PV + int(charge3.current)

    # charge4
    if (charge4.type=='EDF'):
        charge_EDF = charge_EDF + int(charge4.current)
    elif (charge4.type=='PV'):
        charge_PV = charge_PV + int(charge4.current)

    # charge5
    if (charge5.type=='EDF'):
        charge_EDF = charge_EDF + int(charge5.current)
    elif (charge5.type=='PV'):
        charge_PV = charge_PV + int(charge5.current)

    return [charge_EDF,charge_PV]


## CALCUL DES TENSIONS TOTALES. Note: chargex should be Load_Balancer_class type
def Calculate_voltage(charge1,charge2,charge3,charge4,charge5):
    charge_EDF = 0
    charge_PV = 0

    # charge1
    if (charge1.type=='EDF'):
        charge_EDF = charge_EDF + int(charge1.voltage)
    elif (charge1.type=='PV'):
        charge_PV = charge_PV + int(charge1.voltage)

    # charge2
    if (charge2.type=='EDF'):
        charge_EDF = charge_EDF + int(charge2.voltage)
    elif (charge2.type=='PV'):
        charge_PV = charge_PV + int(charge2.voltage)

    # charge3
    if (charge3.type=='EDF'):
        charge_EDF = charge_EDF + int(charge3.voltage)
    elif (charge3.type=='PV'):
        charge_PV = charge_PV + int(charge3.voltage)

    # charge4
    if (charge4.type=='EDF'):
        charge_EDF = charge_EDF + int(charge4.voltage)
    elif (charge4.type=='PV'):
        charge_PV = charge_PV + int(charge4.voltage)

    # charge5
    if (charge5.type=='EDF'):
        charge_EDF = charge_EDF + int(charge5.voltage)
    elif (charge5.type=='PV'):
        charge_PV = charge_PV + int(charge5.voltage)

    return [charge_EDF,charge_PV]


## CALCUL DES PUISSANCES ACTIVES TOTALES. Note: chargex should be Load_Balancer_class type
def Calculate_active_power(charge1,charge2,charge3,charge4,charge5):
    charge_EDF = 0
    charge_PV = 0

    # charge1
    if (charge1.type=='EDF'):
        charge_EDF = charge_EDF + int(charge1.active_power)
    elif (charge1.type=='PV'):
        charge_PV = charge_PV + int(charge1.active_power)

    # charge2
    if (charge2.type=='EDF'):
        charge_EDF = charge_EDF + int(charge2.active_power)
    elif (charge2.type=='PV'):
        charge_PV = charge_PV + int(charge2.active_power)

    # charge3
    if (charge3.type=='EDF'):
        charge_EDF = charge_EDF + int(charge3.active_power)
    elif (charge3.type=='PV'):
        charge_PV = charge_PV + int(charge3.active_power)

    # charge4
    if (charge4.type=='EDF'):
        charge_EDF = charge_EDF + int(charge4.active_power)
    elif (charge4.type=='PV'):
        charge_PV = charge_PV + int(charge4.active_power)

    # charge5
    if (charge5.type=='EDF'):
        charge_EDF = charge_EDF + int(charge5.active_power)
    elif (charge5.type=='PV'):
        charge_PV = charge_PV + int(charge5.active_power)

    return [charge_EDF,charge_PV]


## CALCUL DES PUISSANCES REACTIVES TOTALES. Note: chargex should be Load_Balancer_class type
def Calculate_reactive_power(charge1,charge2,charge3,charge4,charge5):
    charge_EDF = 0
    charge_PV = 0

    # charge1
    if (charge1.type=='EDF'):
        charge_EDF = charge_EDF + int(charge1.reactive_power)
    elif (charge1.type=='PV'):
        charge_PV = charge_PV + int(charge1.reactive_power)

    # charge2
    if (charge2.type=='EDF'):
        charge_EDF = charge_EDF + int(charge2.reactive_power)
    elif (charge2.type=='PV'):
        charge_PV = charge_PV + int(charge2.reactive_power)

    # charge3
    if (charge3.type=='EDF'):
        charge_EDF = charge_EDF + int(charge3.reactive_power)
    elif (charge3.type=='PV'):
        charge_PV = charge_PV + int(charge3.reactive_power)

    # charge4
    if (charge4.type=='EDF'):
        charge_EDF = charge_EDF + int(charge4.reactive_power)
    elif (charge4.type=='PV'):
        charge_PV = charge_PV + int(charge4.reactive_power)

    # charge5
    if (charge5.type=='EDF'):
        charge_EDF = charge_EDF + int(charge5.reactive_power)
    elif (charge5.type=='PV'):
        charge_PV = charge_PV + int(charge5.reactive_power)

    return [charge_EDF,charge_PV]



## CALCUL DES PUISSANCES APPARENTES TOTALES. Note: chargex should be Load_Balancer_class type
def Calculate_apparent_power(charge1,charge2,charge3,charge4,charge5):
    charge_EDF = 0
    charge_PV = 0

    # charge1
    if (charge1.type=='EDF'):
        charge_EDF = charge_EDF + int(charge1.apparent_power)
    elif (charge1.type=='PV'):
        charge_PV = charge_PV + int(charge1.apparent_power)

    # charge2
    if (charge2.type=='EDF'):
        charge_EDF = charge_EDF + int(charge2.apparent_power)
    elif (charge2.type=='PV'):
        charge_PV = charge_PV + int(charge2.apparent_power)

    # charge3
    if (charge3.type=='EDF'):
        charge_EDF = charge_EDF + int(charge3.apparent_power)
    elif (charge3.type=='PV'):
        charge_PV = charge_PV + int(charge3.apparent_power)

    # charge4
    if (charge4.type=='EDF'):
        charge_EDF = charge_EDF + int(charge4.apparent_power)
    elif (charge4.type=='PV'):
        charge_PV = charge_PV + int(charge4.apparent_power)

    # charge5
    if (charge5.type=='EDF'):
        charge_EDF = charge_EDF + int(charge5.apparent_power)
    elif (charge5.type=='PV'):
        charge_PV = charge_PV + int(charge5.apparent_power)

    return [charge_EDF,charge_PV]

## [NOT WORKING YET] ERASE ANY UNWANTED BLANK LINES. Should be implemented each time a CSV file is open
def Erase_blanks(nom_fichier):
    input = open(nom_fichier, 'r')
    output = open(nom_fichier, 'w')
    writer = csv.writer(output)
    for row in csv.reader(input):
        if any(row):
            writer.writerow(row)
    input.close()
    output.close()

###########################################################################
## TEST LOOPS
###########################################################################


## FILE INITIALISATION - OK

#Init_file_batt_csv('battery.csv')
#Init_file_chargetot_csv('charge_tot.csv')
#Init_file_charge_csv('charge1.csv')
#Init_file_charge_csv('charge2.csv')
#Init_file_charge_csv('charge3.csv')
#Init_file_charge_csv('charge4.csv')
#Init_file_charge_csv('charge5.csv')
#Init_file_mppt_csv('mppt.csv')

# WRITE IN FILES - OK

#W_line_file_csv('battery.csv', ['11/01/2019', '16:59', '45', '12', 'charging', 'enabled', 'no', 'no', 'no'])
#W_line_file_csv('charge1.csv', ['11/01/2019', '16:59', '1', 'EDF', '1', '1', '1', '1', '1', '0.1', '10'])
#W_line_file_csv('charge2.csv', ['11/01/2019', '16:59', '2', 'PV', '2', '2', '2', '2', '2', '0.2', '20'])
#W_line_file_csv('charge3.csv', ['11/01/2019', '16:59', '3', 'EDF', '3', '3', '3', '3', '3', '0.3', '30'])
#W_line_file_csv('charge4.csv', ['11/01/2019', '16:59', '4', 'PV', '4', '4', '4', '4', '4', '0.4', '40'])
#W_line_file_csv('charge5.csv', ['11/01/2019', '16:59', '5', 'EDF', '5', '5', '5', '5', '5', '0.5', '50'])
#W_line_file_csv('mppt.csv', ['11/01/19', '16:59', '32', 'on', 'enabled'])

# DISPLAY LINE IN FILE - OK

#D_line_file_csv('battery.csv',2)
#D_line_file_csv('charge1.csv',2)
#D_line_file_csv('charge2.csv',2)
#D_line_file_csv('charge3.csv',2)
#D_line_file_csv('charge4.csv',2)
#D_line_file_csv('charge5.csv',2)
#D_line_file_csv('mppt.csv',2)

# GET OBJECT FROM FILE - OK

#battery = G_line_file_battery_csv('battery.csv',2)
#charge1 = G_line_file_charge_csv('charge1.csv',2)
#charge2 = G_line_file_charge_csv('charge2.csv',2)
#charge3 = G_line_file_charge_csv('charge3.csv',2)
#charge4 = G_line_file_charge_csv('charge4.csv',2)
#charge5 = G_line_file_charge_csv('charge5.csv',2)
#mppt = G_line_file_mppt_csv('mppt.csv', 2)

# DISPLAY OBJECT VALUE - OK

#battery.Display_everything()
#charge1.Display_everything()
#charge2.Display_everything()
#charge3.Display_everything()
#charge4.Display_everything()
#charge5.Display_everything()
#mppt.Display_everything()

# CALCULATE TOTAL LOAD - OK

#[current_EDF, current_PV] = Calculate_current(charge1,charge2,charge3,charge4,charge5)
#[voltage_EDF, voltage_PV] = Calculate_voltage(charge1,charge2,charge3,charge4,charge5)
#[active_power_EDF, active_power_PV] = Calculate_active_power(charge1,charge2,charge3,charge4,charge5)
#[reactive_power_EDF, reactive_power_PV] = Calculate_reactive_power(charge1,charge2,charge3,charge4,charge5)
#[apparent_power_EDF, apparent_power_PV] = Calculate_apparent_power(charge1,charge2,charge3,charge4,charge5)

#W_line_file_csv('charge_tot.csv', ['11/01/2019', '16:59', current_EDF, current_PV, voltage_EDF, voltage_PV,
#                active_power_EDF, active_power_PV, reactive_power_EDF, reactive_power_PV, apparent_power_EDF,
#                apparent_power_PV])

#D_line_file_csv('charge_tot.csv',2)


# WRITE IN LINE FROM OBJECT - OK

#W_line_file_csv('battery.csv', battery.Format_in_line())
#W_line_file_csv('charge1.csv', charge1.Format_in_line())
#W_line_file_csv('charge2.csv', charge2.Format_in_line())
#W_line_file_csv('charge3.csv', charge3.Format_in_line())
#W_line_file_csv('charge4.csv', charge4.Format_in_line())
#W_line_file_csv('charge5.csv', charge5.Format_in_line())
#W_line_file_csv('mppt.csv', mppt.Format_in_line())

#charge_tot = G_line_file_chargetot_csv('charge_tot.csv',2)
#W_line_file_csv('charge_tot.csv', charge_tot.Format_in_line())


# GET LINE NUMBERS FOR A SPECIFIED PERIOD OF TIME - OK

#line_numbers = G_linenumber('charge1.csv','11/01/2019','16:59','14/01/2019','18:59')
#print(line_numbers)

# ERASE BLANK LINES FROM FILES - NOT WORKING YET

#Erase_blanks('charge4.csv')

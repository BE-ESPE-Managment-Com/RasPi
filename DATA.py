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

## CLASS DEFINITION FOR MODULES. Use: check initialisation and communication

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
        self.num = __num  ## charge number
        self.type = __type  ## "EDF" or "MPPT"
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

    # METHODES COMPLEXES

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
        line = [str(self.date), str(self.time), str(self.num), str(self.type), str(self.current), str(self.voltage), str(self.active_power), str(self.reactive_power), str(self.apparent_power), str(self.power_factor), str(self.freq)]
        return line

## CLASS DEFINITION FOR TOTAL LOADS. Use : store computed data

class LBtot_data_class:

    # INITIALISATION

    def __init__(self):
        """à completer"""

        # METHODES SIMPLES
        """à completer"""

## CLASS DEFINITION FOR MPPT DATA. Use: store data acquired through the MPPT

class MPPT_data_class:

    # INITIALISATION

    def __init__(self):
        """à completer"""

        # METHODES SIMPLES
        """à completer"""


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


# INITIALISATION DES FICHIERS CHARGES SIMPLE

def Init_file_charge_csv(nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        fieldnames = ['date','time','num','type','current','voltage','active_power','reactive_power','apparent_power','power_factor','freq']
        writer = csv.DictWriter(fichier, fieldnames = fieldnames, delimiter = ';')
        writer.writeheader()
    return

# INITIALISATION DU FICHIER CHARGES TOTALES

def Init_file_chargetot_csv(nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        fieldnames = """à compléter"""
        writer = csv.DictWriter(fichier, fieldnames = fieldnames, delimiter = ';')
        writer.writeheader()
    return

# INITIALISATION DU FICHIER DATA MPPT

def Init_file_mppt_csv(nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        fieldnames = """à compléter"""
        writer = csv.DictWriter(fichier, fieldnames = fieldnames, delimiter = ';')
        writer.writeheader()
    return


# ECRITURE D'UNE LIGNE DANS UN FICHIER CSV
# ligne_data format: ['x1', 'x2', 'x3', ..., 'x11']

def W_line_file_csv(nom_fichier, ligne_data):
    with open(nom_fichier, 'a') as fichier:
        writer = csv.writer(fichier, delimiter=';')
        writer.writerow(ligne_data)
    fichier.close()
    return


# RECUPERATION D'UNE LIGNE D'UN FICHIER CSV CHARGE SIMPLE VERS UN OBJET LOAD

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

# RECUPERATION D'UNE LIGNE D'UN FICHIER CSV CHARGE TOTALE VERS UN OBJET LOADTOT
"""à compléter"""

# RECUPERATION D'UNE LIGNE D'UN FICHIER CSV MPPT DATA VERS UN OBJET MPPTDATA
"""à compléter"""


# AFFICHAGE CONSOLE D'UNE LIGNE DANS UN FICHIER CSV

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


# AFFICHAGE CONSOLE D'UN FICHIER CSV ENTIER

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


## CALCUL DE MOYENNE
"""à completer"""

## CALCUL DE RMS
"""à completer"""

## CALCUL DES VALEURS TOTALES CHARGES
"""à completer"""

## CALCUL DES VALEURS MPPT CHARGES
"""à completer"""


###########################################################################
## TEST LOOPS
###########################################################################

#D_line_file_csv('test1.csv', 2)

#D_file_csv('test.csv')

#Init_file_charge_csv('test1.csv')
#W_line_file_csv('test1.csv',['x1', 'x2'])


#info = G_line_file_csv('test1.csv',1)
#info.Display_everything()
#W_line_file_csv('test1.csv',info.Format_in_line())

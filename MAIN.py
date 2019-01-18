import sys
from PyQt4 import QtCore, QtGui
from Project_GUI_V6 import Ui_Form
from Loads_consumption import Ui_Form1
import subprocess
import csv
from DATA import *
from MONITORING import *
import matplotlib.pyplot as plt
import datetime

data_Ld_1 = data_Ld_2 = data_Ld_3 = data_Ld_4 = data_Ld_5 = [1 , 0]
i = 0
num_ligne = 0
battery_level = 0

#Loads status and consumption window
class Win_LdStatus(QtGui.QWidget,Ui_Form1):
     def __init__(self, parent=None):
        super(Win_LdStatus, self).__init__(parent)

        self.ui=Ui_Form1()
        self.ui.setupUi(self)
        
        self.ui.BackButton.clicked.connect(self.back_To_Main_Window)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateData)
        self.timer.start(1000) # 1s

     def back_To_Main_Window(self):
        self.dialog = Win_Main()
        self.dialog.show()
        self.close()
        self.timer.stop()

     def updateData(self):
        global num_ligne
        global i
        global data_Ld_1,data_Ld_2,data_Ld_3,data_Ld_4,data_Ld_5
        #num_ligne += 1
        i += 1


        #read line number num_ligne

        data_Ld_1 = G_line_file_charge_csv('logs/charge1.csv', num_ligne)
        data_Ld_2 = G_line_file_charge_csv('logs/charge2.csv', num_ligne)
        data_Ld_3 = G_line_file_charge_csv('logs/charge3.csv', num_ligne)
        data_Ld_4 = G_line_file_charge_csv('logs/charge4.csv', num_ligne)
        data_Ld_5 = G_line_file_charge_csv('logs/charge5.csv', num_ligne)

        self.ui.Ld_1_AP.setText(str(data_Ld_1.active_power))
        self.ui.Ld_2_AP.setText(str(data_Ld_2.active_power))
        self.ui.Ld_3_AP.setText(str(data_Ld_3.active_power))
        self.ui.Ld_4_AP.setText(str(data_Ld_4.active_power))
        self.ui.Ld_5_AP.setText(str(data_Ld_5.active_power))

        self.ui.Ld_1_RP.setText(str(data_Ld_1.reactive_power))
        self.ui.Ld_2_RP.setText(str(data_Ld_2.reactive_power))
        self.ui.Ld_3_RP.setText(str(data_Ld_3.reactive_power))
        self.ui.Ld_4_RP.setText(str(data_Ld_4.reactive_power))
        self.ui.Ld_5_RP.setText(str(data_Ld_5.reactive_power))

        self.ui.Ld_1_AppP.setText(str(data_Ld_1.apparent_power))
        self.ui.Ld_2_AppP.setText(str(data_Ld_2.apparent_power))
        self.ui.Ld_3_AppP.setText(str(data_Ld_3.apparent_power))
        self.ui.Ld_4_AppP.setText(str(data_Ld_4.apparent_power))
        self.ui.Ld_5_AppP.setText(str(data_Ld_5.apparent_power))

        self.ui.Ld_1_rmsCurrent.setText(str(data_Ld_1.current))
        self.ui.Ld_2_rmsCurrent.setText(str(data_Ld_2.current))
        self.ui.Ld_3_rmsCurrent.setText(str(data_Ld_3.current))
        self.ui.Ld_4_rmsCurrent.setText(str(data_Ld_4.current))
        self.ui.Ld_5_rmsCurrent.setText(str(data_Ld_5.current))

        self.ui.Ld_1_rmsVoltage.setText(str(data_Ld_1.voltage))
        self.ui.Ld_2_rmsVoltage.setText(str(data_Ld_2.voltage))
        self.ui.Ld_3_rmsVoltage.setText(str(data_Ld_3.voltage))
        self.ui.Ld_4_rmsVoltage.setText(str(data_Ld_4.voltage))
        self.ui.Ld_5_rmsVoltage.setText(str(data_Ld_5.voltage))

        self.ui.Ld_1_PwrFact.setText(str(data_Ld_1.power_factor))
        self.ui.Ld_2_PwrFact.setText(str(data_Ld_2.power_factor))
        self.ui.Ld_3_PwrFact.setText(str(data_Ld_3.power_factor))
        self.ui.Ld_4_PwrFact.setText(str(data_Ld_4.power_factor))
        self.ui.Ld_5_PwrFact.setText(str(data_Ld_5.power_factor))

        self.ui.Ld_1_Freq.setText(str(data_Ld_1.freq))
        self.ui.Ld_2_Freq.setText(str(data_Ld_2.freq))
        self.ui.Ld_3_Freq.setText(str(data_Ld_3.freq))
        self.ui.Ld_4_Freq.setText(str(data_Ld_4.freq))
        self.ui.Ld_5_Freq.setText(str(data_Ld_5.freq))

        self.ui.Ld_1_PwrSrc_4.setText(str(data_Ld_1.type))
        self.ui.Ld_2_PwrSrc_4.setText(str(data_Ld_2.type))
        self.ui.Ld_3_PwrSrc_4.setText(str(data_Ld_3.type))
        self.ui.Ld_4_PwrSrc_4.setText(str(data_Ld_4.type))
        self.ui.Ld_5_PwrSrc_4.setText(str(data_Ld_5.type))

        

     


#main window
class Win_Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Win_Main, self).__init__(parent)

        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer()

        #RUN "start new eval" button
        self.ui.View_Button.clicked.connect(self.View_Loads_Status_Window)

        

        #show plotter when click on today button
        self.ui.Today_Button.clicked.connect(lambda:self.run('Plot_Prod_Graph.py'))

        self.ui.week_Button.clicked.connect(self.plot_week_prod)

        self.ui.Month_Button.clicked.connect(self.plot_month_prod)
        
        
        self.timer.timeout.connect(self.updateData)
        self.timer.start(1000) # 1s
        
        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.Monitor)
        self.timer2.start(5) # 5ms
        
    def Monitor(self):
        global SData, bus, CAN_msg_queue, counter, num_ligne 
        SData, bus, CAN_msg_queue, counter,num_ligne = Monitoring(SData,bus,CAN_msg_queue,counter,num_ligne)


    def updateData(self):
        global num_ligne, data_Battery
        #num_ligne += 1

        data_Battery = G_line_file_battery_csv('logs/battery.csv', num_ligne)
        batt_power_sign = data_Battery.sign
        
          #update battery level
        self.ui.Battery_level.setProperty("value", data_Battery.battery_level)
        
        if int(batt_power_sign) == -1 :
             self.ui.batt_discharg.hide()
             self.ui.batt_charg.show()
        elif int(batt_power_sign) == 1 :
             self.ui.batt_discharg.show()
             self.ui.batt_charg.hide()
        else:
             self.ui.batt_discharg.hide()
             self.ui.batt_charg.hide()


        data_mppt = G_line_file_mppt_csv('logs/mppt.csv', num_ligne)

                  #update MPPT power
        self.ui.Prod_power.setText(str(data_mppt.power))
        self.ui.Prod_current.setText(str("{0:.2f}".format(float(data_mppt.power)/24.0)))

                  #update power source ( EDF / PV )
        data_Ld_1 = G_line_file_charge_csv('logs/charge1.csv', num_ligne)
        data_Ld_2 = G_line_file_charge_csv('logs/charge2.csv', num_ligne)
        data_Ld_3 = G_line_file_charge_csv('logs/charge3.csv', num_ligne)
        data_Ld_4 = G_line_file_charge_csv('logs/charge4.csv', num_ligne)
        data_Ld_5 = G_line_file_charge_csv('logs/charge5.csv', num_ligne)

        self.ui.state_ld_1.setText(str(data_Ld_1.type))
        self.ui.state_ld_2.setText(str(data_Ld_2.type))
        self.ui.state_ld_3.setText(str(data_Ld_3.type))
        self.ui.state_ld_4.setText(str(data_Ld_4.type))
        self.ui.state_ld_5.setText(str(data_Ld_5.type))
        
                  #update total consumption
        data_Ld_tot = G_line_file_chargetot_csv('logs/charge_tot.csv', num_ligne)

        self.ui.Cons_voltage.setText(str(data_Ld_tot.voltage_PV))
        self.ui.Cons_current.setText(str(data_Ld_tot.current_PV))
        self.ui.Cons_power.setText(str(data_Ld_tot.apparent_power_PV))




    def run(self, path):
        subprocess.call([sys.executable,path])

    def View_Loads_Status_Window(self):
        self.dialog = Win_LdStatus()
        self.dialog.show()
        self.close()
        self.timer.stop()

#NOTE: values need to be adjusted later        
    def plot_week_prod(self):
         global num_ligne
         prod = []
         time = []
         data = G_line_file_charge_csv('logs/charge1.csv', num_ligne - 10)
         date_today = data.date
         date_today = date_today.split("/")
         time_now = data.time
         time_now = time_now.split(":")
         start_date = datetime.datetime(int(date_today[2]),int(date_today[1]),int(date_today[0]),int(time_now[0]), int(time_now[1]))
         lines_numbers = G_linenumber('logs/charge1.csv',date_inf,time_inf,date_sup,time_sup)
         
         for i in range( num_ligne - 10 , num_ligne ):
              data_Ld_1 = G_line_file_charge_csv('logs/charge1.csv', i)
              prod.append(data_Ld_1.apparent_power)
              #time.append(data_Ld_1.time)
         time = [start_date + datetime.timedelta(minutes = i) for i in range(len(prod))]
         plt.plot(time, prod)
         plt.gcf().autofmt_xdate()
         plt.show()


    def plot_month_prod(self):
         global num_ligne
         prod = []
         time = []
         for i in range( num_ligne - 10 , num_ligne , 3600 ):
              data_Ld_1 = G_line_file_charge_csv('logs/charge1.csv', i)
              prod.append(data_Ld_1.apparent_power)
              time.append(data_Ld_1.time)
         plt.plot(time, prod)


    def centre(self):
        """
        Center the window on screen. This implemention will handle the window
        being resized or the screen resolution changing.
        """
        # Get the current screens' dimensions...
        screen = QtGui.QDesktopWidget().screenGeometry()
        # ... and get this windows' dimensions
        mysize = self.geometry()
        # The horizontal position is calulated as screenwidth - windowwidth /2
        hpos = ( screen.width() - mysize.width() ) / 2
        # And vertical position the same, but with the height dimensions
        vpos = ( screen.height() - mysize.height() ) / 2
        # And the move call repositions the window
        self.move(hpos, vpos)



def main():
    app = QtGui.QApplication(sys.argv)
    main = Win_Main()
    main.setFixedSize(main.size())
    main.centre()
    main.show()
    sys.exit(app.exec_())

    
if __name__ == '__main__':
    SData,bus,CAN_msg_queue,counter,num_ligne = Init_monitoring()
    main()

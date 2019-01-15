import sys
from PyQt4 import QtCore, QtGui
from Project_GUI_V6 import Ui_Form
from Loads_consumption import Ui_Form1
import subprocess
import csv
from MONITORING import *

data = [1 , 0]
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

     def updateData(self):
        global num_ligne
        global i
        global data
        num_ligne += 1
        i += 1

##        if i == 1:
##            with open(r'C:\Users\Yahya\Desktop\DataFile2.csv', 'w', newline='') as f:
##                fieldnames=['act power','react pow']
##                writer = csv.DictWriter(f, fieldnames = fieldnames, delimiter = ';')
##                writer.writeheader()
##                writer.writerow({'act power' : i,'react pow' : i})
##                f.close()
##        else :
##            with open(r'C:\Users\Yahya\Desktop\DataFile2.csv', 'a', newline='') as f:
##                fieldnames=['act power','react pow']
##                writer = csv.DictWriter(f, fieldnames = fieldnames, delimiter = ';')
##                writer.writerow({'act power' : i,'react pow' : i})
##                f.close()



        #read line number num_ligne

        
        with open('logs/charge1.csv', "r") as fichier:
                reader = csv.reader(fichier)
                rownum = 0
                for row in reader:
                    # save header row
                    if rownum == 0:
                        header = row
                    elif (rownum == num_ligne):
                        colnum = 0
                        for col in row:
                            global data
                            data = col
                            col = col.split(";")
                            #print(int(col[0]) + 5,"\n")
                            colnum += 1
                    rownum += 1
        fichier.close()
        print(data)
        data = data.split(";")
        self.ui.Ld_1_AP.setText(data[1])

        

     


#main window
class Win_Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(Win_Main, self).__init__(parent)

        self.ui=Ui_Form()
        self.ui.setupUi(self)

        #RUN "start new eval" button
        self.ui.View_Button.clicked.connect(self.View_Loads_Status_Window)
        

        #show plotter when click on today button
        self.ui.Today_Button.clicked.connect(lambda:self.run('Plot_Prod_Graph.py'))
        
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateData)
        self.timer.start(1000) # 1s

        self.timer2 = QtCore.QTimer()
        self.timer2.timeout.connect(self.Monitor)
        self.timer2.start(5) # 5ms

    def Monitor(self):
        global SData, bus, CAN_msg_queue, counter, num_ligne 
        SData, bus, CAN_msg_queue, counter,num_ligne = Monitoring(SData,bus,CAN_msg_queue,counter,num_ligne)

    def updateData(self):
        global num_ligne
        global i
        global data
        #num_ligne += 1
        i += 1

        with open('logs/battery.csv', "r") as fichier:
            reader = csv.reader(fichier)
            rownum = 0
            for row in reader:
                # save header row
                if rownum == 0:
                    header = row
                elif (rownum == num_ligne):
                    colnum = 0
                    for col in row:
                        global data
                        data = col
                        col = col.split(";")
                        #print(int(col[0]) + 5,"\n")
                        colnum += 1
                rownum += 1
        fichier.close()
        print(data)
        data = data.split(";")
        
        battery_level = data[2]
        batt_power_sign = data[4]
          #update battery level
        self.ui.Battery_level.setProperty("value", battery_level)
        
        if int(batt_power_sign) == -1 :
             self.ui.batt_discharg.hide()
             self.ui.batt_charg.show()
        elif int(batt_power_sign) == 1 :
             self.ui.batt_discharg.show()
             self.ui.batt_charg.hide()
        else:
             self.ui.batt_discharg.hide()
             self.ui.batt_charg.hide()


    def run(self, path):
        subprocess.call(['pythonw',path])

    def View_Loads_Status_Window(self):
        self.dialog = Win_LdStatus()
        self.dialog.show()
        self.close()


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

from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg

import collections
import random
import time
import math
import numpy as np
import sys
#import pandas as pd
import csv

i = 0


column = []
class DynamicPlotter():

    def __init__(self, sampleinterval=0.1, timewindow=10., size=(600,350)):
        # Data stuff
        self._interval = int(sampleinterval*1000)
        self._bufsize = int(timewindow/sampleinterval)
        self.databuffer = collections.deque([0.0]*self._bufsize, self._bufsize)
        self.x = np.linspace(-timewindow, 0.0, self._bufsize)
        self.y = np.zeros(self._bufsize, dtype=np.float)
        # PyQtGraph stuff
        self.app = QtGui.QApplication([])
        self.plt = pg.plot(title='Real time power')
        self.plt.resize(*size)
        self.plt.showGrid(x=True, y=True)
        self.plt.setLabel('left', 'amplitude', 'V')
        self.plt.setLabel('bottom', 'time', 's')
        self.curve = self.plt.plot(self.x, self.y, pen=(255,0,0))
        # QTimer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateplot)
        self.timer.start(self._interval)


        
        
    def getdata(self):
##        #frequency = 0.5
##        #noise = random.normalvariate(0., 1.)
##        #new = 10.*math.sin(time.time()*frequency*2*math.pi)
##        
##        global i
##        global column
##        i = i + 1
##        f = open(r"myFile.txt", "a+")
##        f.write(str(i) + " , " + str(i) + "\n")
##        f.close()
##        f = open(r"myFile.txt", "r")
##        data = f.readlines()
##        for line in data:
##            column.append(float(line.strip().split(",")[1]))
##        print(column[-1])
##        f.close()
##        return column[-1]


    #########################################
    #GET DATA FROM CSV FILE WITH CSV PACKAGE#
    #########################################

        #read line number num_ligne

        num_ligne = 2
        with open(r'C:\Users\Yahya\Desktop\DataFile2.csv', "r") as fichier:
                reader = csv.reader(fichier)
                rownum = 0
                for row in reader:
                    # save header row
                    if rownum == 0:
                        header = row
                    elif (rownum == num_ligne):
                        colnum = 0
                        for col in row:
                            col = col.split(";")
                            print(int(col[0]) + 5,"\n")
                            colnum += 1
                    rownum += 1
        fichier.close()
        return (col[0])
    ############################################
    #GET DATA FROM CSV FILE WITH PANDAS PACKAGE#
    ############################################
##        data = pd.read_csv (r'C:\Users\Yahya\Desktop\DataFile.csv', sep=';')
##        #print (data)
##        P = data['puissance active'].values
##        return (P[-1])

    def updateplot(self):
        self.databuffer.append( self.getdata() )
        self.y[:] = self.databuffer
        self.curve.setData(self.x, self.y)
        self.app.processEvents()

    def run(self):
        #print ("ncjf")
        self.app.exec_()
        

if __name__ == '__main__':
    m = DynamicPlotter(sampleinterval=0.1, timewindow=10.)
    m.run()
    m.timer.stop()
    sys.exit()

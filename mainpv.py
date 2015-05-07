#This file includes program for Pv chnl 2 and chnl 3 GUI
#Import data read in file 'pvpymodbus.py' and panel6pymodbus.py'
__author__ = 'alvin'
import sys

#import to allow the initialisation to be done in 'init'
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QSlider
import PyQt5.QtCore

#import Qtimer to be used for updating 
from PyQt5.QtCore import QTimer

#import the class 'Ui_pvUI' from 'pvUI.py'
from pvcontrolUI import Ui_pvControl

#import the class 'pv' from 'pvpymodbus.py'
from pvpymodbus import pv

#import the class 'panel6' from 'panel6pymodbus.py'
#from panel6pymodbus import panel6

#Set up client
from pymodbus3.client.sync import ModbusTcpClient
client = ModbusTcpClient('192.168.0.10')

class Mainpv(QWidget, Ui_pvControl):
    def update_pv_array(self):
        pv.pv2_array(self)
        pv.pv3_array(self)
        panel6.p6_dc1_real_array(self)
        panel6.p6_dc2_real_array(self)
           
    def update_pv_gui(self):
        #Update Chnl 2 Operating State
        if self.MPPT_2_Coil_15 == 1:   #check MPPT_2_Coil_15 - MPPT_2_MPPT
            self.mppt_chnl2_operating_state.setText("MPPT") 
        elif self.MPPT_2_Coil_16 == 1:   #check MPPT_2_Coil_16 - MPPT_2_MB
            self.mppt_chnl2_operating_state.setText("Monitor Bus") 
        else:
             self.mppt_chnl2_operating_state.setText("-") 
        #Update Chnl 2 On/Off                
        if self.MPPT_2_Coil_11 == 0:    #MPPT_2_Coil_11 - MPPT_2_ON_OFF
            self.mppt_chnl2_on_off_indicator.setText('OFF')
            self.mppt_chnl2_on_off_indicator.setStyleSheet("background-color: rgb(255, 0, 0);") #set indicator to red colour
        if self.MPPT_2_Coil_11 == 1:
            self.mppt_chnl2_on_off_indicator.setText('ON')
            self.mppt_chnl2_on_off_indicator.setStyleSheet("background-color: rgb(0, 255, 0);") #set indicator to green colour
                 
        #Update Chnl 3 Operating State
        if self.MPPT_3_Coil_15 == 1:   #check MPPT_3_Coil_15 - MPPT_3_MPPT
            self.mppt_chnl3_operating_state.setText("MPPT")               
        elif self.MPPT_3_Coil_16 == 1:   #check MPPT_3_Coil_16 - MPPT_3_MB
            self.mppt_chnl3_operating_state.setText("Monitor Bus") 
        else:
             self.mppt_chnl3_operating_state.setText("-")      
        #Update Chnl 3 On/Off                
        if self.MPPT_3_Coil_11 == 0:    #MPPT_3_Coil_11 - MPPT_2_ON_OFF
            self.mppt_chnl3_on_off_indicator.setText('OFF')
            self.mppt_chnl3_on_off_indicator.setStyleSheet("background-color: rgb(255, 0, 0);") #set indicator to red colour
        if self.MPPT_3_Coil_11 == 1:
            self.mppt_chnl3_on_off_indicator.setText('ON')
            self.mppt_chnl3_on_off_indicator.setStyleSheet("background-color: rgb(0, 255, 0);") #set indicator to green colour
 #     ------------------------------------------------------------     #            
    #Pushbutton Functionality         
    def mppt_chnl2_on_off_clicked(self):
        #print(self.MPPT_2_Coil_11)
        
        if self.MPPT_2_Coil_11 == 1: # check for MPPT_2_ON_OFF
            client.write_register(921, 0) # write MPPT_2_CoilSet_Word_0=0
        else:
            client.write_registers(921, 1) #write MPPT_2_CoilSet_Word_0=1
        client.write_register(922, 1) #write MPPT_2_ Write_Indicator_1=1
        
    def mppt_chnl3_on_off_clicked(self):
        #print(self.MPPT_3_Coil_11)   
        
        if self.MPPT_3_Coil_11 == 1:   #check MPPT_3_Coil_11 = MPPT_3_ON_OFF
            client.write_register(941, 0) #write MPPT_3_CoilSet_Word_0=0
        else:
            client.write_registers(941, 1) #write MPPT_3_CoilSet_Word_0=1
        client.write_register(942, 1) #write MPPT_3_ Write_Indicator_1=1


 #     ------------------------------------------------------------     #     
         
    def __init__(self): #initialisation, passing parameter during the intial state
       
        QWidget.__init__(self)
        # set up User Interface (widgets, layout...)
        self.setupUi(self)         
        
        #Event handlers for MPPT Chnl 2
        self.mppt_chnl2_on_off.clicked.connect(self.mppt_chnl2_on_off_clicked)  # Bind the event handlers to button       
                
        #Event handlers for MPPT Chnl 3
        self.mppt_chnl3_on_off.clicked.connect(self.mppt_chnl3_on_off_clicked)  # Bind the event handlers to button                      
                
        #Timer for updating gui data
        timer = QTimer(self)
        timer.timeout.connect(self.update_pv_array)
        timer.timeout.connect(self.update_pv_gui)
        timer.start(200) 
                                 
    

def main():
    # create Qt application
    app = QApplication(sys.argv)
    
    # create main window
    wndpv = Mainpv()  # classname
    wndpv.show()
   
    # Start the app up
    sys.exit(app.exec_())
   

if __name__ == "__main__":
    main()    
    

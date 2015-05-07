#This file includes program for Lithium Ion Battery GUI
#Import data read in file 'battpymodbus.py' and panel5pymodbus.py'
__author__ = 'alvin'
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QSlider
import PyQt5.QtCore

from PyQt5.QtCore import QTimer

import time
import math

#Import the class for battery 1 GUI
from battery1controlUI import Ui_battery1Control

#Import the class 'battery' from 'battpymodbus.py'
from battpymodbus import battery

#Import the class 'panel5' from 'panel5pymodbus.py'
from panel5pymodbus import panel5

#Create a Modbus TCP/IP Client
from pymodbus3.client.sync import ModbusTcpClient
client = ModbusTcpClient('192.168.0.10')

class Mainbattery1(QWidget, Ui_battery1Control):    
    #Updating of Battery Array data
    def update_batt1_array(self):
        battery.battery1_inarray(self)
        panel5.p5_dc1_real_array(self)      
        
    #Updating of battery GUI data, only include data to be shown on GUI       
    def update_batt1_gui(self):          
        #Update GUI ref current
        self.batt1_ref_current.setText(""+str(self.Bat_1_Ref_Current_Read_SIGNED))   
        
        #Update GUI ref voltage
        self.batt1_ref_voltage.setText(""+str(self.Bat_1_Bus_Voltage_Read_SIGNED))   
        
        #Update Operating State                       
        if self.Bat_1_Coil_15 == 1:    #Check Bat_1_Coil_15 - Bat_1_Stg_MB
            self.batt1_operating_state.setText("Monitor Bus") 
        else:
            self.batt1_operating_state.setText("-") 
        if self.Bat_1_Coil_19 == 1:    #Check Bat_1_Coil_19 - Bat_1_Stg_CC
            self.batt1_operating_state.setText("Constant Current") 
        else:
            self.batt1_operating_state.setText("-")  
             
        #Update Control Mode
        if self.Bat_1_Coil_12 == 1:    #Check Bat_1_Coil_12 - Bat_1_MD_MB
            self.batt1_control_mode.setText("Monitor Bus")                     
        elif self.Bat_1_Coil_14 == 1:    #Check Bat_1_Coil_14 - Bat_1_MD_CC
            self.batt1_control_mode.setText("Constant Current") 
        else:
            self.batt1_control_mode.setText("-")  
          
        #Update on/off indicator      
        if self.Bat_1_Coil_11 == 0:    #Check Bat_1_Coil_11 - Bat_1_ON_OFF
            self.batt1_on_off_indicator.setText('OFF')
            self.batt1_on_off_indicator.setStyleSheet("background-color: rgb(255, 0, 0);") #set indicator to red colour
        if self.Bat_1_Coil_11 == 1:
            self.batt1_on_off_indicator.setText('ON')
            self.batt1_on_off_indicator.setStyleSheet("background-color: rgb(0, 255, 0);") #set indicator to green colour
            
    #Pushbutton          
    def batt1_on_off_pb_clicked(self):            
        #print(self.Bat_1_Coil_11)
        
        if self.Bat_1_Coil_11 == 1:        #check Bat_1_ON_OFF
            client.write_register(961, 0)  #write Bat_1_CoilsSet_Word_0=0
        else:
            client.write_registers(961, 1) #write Bat_1_CoilsSet_Word_0=1
        client.write_register(975, 1)      #write Bat_1_Write_Indicator_1=1              

    def batt1_switch_control_mode_pb_clicked(self):
        #print(self.Bat_1_Coil_1)
        
        if self.Bat_1_Coil_1 == 1:         #check for Bat_1_Coil_1 - Bat_1_MD
            client.write_register(962, 0)  #write Bat_1_CoilsSet_Word_1=0
        else:
            client.write_registers(962, 1) #write Bat_1_CoilsSet_Word_0=1
        client.write_register(977, 1)      #write Bat_1_Write_Indicator_3=1
                              
    def batt1_apply_current_pb_clicked(self):
         #Write value of Set Current to Bat_1_Ref_Current_Write_Unit
        Bat_1_Ref_Current_Write_Unit = self.batt1_set_ref_current.text()
        client.write_register(970, int(Bat_1_Ref_Current_Write_Unit))  #Write to reg 970 - Bat_1_Ref_Current_Write_Unit              
        client.write_register(976, 1) #write Bat_1_Write_Indicator_2=1         
        #print(self.batt1_set_ref_current.text())
        
    def batt1_apply_voltage_pb_clicked(self):
        #Write value of Set Voltage to Bat_1_Ref_Current_Write_Unit
        Bat_1_Ref_Voltage_Write_Unit = int(self.batt1_set_ref_voltage.text()) * 100
        client.write_register(966, int(Bat_1_Ref_Voltage_Write_Unit))  #Write to reg 966 - Bat_1_Ref_Voltage_Write_Unit              
        client.write_register(960, 1)                                  #write Bat_1_Write_Indicator_0=1         
        #print(self.batt1_set_ref_voltage.text())
    

    def __init__(self): #initialisation, passing parameter during the intial state       
        QWidget.__init__(self)
        # set up User Interface (widgets, layout...)
        self.setupUi(self)         
        
        #Event handlers for Battery1
        #Bind the event handlers to button  
        self.batt1_on_off_pb.clicked.connect(self.batt1_on_off_pb_clicked)       
        self.batt1_switch_control_mode_pb.clicked.connect(self.batt1_switch_control_mode_pb_clicked)      
        self.batt1_apply_current_pb.clicked.connect(self.batt1_apply_current_pb_clicked)
        self.batt1_apply_voltage_pb.clicked.connect(self.batt1_apply_voltage_pb_clicked)
        
        #Timer for updating data
        timer = QTimer(self)
        timer.timeout.connect(self.update_batt1_array) 
        timer.timeout.connect(self.update_batt1_gui)   
        timer.start(200) 
 
    

def main():
    # create Qt application
    app = QApplication(sys.argv)
    
    # create main window
    wndbattery1 = Mainbattery1()  # classname
    wndbattery1.show() 
  
    # Start the app up
    sys.exit(app.exec_())       

if __name__ == "__main__":
    main()    
    



'''
Default program
def main(argv):
    # create Qt application
    app = QApplication(argv)
    
    # create main window
    wnd = Batt()  # classname
    wnd.show()
    
    # Connect signal for app finish
    #app.connect(app, QtCore.SIGNAL("lastWindowClosed()"), app, QtCore.SLOT("quit()"))
    
    # Start the app up
    sys.exit(app.exec_())

    
    #Main program   
    
    #self.lead_batt_operating_state.setText('Monitor Bus') #set operating mode to 'Monitor Bus' when system achieve the mode
    

if __name__ == "__main__":
    main(sys.argv)
    print (sys.argv)     
'''     
      
    
   
    
   


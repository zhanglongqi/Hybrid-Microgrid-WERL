# This file includes program for Main Hybrid Grid GUI.
__author__ = 'alvin'
import sys

# Import to for initialisation
from PyQt5 import QtCore, QtGui, QtWidgets

# Import pyqtSlot to enable access to Signals and Slot
from PyQt5.QtCore import pyqtSlot

#Import QApplication, QWidget
import PyQt5.QtWidgets

#Import Qtimer to be used for updating 
from PyQt5.QtCore import QTimer

#Set up Modbus Client
from pymodbus3.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.0.10')

#Import the class 'Ui_hybridgrid' from 'hybridgridui.py'
from hybridgridUI import Ui_hybridgridUI
#from beaglebonehybridgridUI import Ui_beaglebonehybridgridUI
#Import the class 'panel8' from 'panel8pymodbus.py'
from panel8pymodbus import panel8

#Import the class 'panel7' from 'panel7pymodbus.py'
from panel7pymodbus import panel7

#Import the class 'Mainpv' from 'Mainpv.py'
from mainpv import Mainpv
#Import the class 'pv' from 'pvpymodbus.py'
from pvpymodbus import pv
#Import the class 'panel6' from 'panel6pymodbus.py'
from panel6pymodbus import panel6

#import the class 'Mainbattery1' from 'mainbattery1.py'
from mainbattery1 import Mainbattery1
#import the class 'battery' from 'battpymodbus.py'
from battpymodbus import battery
#Import the class 'panel5' from 'panel5pymodbus.py'
from panel5pymodbus import panel5

#Import the class 'panel4' from 'panel4pymodbus.py'
from panel4pymodbus import panel4

#Import the class 'Mainbidir' from 'mainbidirpymodbus.py'
from mainbidir import Mainbidir
#import the class 'bidir' from 'bidirpymodbus.py'
from bidirpymodbus import bidir
#Import the class 'panel3' from 'panel3pymodbus.py'
from panel3pymodbus import panel3


class Hybridgrid(PyQt5.QtWidgets.QWidget, Ui_hybridgridUI):
    #---Updating of Array Data-----------------------------------------------------#
    def update_array(self):
        #Updating of Panel 8 data
        panel8.p8_ac1_real_array(self)
        panel8.p8_ac2_real_array(self)
        panel8.p8_dc1_real_array(self)
        panel8.p8_dc2_real_array(self)
        panel8.p8_switches_status(self)

        #Updating of Panel 7 data
        panel7.p7_ac1_real_array(self)
        panel7.p7_ac2_real_array(self)
        panel7.p7_dc1_real_array(self)
        panel7.p7_dc2_real_array(self)
        panel7.p7_switches_status(self)

        #Updating of Panel 6 data and PV data
        pv.pv2_array(self)
        pv.pv3_array(self)
        panel6.p6_ac1_real_array(self)
        panel6.p6_ac2_real_array(self)
        panel6.p6_dc1_real_array(self)
        panel6.p6_dc2_real_array(self)
        panel6.p6_switches_status(self)

        #Updating of Panel 5 data and Battery data
        battery.battery1_inarray(self)
        panel5.p5_ac1_real_array(self)
        panel5.p5_ac2_real_array(self)
        panel5.p5_dc1_real_array(self)
        panel5.p5_dc2_real_array(self)
        panel5.p5_switches_status(self)

        #Updating of Panel 4 data
        panel4.p4_ac1_real_array(self)
        panel4.p4_ac2_real_array(self)
        panel4.p4_dc1_real_array(self)
        panel4.p4_dc2_real_array(self)
        panel4.p4_switches_status(self)

        #Updating of Panel 3 data and BiDirectional Converter data
        bidir.bidir_array(self)
        panel3.p3_ac1_real_array(self)
        panel3.p3_ac2_real_array(self)
        panel3.p3_dc1_real_array(self)
        panel3.p3_dc2_real_array(self)
        panel3.p3_switches_status(self)

    #---Updating of main hybridgrid data, to be display on GUI---------------------#
    def update_hybridgrid_gui(self):
        #Update Panel 8 - DC Source power, current,voltage  
        self.p8dc1_power.setText("" + str(self.p8dc1list_power))
        self.p8dc1_current.setText("" + str(self.p8dc1list_current))
        self.p8dc1_voltage.setText("" + str(self.p8dc1list_voltage))
        #AC Programmable Source
        self.p8ac1_power.setText("" + str(self.p8ac1_TotalRealPower))
        self.p8ac1_current.setText("" + str(self.p8ac1_Current))
        self.p8ac1_voltage.setText("" + str(self.p8ac1_LN_Voltage))

        #Update Panel 7 - power, current,voltage 
        #AC 3.3kW load
        self.p7ac1_power.setText("" + str(self.p7ac1_TotalRealPower))
        self.p7ac1_current.setText("" + str(self.p7ac1_Current))
        self.p7ac1_voltage.setText("" + str(self.p7ac1_LN_Voltage))

        #Update Panel 6 - PV power, current,voltage  
        self.p6dc1_power.setText("" + str(self.p6dc1list_power))
        self.p6dc1_current.setText("" + str(self.p6dc1list_current))
        self.p6dc1_voltage.setText("" + str(self.p6dc1list_voltage))

        #Update Panel 5 - power, current,voltage  
        #Battery1
        self.batt1_soc.setProperty("value", +int(self.lithium_batt_soc))
        self.p5dc1_power.setText("" + str(self.p5dc1list_power))
        self.p5dc1_current.setText("" + str(self.p5dc1list_current))
        self.p5dc1_voltage.setText("" + str(self.p5dc1list_voltage))
        #Programmable Load
        self.p5ac1_power.setText("" + str(self.p5ac1_TotalRealPower))
        self.p5ac1_current.setText("" + str(self.p5ac1_Current))
        self.p5ac1_voltage.setText("" + str(self.p5ac1_LN_Voltage))

        #Update Panel 4 - power, current,voltage  
        #DC 3.3kW Load
        self.p4dc1_power.setText("" + str(self.p4dc1list_power))
        self.p4dc1_current.setText("" + str(self.p4dc1list_current))
        self.p4dc1_voltage.setText("" + str(self.p4dc1list_voltage))
        #WTG Simulator
        self.p4ac1_power.setText("" + str(self.p4ac1_TotalRealPower))
        self.p4ac1_current.setText("" + str(self.p4ac1_Current))
        self.p4ac1_voltage.setText("" + str(self.p4ac1_LN_Voltage))

        #Update Panel 3 
        #Bidir DC
        self.p3dc2_power.setText("" + str(self.p3dc2list_power))
        self.p3dc2_current.setText("" + str(self.p3dc2list_current))
        self.p3dc2_voltage.setText("" + str(self.p3dc2list_voltage))
        #Bidir AC
        self.p3ac2_power.setText("" + str(self.p3ac2_TotalRealPower))
        self.p3ac2_current.setText("" + str(self.p3ac2_Current))
        self.p3ac2_voltage.setText("" + str(self.p3ac2_LN_Voltage))
        #Utility Grid
        self.p3ac1_power.setText("" + str(self.p3ac1_TotalRealPower))
        self.p3ac1_current.setText("" + str(self.p3ac1_Current))
        self.p3ac1_voltage.setText("" + str(self.p3ac1_LN_Voltage))

        #Update Bus Voltages   
        self.dc_bus_voltage.setText("" + str(self.p4dc1list_voltage))
        self.ac_bus_voltage.setText("" + str(self.p4ac2_LL_Voltage))

        #Update Bidir Status     
        self.bidir_ac_frequency.setText("" + str(self.BiDirCon_Freq))
        self.bidir_ac_real_power.setText("" + str(self.BiDirCon_RealPower))
        self.bidir_ac_reactive_power.setText("" + str(self.BiDirCon_ReactPower))

        #Update Battery 1 Status
        #Update Operating State
        if self.Bat_1_Coil_15 == 1:  #Check Bat_1_Coil_15 - Bat_1_Stg_MB
            self.batt1_operating_state.setText("MB")
        else:
            self.batt1_operating_state.setText("-")
        if self.Bat_1_Coil_19 == 1:  #Check Bat_1_Coil_19 - Bat_1_Stg_CC
            self.batt1_operating_state.setText("CC")
        else:
            self.batt1_operating_state.setText("-")
            #Update On/Off indicator      
        if self.Bat_1_Coil_11 == 0:  #Check Bat_1_Coil_11 - Bat_1_ON_OFF
            self.batt1_on_off_indicator.setText('OFF')
            self.batt1_on_off_indicator.setStyleSheet("background-color: rgb(255, 0, 0);")  #set indicator to red colour
        if self.Bat_1_Coil_11 == 1:
            self.batt1_on_off_indicator.setText('ON')
            self.batt1_on_off_indicator.setStyleSheet(
                "background-color: rgb(0, 255, 0);")  #set indicator to green colour

            #Update PV Status
            #Update Chnl 2 Operating State
        if self.MPPT_2_Coil_15 == 1:  #check MPPT_2_Coil_15 - MPPT_2_MPPT
            self.mppt_chnl2_operating_state.setText("MPPT")
        elif self.MPPT_2_Coil_16 == 1:  #check MPPT_2_Coil_16 - MPPT_2_MB
            self.mppt_chnl2_operating_state.setText("MB")
        else:
            self.mppt_chnl2_operating_state.setText("-")
            #Update Chnl 2 On/Off                
        if self.MPPT_2_Coil_11 == 0:  #MPPT_2_Coil_11 - MPPT_2_ON_OFF
            self.mppt_chnl2_on_off_indicator.setText('OFF')
            self.mppt_chnl2_on_off_indicator.setStyleSheet(
                "background-color: rgb(255, 0, 0);")  #set indicator to red colour
        if self.MPPT_2_Coil_11 == 1:
            self.mppt_chnl2_on_off_indicator.setText('ON')
            self.mppt_chnl2_on_off_indicator.setStyleSheet(
                "background-color: rgb(0, 255, 0);")  #set indicator to green colour
            #Update Chnl 3 Operating State
        if self.MPPT_3_Coil_15 == 1:  #check MPPT_3_Coil_15 - MPPT_3_MPPT
            self.mppt_chnl3_operating_state.setText("MPPT")
        elif self.MPPT_3_Coil_16 == 1:  #check MPPT_3_Coil_16 - MPPT_3_MB
            self.mppt_chnl3_operating_state.setText("MB")
        else:
            self.mppt_chnl3_operating_state.setText("-")
            # Update Chnl 3 On/Off
        if self.MPPT_3_Coil_11 == 0:  #MPPT_3_Coil_11 - MPPT_2_ON_OFF
            self.mppt_chnl3_on_off_indicator.setText('OFF')
            self.mppt_chnl3_on_off_indicator.setStyleSheet(
                "background-color: rgb(255, 0, 0);")  #set indicator to red colour
        if self.MPPT_3_Coil_11 == 1:
            self.mppt_chnl3_on_off_indicator.setText('ON')
            self.mppt_chnl3_on_off_indicator.setStyleSheet(
                "background-color: rgb(0, 255, 0);")  #set indicator to green colour

            #Update Switches
            #Panel 3 DC switches
        if self.p3_dc1_status == 1:
            self.switch_p3dc1.setIcon(QtGui.QIcon("images/dc on up.jpg"))
        elif self.p3_dc1_status == 0:
            self.switch_p3dc1.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        if self.p3_dc_status == 1:
            self.switch_p3dc.setIcon(QtGui.QIcon("images/dc on.jpg"))
        elif self.p3_dc_status == 0:
            self.switch_p3dc.setIcon(QtGui.QIcon("images/dc off.jpg"))
        if self.p3_dc2_status == 1:
            self.switch_p3dc2.setIcon(QtGui.QIcon("images/dc on up.jpg"))
        elif self.p3_dc2_status == 0:
            self.switch_p3dc2.setIcon(QtGui.QIcon("images/dc off up.jpg"))
            #Panel 3 AC switches
        if self.p3_ac1_status == 1:
            self.switch_p3ac1.setIcon(QtGui.QIcon("images/ac on up.jpg"))
        elif self.p3_ac1_status == 0:
            self.switch_p3ac1.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        if self.p3_ac_status == 1:
            self.switch_p3ac.setIcon(QtGui.QIcon("images/ac on.jpg"))
        elif self.p3_ac_status == 0:
            self.switch_p3ac.setIcon(QtGui.QIcon("images/ac off.jpg"))
        if self.p3_ac2_status == 1:
            self.switch_p3ac2.setIcon(QtGui.QIcon("images/ac on up.jpg"))
        elif self.p3_ac2_status == 0:
            self.switch_p3ac2.setIcon(QtGui.QIcon("images/ac off up.jpg"))

            #Panel 4 DC switches
        if self.p4_dc1_status == 1:
            self.switch_p4dc1.setIcon(QtGui.QIcon("images/dc on up.jpg"))
        elif self.p4_dc1_status == 0:
            self.switch_p4dc1.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        if self.p4_dc_status == 1:
            self.switch_p4dc.setIcon(QtGui.QIcon("images/dc on.jpg"))
        elif self.p4_dc_status == 0:
            self.switch_p4dc.setIcon(QtGui.QIcon("images/dc off.jpg"))
        if self.p4_dc2_status == 1:
            self.switch_p4dc2.setIcon(QtGui.QIcon("images/dc on up.jpg"))
        elif self.p4_dc2_status == 0:
            self.switch_p4dc2.setIcon(QtGui.QIcon("images/dc off up.jpg"))
            #Panel 4 AC switches
        if self.p4_ac1_status == 1:
            self.switch_p4ac1.setIcon(QtGui.QIcon("images/ac on up.jpg"))
        elif self.p4_ac1_status == 0:
            self.switch_p4ac1.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        if self.p4_ac_status == 1:
            self.switch_p4ac.setIcon(QtGui.QIcon("images/ac on.jpg"))
        elif self.p4_ac_status == 0:
            self.switch_p4ac.setIcon(QtGui.QIcon("images/ac off.jpg"))
        if self.p4_ac2_status == 1:
            self.switch_p4ac2.setIcon(QtGui.QIcon("images/ac on up.jpg"))
        elif self.p4_ac2_status == 0:
            self.switch_p4ac2.setIcon(QtGui.QIcon("images/ac off up.jpg"))

            #Panel 5 DC switches
        if self.p5_dc1_status == 1:
            self.switch_p5dc1.setIcon(QtGui.QIcon("images/dc on up.jpg"))
        elif self.p5_dc1_status == 0:
            self.switch_p5dc1.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        if self.p5_dc_status == 1:
            self.switch_p5dc.setIcon(QtGui.QIcon("images/dc on.jpg"))
        elif self.p5_dc_status == 0:
            self.switch_p5dc.setIcon(QtGui.QIcon("images/dc off.jpg"))
        if self.p5_dc2_status == 1:
            self.switch_p5dc2.setIcon(QtGui.QIcon("images/dc on up.jpg"))
        elif self.p5_dc2_status == 0:
            self.switch_p5dc2.setIcon(QtGui.QIcon("images/dc off up.jpg"))
            #Panel 5 AC switches
        if self.p5_ac1_status == 1:
            self.switch_p5ac1.setIcon(QtGui.QIcon("images/ac on up.jpg"))
        elif self.p5_ac1_status == 0:
            self.switch_p5ac1.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        if self.p5_ac_status == 1:
            self.switch_p5ac.setIcon(QtGui.QIcon("images/ac on.jpg"))
        elif self.p5_ac_status == 0:
            self.switch_p5ac.setIcon(QtGui.QIcon("images/ac off.jpg"))
        if self.p5_ac2_status == 1:
            self.switch_p5ac2.setIcon(QtGui.QIcon("images/ac on up.jpg"))
        elif self.p5_ac2_status == 0:
            self.switch_p5ac2.setIcon(QtGui.QIcon("images/ac off up.jpg"))

            #Panel 6 DC switches
        if self.p6_dc1_status == 1:
            self.switch_p6dc1.setIcon(QtGui.QIcon("images/dc on up.jpg"))
        elif self.p6_dc1_status == 0:
            self.switch_p6dc1.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        if self.p6_dc_status == 1:
            self.switch_p6dc.setIcon(QtGui.QIcon("images/dc on.jpg"))
        elif self.p6_dc_status == 0:
            self.switch_p6dc.setIcon(QtGui.QIcon("images/dc off.jpg"))
        if self.p6_dc2_status == 1:
            self.switch_p6dc2.setIcon(QtGui.QIcon("images/dc on up.jpg"))
        elif self.p6_dc2_status == 0:
            self.switch_p6dc2.setIcon(QtGui.QIcon("images/dc off up.jpg"))
            #Panel 6 AC switches
        if self.p6_ac1_status == 1:
            self.switch_p6ac1.setIcon(QtGui.QIcon("images/ac on up.jpg"))
        elif self.p6_ac1_status == 0:
            self.switch_p6ac1.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        if self.p6_ac_status == 1:
            self.switch_p6ac.setIcon(QtGui.QIcon("images/ac on.jpg"))
        elif self.p6_ac_status == 0:
            self.switch_p6ac.setIcon(QtGui.QIcon("images/ac off.jpg"))
        if self.p6_ac2_status == 1:
            self.switch_p6ac2.setIcon(QtGui.QIcon("images/ac on up.jpg"))
        elif self.p6_ac2_status == 0:
            self.switch_p6ac2.setIcon(QtGui.QIcon("images/ac off up.jpg"))

            #Panel 7 DC switches
        if self.p7_dc1_status == 1:
            self.switch_p7dc1.setIcon(QtGui.QIcon("images/dc on up.jpg"))
        elif self.p7_dc1_status == 0:
            self.switch_p7dc1.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        if self.p7_dc_status == 1:
            self.switch_p7dc.setIcon(QtGui.QIcon("images/dc on.jpg"))
        elif self.p7_dc_status == 0:
            self.switch_p7dc.setIcon(QtGui.QIcon("images/dc off.jpg"))
        if self.p7_dc2_status == 1:
            self.switch_p7dc2.setIcon(QtGui.QIcon("images/dc on up.jpg"))
        elif self.p7_dc2_status == 0:
            self.switch_p7dc2.setIcon(QtGui.QIcon("images/dc off up.jpg"))
            #Panel 7 AC switches
        if self.p7_ac1_status == 1:
            self.switch_p7ac1.setIcon(QtGui.QIcon("images/ac on up.jpg"))
        elif self.p7_ac1_status == 0:
            self.switch_p7ac1.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        if self.p7_ac_status == 1:
            self.switch_p7ac.setIcon(QtGui.QIcon("images/ac on.jpg"))
        elif self.p7_ac_status == 0:
            self.switch_p7ac.setIcon(QtGui.QIcon("images/ac off.jpg"))
        if self.p7_ac2_status == 1:
            self.switch_p7ac2.setIcon(QtGui.QIcon("images/ac on up.jpg"))
        elif self.p7_ac2_status == 0:
            self.switch_p7ac2.setIcon(QtGui.QIcon("images/ac off up.jpg"))

            #Panel 8 DC switches
        if self.p8_dc1_status == 1:
            self.switch_p8dc1.setIcon(QtGui.QIcon("images/dc on up.jpg"))
        elif self.p8_dc1_status == 0:
            self.switch_p8dc1.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        if self.p8_dc_status == 1:
            self.switch_p8dc.setIcon(QtGui.QIcon("images/dc on.jpg"))
        elif self.p8_dc_status == 0:
            self.switch_p8dc.setIcon(QtGui.QIcon("images/dc off.jpg"))
        if self.p8_dc2_status == 1:
            self.switch_p8dc2.setIcon(QtGui.QIcon("images/dc on up.jpg"))
        elif self.p8_dc2_status == 0:
            self.switch_p8dc2.setIcon(QtGui.QIcon("images/dc off up.jpg"))
            #Panel 8 AC switches
        if self.p8_ac1_status == 1:
            self.switch_p8ac1.setIcon(QtGui.QIcon("images/ac on up.jpg"))
        elif self.p8_ac1_status == 0:
            self.switch_p8ac1.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        if self.p8_ac_status == 1:
            self.switch_p8ac.setIcon(QtGui.QIcon("images/ac on.jpg"))
        elif self.p8_ac_status == 0:
            self.switch_p8ac.setIcon(QtGui.QIcon("images/ac off.jpg"))
        if self.p8_ac2_status == 1:
            self.switch_p8ac2.setIcon(QtGui.QIcon("images/ac on up.jpg"))
        elif self.p8_ac2_status == 0:
            self.switch_p8ac2.setIcon(QtGui.QIcon("images/ac off up.jpg"))

        #-------Update Line------------------------------------------------------------#
        #Supplied by p3dc1
        self.p3dc1_on_line_dc_3to4 = 0
        if (self.p3dc1list_voltage >= 40 and self.p3_dc1_status == 1):
            self.p3dc1_on_line_dc_3to4 = 1

            #Supplied by p3dc2
        self.p3dc2_on_line_dc_8to3 = 0
        if (self.p3dc2list_voltage >= 40 and self.p3_dc2_status == 1):
            self.p3dc2_on_line_dc_8to3 = 1

            #Supplied by p4dc1
        self.p4dc1_on_line_dc_4to5 = 0
        if (self.p4dc1list_voltage >= 40 and self.p4_dc1_status == 1):
            self.p4dc1_on_line_dc_4to5 = 1

            #Supplied by p4dc2
        self.p4dc2_on_line_dc_3to4 = 0
        if (self.p4dc2list_voltage >= 40 and self.p4_dc2_status == 1):
            self.p4dc2_on_line_dc_3to4 = 1

            #Supplied by p5dc1
        self.p5dc1_on_line_dc_5to6 = 0

        self.p5dc1cw_on_line_dc_3to4 = 0
        self.p5dc1cw_on_line_dc_4to5 = 0
        self.p5dc1cw_on_line_dc_6to7 = 0
        self.p5dc1cw_on_line_dc_7to8 = 0
        self.p5dc1cw_on_line_dc_8to3 = 0

        self.p5dc1ccw_on_line_dc_3to4 = 0
        self.p5dc1ccw_on_line_dc_4to5 = 0
        self.p5dc1ccw_on_line_dc_6to7 = 0
        self.p5dc1ccw_on_line_dc_7to8 = 0
        self.p5dc1ccw_on_line_dc_8to3 = 0
        #Check clockwise 
        if (self.p5dc1list_voltage >= 40 and self.p5_dc1_status == 1):
            self.p5dc1_on_line_dc_5to6 = 1
            if self.p6_dc_status == 1:
                self.p5dc1cw_on_line_dc_6to7 = 1
                if self.p7_dc_status == 1:
                    self.p5dc1cw_on_line_dc_7to8 = 1
                    if self.p8_dc_status == 1:
                        self.p5dc1cw_on_line_dc_8to3 = 1
                        if self.p3_dc_status == 1:
                            self.p5dc1cw_on_line_dc_3to4 = 1
                            if self.p4_dc_status == 1:
                                self.p5dc1cw_on_line_dc_4to5 = 1

                                #Check counterclockwise
        if (self.p5dc1list_voltage >= 40 and self.p5_dc1_status == 1 and self.p5_dc_status == 1):
            self.p5dc1ccw_on_line_dc_4to5 = 1
            if self.p4_dc_status == 1:
                self.p5dc1ccw_on_line_dc_3to4 = 1
                if self.p3_dc_status == 1:
                    self.p5dc1ccw_on_line_dc_8to3 = 1
                    if self.p8_dc_status == 1:
                        self.p5dc1ccw_on_line_dc_7to8 = 1
                        if self.p7_dc_status == 1:
                            self.p5dc1ccw_on_line_dc_6to7 = 1


                            #Supplied by p5dc2
        self.p5dc2_on_line_dc_4to5 = 0
        if (self.p5dc2list_voltage >= 40 and self.p5_dc2_status == 1):
            self.p5dc2_on_line_dc_4to5 = 1

            #Supplied by p6dc1
        self.p6dc1_on_line_dc_6to7 = 0

        self.p6dc1cw_on_line_dc_3to4 = 0
        self.p6dc1cw_on_line_dc_4to5 = 0
        self.p6dc1cw_on_line_dc_5to6 = 0
        self.p6dc1cw_on_line_dc_7to8 = 0
        self.p6dc1cw_on_line_dc_8to3 = 0

        self.p6dc1ccw_on_line_dc_3to4 = 0
        self.p6dc1ccw_on_line_dc_4to5 = 0
        self.p6dc1ccw_on_line_dc_5to6 = 0
        self.p6dc1ccw_on_line_dc_7to8 = 0
        self.p6dc1ccw_on_line_dc_8to3 = 0

        #Check clockwise 
        if (self.p6dc1list_voltage >= 40 and self.p6_dc1_status == 1):
            self.p6dc1_on_line_dc_6to7 = 1
            if self.p7_dc_status == 1:
                self.p6dc1cw_on_line_dc_7to8 = 1
                if self.p8_dc_status == 1:
                    self.p6dc1cw_on_line_dc_8to3 = 1
                    if self.p3_dc_status == 1:
                        self.p6dc1cw_on_line_dc_3to4 = 1
                        if self.p4_dc_status == 1:
                            self.p6dc1cw_on_line_dc_4to5 = 1
                            if self.p5_dc_status == 1:
                                self.p6dc1cw_on_line_dc_5to6 = 1

                                #Check counterclockwise
        if (self.p6dc1list_voltage >= 40 and self.p6_dc1_status == 1 and self.p6_dc_status == 1):
            self.p6dc1ccw_on_line_dc_5to6 = 1
            if self.p5_dc_status == 1:
                self.p6dc1ccw_on_line_dc_4to5 = 1
                if self.p4_dc_status == 1:
                    self.p6dc1ccw_on_line_dc_3to4 = 1
                    if self.p3_dc_status == 1:
                        self.p6dc1ccw_on_line_dc_8to3 = 1
                        if self.p8_dc_status == 1:
                            self.p6dc1ccw_on_line_dc_7to8 = 1



                            #Supplied by p6dc2
        self.p6dc2_on_line_dc_5to6 = 0
        if (self.p6dc2list_voltage >= 40 and self.p6_dc2_status == 1):
            self.p6dc2_on_line_dc_5to6 = 1

            #Supplied by p7dc1
        self.p7dc1_on_line_dc_7to8 = 0
        if (self.p7dc1list_voltage >= 40 and self.p7_dc1_status == 1):
            self.p7dc1_on_line_dc_7to8 = 1

            #Supplied by p7dc2
        if (self.p7dc2list_voltage >= 40 and self.p7_dc2_status == 1):
            self.p7dc2_on_line_dc_6to7 = 1
        else:
            self.p7dc2_on_line_dc_6to7 = 0

            #Supplied by p8dc1
        self.p8dc1_on_line_dc_8to3 = 0
        if (self.p8dc1list_voltage >= 40 and self.p8_dc1_status == 1):
            self.p8dc1_on_line_dc_8to3 = 1

            #Supplied by p8dc2
        self.p8dc2_on_line_dc_7to8 = 0
        if (self.p8dc2list_voltage >= 40 and self.p8_dc2_status == 1):
            self.p8dc2_on_line_dc_7to8 = 1

        #-------Turn on/off dc interconnected line-------------------------------------#
        #line 3to4   
        if (
                                        self.p3dc1_on_line_dc_3to4 == 1 or self.p4dc2_on_line_dc_3to4 == 1 or self.p5dc1cw_on_line_dc_3to4 == 1 or self.p5dc1ccw_on_line_dc_3to4 == 1 or self.p6dc1cw_on_line_dc_3to4 == 1 or self.p6dc1ccw_on_line_dc_3to4 == 1 ):
            self.line_dc_3to4.setStyleSheet("color: rgb(0, 255, 0);")  #set to green 
        else:
            self.line_dc_3to4.setStyleSheet("color: rgb(0, 0, 255);")  #set back to blue
        #line 4to5    
        if (
                                        self.p4dc1_on_line_dc_4to5 == 1 or self.p5dc2_on_line_dc_4to5 == 1 or self.p5dc1ccw_on_line_dc_4to5 == 1 or self.p5dc1cw_on_line_dc_4to5 == 1 or self.p6dc1ccw_on_line_dc_4to5 == 1 or self.p6dc1cw_on_line_dc_4to5 == 1):
            self.line_dc_4to5.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.line_dc_4to5.setStyleSheet("color: rgb(0, 0, 255);")
            #line 5to6
        if (
                                self.p5dc1_on_line_dc_5to6 == 1 or self.p6dc2_on_line_dc_5to6 == 1 or self.p6dc1ccw_on_line_dc_5to6 == 1 or self.p6dc1cw_on_line_dc_5to6 == 1):
            self.line_dc_5to6.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.line_dc_5to6.setStyleSheet("color: rgb(0, 0, 255);")
        #line 6to7    
        if (
                                self.p6dc1_on_line_dc_6to7 == 1 or self.p7dc2_on_line_dc_6to7 == 1 or self.p5dc1ccw_on_line_dc_6to7 == 1 or self.p5dc1cw_on_line_dc_6to7 == 1 ):
            self.line_dc_6to7.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.line_dc_6to7.setStyleSheet("color: rgb(0, 0, 255);")
        #line 7to8    
        if (
                                        self.p7dc1_on_line_dc_7to8 == 1 or self.p8dc2_on_line_dc_7to8 == 1 or self.p5dc1ccw_on_line_dc_7to8 == 1 or self.p5dc1cw_on_line_dc_7to8 == 1 or self.p6dc1ccw_on_line_dc_7to8 == 1 or self.p6dc1cw_on_line_dc_7to8 == 1):
            self.line_dc_7to8.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.line_dc_7to8.setStyleSheet("color: rgb(0, 0, 255);")
            #line 8to3
        if (
                                        self.p8dc1_on_line_dc_8to3 == 1 or self.p3dc2_on_line_dc_8to3 == 1 or self.p5dc1ccw_on_line_dc_8to3 == 1 or self.p5dc1cw_on_line_dc_8to3 == 1 or self.p6dc1ccw_on_line_dc_8to3 == 1 or self.p6dc1cw_on_line_dc_8to3 == 1):
            self.line_dc_8to3_1.setStyleSheet("color: rgb(0, 255, 0);")
            self.line_dc_8to3_2.setStyleSheet("color: rgb(0, 255, 0);")
            self.line_dc_8to3_3.setStyleSheet("color: rgb(0, 255, 0);")
            self.line_dc_8to3_4.setStyleSheet("color: rgb(0, 255, 0);")
            self.line_dc_8to3_5.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.line_dc_8to3_1.setStyleSheet("color: rgb(0, 0, 255);")
            self.line_dc_8to3_2.setStyleSheet("color: rgb(0, 0, 255);")
            self.line_dc_8to3_3.setStyleSheet("color: rgb(0, 0, 255);")
            self.line_dc_8to3_4.setStyleSheet("color: rgb(0, 0, 255);")
            self.line_dc_8to3_5.setStyleSheet("color: rgb(0, 0, 255);")


        #-------For dc output connected line-------------------------------------------#
        if (self.p3dc1list_voltage) >= 40:
            self.line_p3dc1.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p3dc1.setStyleSheet("color: rgb(0, 0, 255);")  #set back to blue

        if (self.p3dc2list_voltage) >= 40:
            self.line_p3dc2.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p3dc2.setStyleSheet("color: rgb(0, 0, 255);")  #set back to blue

        if (self.p4dc1list_voltage) >= 40:
            self.line_p4dc1.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p4dc1.setStyleSheet("color: rgb(0, 0, 255);")  #set back to blue

        if (self.p4dc2list_voltage) >= 40:
            self.line_p4dc2.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p4dc2.setStyleSheet("color: rgb(0, 0, 255);")  #set back to blue

        if (self.p5dc1list_voltage) >= 40:
            self.line_p5dc1.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p5dc1.setStyleSheet("color: rgb(0, 0, 255);")  #set back to blue

        if (self.p5dc2list_voltage) >= 40:
            self.line_p5dc2.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p5dc2.setStyleSheet(
                "color: rgb(0, 0, 255);")  #set back to blue

        if (self.p6dc1list_voltage) >= 40:
            self.line_p6dc1.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p6dc1.setStyleSheet("color: rgb(0, 0, 255);")  #set back to blue

        if (self.p6dc2list_voltage) >= 40:
            self.line_p6dc2.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p6dc2.setStyleSheet("color: rgb(0, 0, 255);")  #set back to blue

        if (self.p7dc1list_voltage) >= 40:
            self.line_p7dc1.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p7dc1.setStyleSheet("color: rgb(0, 0, 255);")  #set back to blue

        if (self.p7dc2list_voltage) >= 40:
            self.line_p7dc2.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p7dc2.setStyleSheet("color: rgb(0, 0, 255);")  #set back to blue

        if (self.p8dc1list_voltage) >= 40:
            self.line_p8dc1.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p8dc1.setStyleSheet("color: rgb(0, 0, 255);")  #set back to blue

        if (self.p8dc2list_voltage) >= 40:
            self.line_p8dc2.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p8dc2.setStyleSheet("color: rgb(0, 0, 255);")  #set back to blue


        #-------Update AC line---------------------------------------------------------#
        #Supplied by p3ac1
        self.p3ac1_on_line_ac_3to4 = 0

        self.p3ac1cw_on_line_ac_4to5 = 0
        self.p3ac1cw_on_line_ac_5to6 = 0
        self.p3ac1cw_on_line_ac_6to7 = 0
        self.p3ac1cw_on_line_ac_7to8 = 0
        self.p3ac1cw_on_line_ac_8to3 = 0

        self.p3ac1ccw_on_line_ac_4to5 = 0
        self.p3ac1ccw_on_line_ac_5to6 = 0
        self.p3ac1ccw_on_line_ac_6to7 = 0
        self.p3ac1ccw_on_line_ac_7to8 = 0
        self.p3ac1ccw_on_line_ac_8to3 = 0

        #Check clockwise 
        if (self.p3ac1_LN_Voltage >= 40 and self.p3_ac1_status == 1):
            self.p3ac1_on_line_ac_3to4 = 1
            if self.p4_ac_status == 1:
                self.p3ac1cw_on_line_ac_4to5 = 1
                if self.p5_ac_status == 1:
                    self.p3ac1cw_on_line_ac_5to6 = 1
                    if self.p6_ac_status == 1:
                        self.p3ac1cw_on_line_ac_6to7 = 1
                        if self.p7_ac_status == 1:
                            self.p3ac1cw_on_line_ac_7to8 = 1
                            if self.p8_ac_status == 1:
                                self.p3ac1cw_on_line_ac_8to3 = 1

                                #Check counterclockwise
        if (self.p3ac1_LN_Voltage >= 40 and self.p3_ac1_status == 1 and self.p3_ac_status == 1):
            self.p3ac1ccw_on_line_ac_8to3 = 1
            if self.p4_ac_status == 1:
                self.p3ac1ccw_on_line_ac_7to8 = 1
                if self.p5_ac_status == 1:
                    self.p3ac1ccw_on_line_ac_6to7 = 1
                    if self.p6_ac_status == 1:
                        self.p3ac1ccw_on_line_ac_5to6 = 1
                        if self.p7_ac_status == 1:
                            self.p3ac1ccw_on_line_ac_4to5 = 1

                            #Supplied by p3ac2
        self.p3ac2_on_line_ac_8to3 = 0

        self.p3ac2ccw_on_line_ac_3to4 = 0
        self.p3ac2ccw_on_line_ac_4to5 = 0
        self.p3ac2ccw_on_line_ac_5to6 = 0
        self.p3ac2ccw_on_line_ac_6to7 = 0
        self.p3ac2ccw_on_line_ac_7to8 = 0

        self.p3ac2cw_on_line_ac_4to5 = 0
        self.p3ac2cw_on_line_ac_5to6 = 0
        self.p3ac2cw_on_line_ac_6to7 = 0
        self.p3ac2cw_on_line_ac_7to8 = 0
        #Check counterclockwise 
        if (self.p3ac2_LN_Voltage >= 40 and self.p3_ac2_status == 1):
            self.p3ac2_on_line_ac_8to3 = 1
            if self.p8_ac_status == 1:
                self.p3ac2cc_on_line_ac_7to8 = 1
                if self.p7_ac_status == 1:
                    self.p3ac2cc_on_line_ac_6to7 = 1
                    if self.p6_ac_status == 1:
                        self.p3ac2cc_on_line_ac_5to6 = 1
                        if self.p5_ac_status == 1:
                            self.p3ac2cc_on_line_ac_4to5 = 1

                            #Check clockwise
        if (self.p3ac2_LN_Voltage >= 40 and self.p3_ac2_status == 1 and self.p3_ac_status == 1):
            self.p3ac2ccw_on_line_ac_3to4 = 1
            if self.p4_ac_status == 1:
                self.p3ac2ccw_on_line_ac_4to5 = 1
                if self.p5_ac_status == 1:
                    self.p3ac2ccw_on_line_ac_5to6 = 1
                    if self.p6_ac_status == 1:
                        self.p3ac2ccw_on_line_ac_6to7 = 1
                        if self.p7_ac_status == 1:
                            self.p3ac2ccw_on_line_ac_7to8 = 1


                            #Supplied by p4ac1
        self.p4ac1_on_line_ac_4to5 = 0
        if (self.p4ac1_LN_Voltage >= 40 and self.p4_ac1_status == 1):
            self.p4ac1_on_line_ac_4to5 = 1

            #Supplied by p4ac2
        self.p4ac2_on_line_ac_3to4 = 0
        if (self.p4ac2_LN_Voltage >= 40 and self.p4_ac2_status == 1):
            self.p4ac2_on_line_ac_3to4 = 1

            #Supplied by p5ac1
        self.p5ac1_on_line_ac_5to6 = 0
        if (self.p5ac1_LN_Voltage >= 40 and self.p4_ac1_status == 1):
            self.p5ac1_on_line_ac_4to5 = 1

            #Supplied by p5ac2
        self.p5ac2_on_line_ac_4to5 = 0
        if (self.p5ac2_LN_Voltage >= 40 and self.p4_ac2_status == 1):
            self.p5ac2_on_line_ac_3to4 = 1

            #Supplied by p6ac1
        self.p6ac1_on_line_ac_6to7 = 0
        if (self.p6ac1_LN_Voltage >= 40 and self.p4_ac1_status == 1):
            self.p6ac1_on_line_ac_6to7 = 1

            #Supplied by p6ac2
        self.p6ac2_on_line_ac_5to6 = 0
        if (self.p6ac2_LN_Voltage >= 40 and self.p4_ac2_status == 1):
            self.p6ac2_on_line_ac_5to6 = 1

            #Supplied by p7ac1
        self.p7ac1_on_line_ac_7to8 = 0
        if (self.p7ac1_LN_Voltage >= 40 and self.p4_ac1_status == 1):
            self.p7ac1_on_line_ac_7to8 = 1

            #Supplied by p7ac2
        self.p7ac2_on_line_ac_6to7 = 0
        if (self.p7ac2_LN_Voltage >= 40 and self.p4_ac2_status == 1):
            self.p7ac2_on_line_ac_6to7 = 1

            #Supplied by p8ac1
        self.p8ac1_on_line_ac_8to3 = 0
        if (self.p8ac1_LN_Voltage >= 40 and self.p4_ac1_status == 1):
            self.p8ac1_on_line_ac_8to3 = 1

            #Supplied by p8ac2
        self.p8ac2_on_line_ac_7to8 = 0
        if (self.p8ac2_LN_Voltage >= 40 and self.p4_ac2_status == 1):
            self.p8ac2_on_line_ac_7to8 = 1


        #-------Turn on/off AC interconnected line-------------------------------------#
        #line 3to4   
        if (self.p3ac1_on_line_ac_3to4 == 1 or self.p4ac2_on_line_ac_3to4 == 1 or self.p3ac2ccw_on_line_ac_3to4 == 1):
            self.line_ac_3to4.setStyleSheet("color: rgb(0, 255, 0);")  #set to green 
        else:
            self.line_ac_3to4.setStyleSheet("color: rgb(255, 0, 0);")  #set back to red
        #line 4to5    
        if (
                                        self.p4ac1_on_line_ac_4to5 == 1 or self.p5ac2_on_line_ac_4to5 == 1 or self.p3ac1cw_on_line_ac_4to5 == 1 or self.p3ac1ccw_on_line_ac_4to5 == 1 or self.p3ac2cw_on_line_ac_4to5 == 1 or self.p3ac2ccw_on_line_ac_4to5 == 1):
            self.line_ac_4to5.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.line_ac_4to5.setStyleSheet("color: rgb(255, 0, 0);")
            #line 5to6
        if (
                                        self.p5ac1_on_line_ac_5to6 == 1 or self.p6ac2_on_line_ac_5to6 == 1 or self.p3ac1cw_on_line_ac_5to6 == 1 or self.p3ac1ccw_on_line_ac_5to6 == 1 or self.p3ac2cw_on_line_ac_5to6 == 1 or self.p3ac2ccw_on_line_ac_5to6 == 1):
            self.line_ac_5to6.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.line_ac_5to6.setStyleSheet("color: rgb(255, 0, 0);")
        #line 6to7    
        if (
                                        self.p6ac1_on_line_ac_6to7 == 1 or self.p7ac2_on_line_ac_6to7 == 1 or self.p3ac1cw_on_line_ac_6to7 == 1 or self.p3ac1ccw_on_line_ac_6to7 == 1 or self.p3ac2cw_on_line_ac_6to7 == 1 or self.p3ac2ccw_on_line_ac_6to7 == 1):
            self.line_ac_6to7.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.line_ac_6to7.setStyleSheet("color: rgb(255, 0, 0);")
        #line 7to8    
        if (
                                        self.p7ac1_on_line_ac_7to8 == 1 or self.p8ac2_on_line_ac_7to8 == 1 or self.p3ac1cw_on_line_ac_7to8 == 1 or self.p3ac1ccw_on_line_ac_7to8 == 1 or self.p3ac2cw_on_line_ac_7to8 == 1 or self.p3ac2ccw_on_line_ac_7to8 == 1):
            self.line_ac_7to8.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.line_ac_7to8.setStyleSheet("color: rgb(255, 0, 0);")
            #line 8to3
        if (
                                self.p8ac1_on_line_ac_8to3 == 1 or self.p3ac2_on_line_ac_8to3 == 1 or self.p3ac1cw_on_line_ac_8to3 == 1 or self.p3ac1ccw_on_line_ac_8to3 == 1):
            self.line_ac_8to3_1.setStyleSheet("color: rgb(0, 255, 0);")
            self.line_ac_8to3_2.setStyleSheet("color: rgb(0, 255, 0);")
            self.line_ac_8to3_3.setStyleSheet("color: rgb(0, 255, 0);")
            self.line_ac_8to3_4.setStyleSheet("color: rgb(0, 255, 0);")
            self.line_ac_8to3_5.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.line_ac_8to3_1.setStyleSheet("color: rgb(255, 0, 0);")
            self.line_ac_8to3_2.setStyleSheet("color: rgb(255, 0, 0);")
            self.line_ac_8to3_3.setStyleSheet("color: rgb(255, 0, 0);")
            self.line_ac_8to3_4.setStyleSheet("color: rgb(255, 0, 0);")
            self.line_ac_8to3_5.setStyleSheet("color: rgb(255, 0, 0);")


        #-------Turn on/off AC output connected line-----------------------------------#
        if (self.p3ac1_LN_Voltage) >= 40:
            self.line_p3ac1.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p3ac1.setStyleSheet("color: rgb(255, 0, 0);")  #set back to red

        if (self.p3ac2_LN_Voltage) >= 40:
            self.line_p3ac2.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p3ac2.setStyleSheet("color: rgb(255, 0, 0);")  #set back to red

        if (self.p4ac1_LN_Voltage) >= 40:
            self.line_p4ac1.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p4ac1.setStyleSheet("color: rgb(255, 0, 0);")  #set back to red

        if (self.p4ac2_LN_Voltage) >= 40:
            self.line_p4ac2.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p4ac2.setStyleSheet("color: rgb(255, 0, 0);")  #set back to red

        if (self.p5ac1_LN_Voltage) >= 40:
            self.line_p5ac1.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p5ac1.setStyleSheet("color: rgb(255, 0, 0);")  #set back to red

        if (self.p5ac2_LN_Voltage) >= 40:
            self.line_p5ac2.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p5ac2.setStyleSheet(
                "color: rgb(255, 0, 0);")  #set back to red

        if (self.p6ac1_LN_Voltage) >= 40:
            self.line_p6ac1.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p6ac1.setStyleSheet("color: rgb(255, 0, 0);")  #set back to red

        if (self.p6ac2_LN_Voltage) >= 40:
            self.line_p6ac2.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p6ac2.setStyleSheet("color: rgb(255, 0, 0);")  #set back to red

        if (self.p7ac1_LN_Voltage) >= 40:
            self.line_p7ac1.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p7ac1.setStyleSheet("color: rgb(255, 0, 0);")  #set back to red

        if (self.p7ac2_LN_Voltage) >= 40:
            self.line_p7ac2.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p7ac2.setStyleSheet("color: rgb(255, 0, 0);")  #set back to red

        if (self.p8ac1_LN_Voltage) >= 40:
            self.line_p8ac1.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p8ac1.setStyleSheet("color: rgb(255, 0, 0);")  #set back to red

        if (self.p8ac2_LN_Voltage) >= 40:
            self.line_p8ac2.setStyleSheet("color: rgb(0, 255, 0);")  #set to green
        else:
            self.line_p8ac2.setStyleSheet("color: rgb(255, 0, 0);")  #set back to red

        #-------------------Arrow direction---------------------------------------------#
        if self.p4dc1list_power >= 0.02:
            self.arrow_p4dc1.setIcon(QtGui.QIcon("images/arrow_down.jpg"))
            self.arrow_p4dc1_2.setIcon(QtGui.QIcon("images/arrow_down.jpg"))
        elif self.p4dc1list_power <= (-0.02):
            self.arrow_p4dc1.setIcon(QtGui.QIcon("images/arrow_up.jpg"))
            self.arrow_p4dc1_2.setIcon(QtGui.QIcon("images/arrow_up.jpg"))
        else:
            self.arrow_p4dc1.setIcon(QtGui.QIcon(""))
            self.arrow_p4dc1_2.setIcon(QtGui.QIcon(""))

        if self.p5dc1list_power >= 0.02:
            self.arrow_p5dc1.setIcon(QtGui.QIcon("images/arrow_down.jpg"))
        elif self.p5dc1list_power <= (-0.02):
            self.arrow_p5dc1.setIcon(QtGui.QIcon("images/arrow_up.jpg"))
        else:
            self.arrow_p5dc1.setIcon(QtGui.QIcon(""))

        if self.p6dc1list_power >= 0.02:
            self.arrow_p6dc1.setIcon(QtGui.QIcon("images/arrow_down.jpg"))
        elif self.p6dc1list_power <= (-0.02):
            self.arrow_p6dc1.setIcon(QtGui.QIcon("images/arrow_up.jpg"))
        else:
            self.arrow_p6dc1.setIcon(QtGui.QIcon(""))

        if self.p3dc2list_power >= 0.02:
            self.arrow_p3dc2.setIcon(QtGui.QIcon("images/arrow_up.jpg"))
            self.arrow_p3ac2.setIcon(QtGui.QIcon("images/arrow_up.jpg"))
        elif self.p3dc2list_power <= (-0.02):
            self.arrow_p3dc2.setIcon(QtGui.QIcon("images/arrow_down.jpg"))
            self.arrow_p3ac2.setIcon(QtGui.QIcon("images/arrow_down.jpg"))
        else:
            self.arrow_p3dc2.setIcon(QtGui.QIcon(""))
            self.arrow_p3ac2.setIcon(QtGui.QIcon(""))


            #--------------------------------------------------------------------------------#

    #Functions for the pushbutton for GUI                                                              
    def pb_batt1_controller_clicked(self):
        #Open Battery1 Control GUI
        print('Open Battery GUI')
        self.wndbattery1 = Mainbattery1()  #Mainbattery1() is the classname of GUI File
        self.wndbattery1.show()

    def pb_pv_mppt_controller_clicked(self):
        #Open PV Control GUI
        print('Open PV GUI')
        self.wndpv = Mainpv()  #Mainpv() is the classname of the GUI File
        self.wndpv.show()

    def pb_bidir_clicked(self):
        #Open Bidir Control GUI
        print('Open Bidir GUI')
        self.wndbidir.show()

        #Control of the switches
        #------------------------------------------------------------------------#
        #Panel 3 DC switches  

    def switch_p3dc1_clicked(self):
        #print ('switch_p3dc1')
        if self.p3_dc1_status == 1:
            client.write_coils(304, [False])
            self.switch_p3dc1.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        elif self.p3_dc1_status == 0:
            client.write_coils(304, [True])
            self.switch_p3dc1.setIcon(QtGui.QIcon("images/dc on up.jpg"))

    def switch_p3dc_clicked(self):
        #print ('switch_p3dc')        
        if self.p3_dc_status == 1:
            client.write_coils(301, [False])
            self.switch_p3dc.setIcon(QtGui.QIcon("images/dc off.jpg"))
        elif self.p3_dc_status == 0:
            client.write_coils(301, [True])
            self.switch_p3dc.setIcon(QtGui.QIcon("images/dc on.jpg"))

    def switch_p3dc2_clicked(self):
        #print ('switch_p3dc2')
        if self.p3_dc2_status == 1:
            client.write_coils(305, [False])
            self.switch_p3dc2.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        elif self.p3_dc2_status == 0:
            client.write_coils(305, [True])
            self.switch_p3dc2.setIcon(QtGui.QIcon("images/dc on up.jpg"))

            #Panel 3 AC switches

    def switch_p3ac1_clicked(self):
        #print ('switch_p3ac1')
        if self.p3_ac1_status == 1:
            client.write_coils(302, [False])
            self.switch_p3ac1.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        elif self.p3_ac1_status == 0:
            client.write_coils(302, [True])
            self.switch_p3ac1.setIcon(QtGui.QIcon("images/ac on up.jpg"))

    def switch_p3ac_clicked(self):
        #print ('switch_p3ac')        
        if self.p3_ac_status == 1:
            client.write_coils(300, [False])
            self.switch_p3ac.setIcon(QtGui.QIcon("images/ac off.jpg"))
        elif self.p3_ac_status == 0:
            client.write_coils(300, [True])
            self.switch_p3ac.setIcon(QtGui.QIcon("images/ac on.jpg"))

    def switch_p3ac2_clicked(self):
        #print ('switch_p3ac2')
        if self.p3_ac2_status == 1:
            client.write_coils(303, [False])
            self.switch_p3ac2.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        elif self.p3_ac2_status == 0:
            client.write_coils(303, [True])
            self.switch_p3ac2.setIcon(QtGui.QIcon("images/ac on up.jpg"))
            #-------------------------------------------------------------------------#

            #------------------------------------------------------------------------#
            #Panel 4 DC switches

    def switch_p4dc1_clicked(self):
        #print ('switch_p4dc1')
        if self.p4_dc1_status == 1:
            client.write_coils(404, [False])
            self.switch_p4dc1.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        elif self.p4_dc1_status == 0:
            client.write_coils(404, [True])
            self.switch_p4dc1.setIcon(QtGui.QIcon("images/dc on up.jpg"))

    def switch_p4dc_clicked(self):
        # print ('switch_p4dc')
        if self.p4_dc_status == 1:
            client.write_coils(401, [False])
            self.switch_p4dc.setIcon(QtGui.QIcon("images/dc off.jpg"))
        elif self.p4_dc_status == 0:
            client.write_coils(401, [True])
            self.switch_p4dc.setIcon(QtGui.QIcon("images/dc on.jpg"))

    def switch_p4dc2_clicked(self):
        #print ('switch_p4dc2')
        if self.p4_dc2_status == 1:
            client.write_coils(405, [False])
            self.switch_p4dc2.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        elif self.p4_dc2_status == 0:
            client.write_coils(405, [True])
            self.switch_p4dc2.setIcon(QtGui.QIcon("images/dc on up.jpg"))

            #Panel 4 AC switches

    def switch_p4ac1_clicked(self):
        #print ('switch_p4ac1')
        if self.p4_ac1_status == 1:
            client.write_coils(402, [False])
            self.switch_p4ac1.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        elif self.p4_ac1_status == 0:
            client.write_coils(402, [True])
            self.switch_p4ac1.setIcon(QtGui.QIcon("images/ac on up.jpg"))

    def switch_p4ac_clicked(self):
        #print ('switch_p4ac')        
        if self.p4_ac_status == 1:
            client.write_coils(400, [False])
            self.switch_p4ac.setIcon(QtGui.QIcon("images/ac off.jpg"))
        elif self.p4_ac_status == 0:
            client.write_coils(400, [True])
            self.switch_p4ac.setIcon(QtGui.QIcon("images/ac on.jpg"))

    def switch_p4ac2_clicked(self):
        #print ('switch_p4ac2')
        if self.p4_ac2_status == 1:
            client.write_coils(403, [False])
            self.switch_p4ac2.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        elif self.p4_ac2_status == 0:
            client.write_coils(403, [True])
            self.switch_p4ac2.setIcon(QtGui.QIcon("images/ac on up.jpg"))
            #-------------------------------------------------------------------------#
            #------------------------------------------------------------------------#
            #Panel 5 DC switches

    def switch_p5dc1_clicked(self):
        #print ('switch_p5dc1')
        if self.p5_dc1_status == 1:
            client.write_coils(504, [False])
            self.switch_p5dc1.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        elif self.p5_dc1_status == 0:
            client.write_coils(504, [True])
            self.switch_p5dc1.setIcon(QtGui.QIcon("images/dc on up.jpg"))

    def switch_p5dc_clicked(self):
        #print ('switch_p5dc')        
        if self.p5_dc_status == 1:
            client.write_coils(501, [False])
            self.switch_p5dc.setIcon(QtGui.QIcon("images/dc off.jpg"))
        elif self.p5_dc_status == 0:
            client.write_coils(501, [True])
            self.switch_p5dc.setIcon(QtGui.QIcon("images/dc on.jpg"))

    def switch_p5dc2_clicked(self):
        #print ('switch_p5dc2')
        if self.p5_dc2_status == 1:
            client.write_coils(505, [False])
            self.switch_p5dc2.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        elif self.p5_dc2_status == 0:
            client.write_coils(505, [True])
            self.switch_p5dc2.setIcon(QtGui.QIcon("images/dc on up.jpg"))

            #Panel 5 AC switches

    def switch_p5ac1_clicked(self):
        #print ('switch_p5ac1')
        if self.p5_ac1_status == 1:
            client.write_coils(502, [False])
            self.switch_p5ac1.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        elif self.p5_ac1_status == 0:
            client.write_coils(502, [True])
            self.switch_p5ac1.setIcon(QtGui.QIcon("images/ac on up.jpg"))

    def switch_p5ac_clicked(self):
        #print ('switch_p5ac')        
        if self.p5_ac_status == 1:
            client.write_coils(500, [False])
            self.switch_p5ac.setIcon(QtGui.QIcon("images/ac off.jpg"))
        elif self.p5_ac_status == 0:
            client.write_coils(500, [True])
            self.switch_p5ac.setIcon(QtGui.QIcon("images/ac on.jpg"))

    def switch_p5ac2_clicked(self):
        #print ('switch_p5ac2')
        if self.p5_ac2_status == 1:
            client.write_coils(503, [False])
            self.switch_p5ac2.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        elif self.p5_ac2_status == 0:
            client.write_coils(503, [True])
            self.switch_p5ac2.setIcon(QtGui.QIcon("images/ac on up.jpg"))
            #-------------------------------------------------------------------------#
            #------------------------------------------------------------------------#
            #Panel 6 DC switches

    def switch_p6dc1_clicked(self):
        #print ('switch_p6dc1')
        if self.p6_dc1_status == 1:
            client.write_coils(604, [False])
            self.switch_p6dc1.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        elif self.p6_dc1_status == 0:
            client.write_coils(604, [True])
            self.switch_p6dc1.setIcon(QtGui.QIcon("images/dc on up.jpg"))

    def switch_p6dc_clicked(self):
        #print ('switch_p6dc')        
        if self.p6_dc_status == 1:
            client.write_coils(601, [False])
            self.switch_p6dc.setIcon(QtGui.QIcon("images/dc off.jpg"))
        elif self.p6_dc_status == 0:
            client.write_coils(601, [True])
            self.switch_p6dc.setIcon(QtGui.QIcon("images/dc on.jpg"))

    def switch_p6dc2_clicked(self):
        #print ('switch_p6dc2')
        if self.p6_dc2_status == 1:
            client.write_coils(605, [False])
            self.switch_p6dc2.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        elif self.p6_dc2_status == 0:
            client.write_coils(605, [True])
            self.switch_p6dc2.setIcon(QtGui.QIcon("images/dc on up.jpg"))

            #Panel 6 AC switches

    def switch_p6ac1_clicked(self):
        #print ('switch_p6ac1')
        if self.p6_ac1_status == 1:
            client.write_coils(602, [False])
            self.switch_p6ac1.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        elif self.p6_ac1_status == 0:
            client.write_coils(602, [True])
            self.switch_p6ac1.setIcon(QtGui.QIcon("images/ac on up.jpg"))

    def switch_p6ac_clicked(self):
        #print ('switch_p6ac')        
        if self.p6_ac_status == 1:
            client.write_coils(600, [False])
            self.switch_p6ac.setIcon(QtGui.QIcon("images/ac off.jpg"))
        elif self.p6_ac_status == 0:
            client.write_coils(600, [True])
            self.switch_p6ac.setIcon(QtGui.QIcon("images/ac on.jpg"))

    def switch_p6ac2_clicked(self):
        #print ('switch_p6ac2')
        if self.p6_ac2_status == 1:
            client.write_coils(603, [False])
            self.switch_p6ac2.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        elif self.p6_ac2_status == 0:
            client.write_coils(603, [True])
            self.switch_p6ac2.setIcon(QtGui.QIcon("images/ac on up.jpg"))
            #-------------------------------------------------------------------------#
            #------------------------------------------------------------------------#
            #Panel 7 DC switches

    def switch_p7dc1_clicked(self):
        #print ('switch_p7dc1')
        if self.p7_dc1_status == 1:
            client.write_coils(704, [False])
            self.switch_p7dc1.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        elif self.p7_dc1_status == 0:
            client.write_coils(704, [True])
            self.switch_p7dc1.setIcon(QtGui.QIcon("images/dc on up.jpg"))

    def switch_p7dc_clicked(self):
        #print ('switch_p7dc')        
        if self.p7_dc_status == 1:
            client.write_coils(701, [False])
            self.switch_p7dc.setIcon(QtGui.QIcon("images/dc off.jpg"))
        elif self.p7_dc_status == 0:
            client.write_coils(701, [True])
            self.switch_p7dc.setIcon(QtGui.QIcon("images/dc on.jpg"))

    def switch_p7dc2_clicked(self):
        #print ('switch_p7dc2')
        if self.p7_dc2_status == 1:
            client.write_coils(705, [False])
            self.switch_p7dc2.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        elif self.p7_dc2_status == 0:
            client.write_coils(705, [True])
            self.switch_p7dc2.setIcon(QtGui.QIcon("images/dc on up.jpg"))

            #Panel 7 AC switches

    def switch_p7ac1_clicked(self):
        #print ('switch_p7ac1')
        if self.p7_ac1_status == 1:
            client.write_coils(702, [False])
            self.switch_p7ac1.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        elif self.p7_ac1_status == 0:
            client.write_coils(702, [True])
            self.switch_p7ac1.setIcon(QtGui.QIcon("images/ac on up.jpg"))

    def switch_p7ac_clicked(self):
        #print ('switch_p7ac')        
        if self.p7_ac_status == 1:
            client.write_coils(700, [False])
            self.switch_p7ac.setIcon(QtGui.QIcon("images/ac off.jpg"))
        elif self.p7_ac_status == 0:
            client.write_coils(700, [True])
            self.switch_p7ac.setIcon(QtGui.QIcon("images/ac on.jpg"))

    def switch_p7ac2_clicked(self):
        #print ('switch_p7ac2')
        if self.p7_ac2_status == 1:
            client.write_coils(703, [False])
            self.switch_p7ac2.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        elif self.p7_ac2_status == 0:
            client.write_coils(703, [True])
            self.switch_p7ac2.setIcon(QtGui.QIcon("images/ac on up.jpg"))
            #-------------------------------------------------------------------------#
            #------------------------------------------------------------------------#
            #Panel 8 DC switches

    def switch_p8dc1_clicked(self):
        #print ('switch_p8dc1')
        if self.p8_dc1_status == 1:
            client.write_coils(804, [False])
            self.switch_p8dc1.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        elif self.p8_dc1_status == 0:
            client.write_coils(804, [True])
            self.switch_p8dc1.setIcon(QtGui.QIcon("images/dc on up.jpg"))

    def switch_p8dc_clicked(self):
        #print ('switch_p8dc')        
        if self.p8_dc_status == 1:
            client.write_coils(801, [False])
            self.switch_p8dc.setIcon(QtGui.QIcon("images/dc off.jpg"))
        elif self.p8_dc_status == 0:
            client.write_coils(801, [True])
            self.switch_p8dc.setIcon(QtGui.QIcon("images/dc on.jpg"))

    def switch_p8dc2_clicked(self):
        #print ('switch_p8dc2')
        if self.p8_dc2_status == 1:
            client.write_coils(805, [False])
            self.switch_p8dc2.setIcon(QtGui.QIcon("images/dc off up.jpg"))
        elif self.p8_dc2_status == 0:
            client.write_coils(805, [True])
            self.switch_p8dc2.setIcon(QtGui.QIcon("images/dc on up.jpg"))

            #Panel 8 AC switches

    def switch_p8ac1_clicked(self):
        #print ('switch_p8ac1')
        if self.p8_ac1_status == 1:
            client.write_coils(802, [False])
            self.switch_p8ac1.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        elif self.p8_ac1_status == 0:
            client.write_coils(802, [True])
            self.switch_p8ac1.setIcon(QtGui.QIcon("images/ac on up.jpg"))

    def switch_p8ac_clicked(self):
        #print ('switch_p8ac')        
        if self.p8_ac_status == 1:
            client.write_coils(800, [False])
            self.switch_p8ac.setIcon(QtGui.QIcon("images/ac off.jpg"))
        elif self.p8_ac_status == 0:
            client.write_coils(800, [True])
            self.switch_p8ac.setIcon(QtGui.QIcon("images/ac on.jpg"))

    def switch_p8ac2_clicked(self):
        #print ('switch_p8ac2')
        if self.p8_ac2_status == 1:
            client.write_coils(803, [False])
            self.switch_p8ac2.setIcon(QtGui.QIcon("images/ac off up.jpg"))
        elif self.p8_ac2_status == 0:
            client.write_coils(803, [True])
            self.switch_p8ac2.setIcon(QtGui.QIcon("images/ac on up.jpg"))
            #-------------------------------------------------------------------------#


    def __init__(self):
        PyQt5.QtWidgets.QWidget.__init__(self)
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        self.wndbidir = Mainbidir()  #Mainbidir() is the classname of the GUI File

        #Event handlers     
        # Bind the event handlers to buttons
        #Event handlers for GUI
        self.pb_batt1_controller.clicked.connect(self.pb_batt1_controller_clicked)
        self.pb_pv_mppt_controller.clicked.connect(self.pb_pv_mppt_controller_clicked)
        self.pb_bidir.clicked.connect(self.pb_bidir_clicked)

        #Event handler for switches  
        self.switch_p8dc1.clicked.connect(self.switch_p8dc1_clicked)
        self.switch_p8dc.clicked.connect(self.switch_p8dc_clicked)
        self.switch_p8dc2.clicked.connect(self.switch_p8dc2_clicked)

        self.switch_p8ac1.clicked.connect(self.switch_p8ac1_clicked)
        self.switch_p8ac.clicked.connect(self.switch_p8ac_clicked)
        self.switch_p8ac2.clicked.connect(self.switch_p8ac2_clicked)

        self.switch_p7dc1.clicked.connect(self.switch_p7dc1_clicked)
        self.switch_p7dc.clicked.connect(self.switch_p7dc_clicked)
        self.switch_p7dc2.clicked.connect(self.switch_p7dc2_clicked)

        self.switch_p7ac1.clicked.connect(self.switch_p7ac1_clicked)
        self.switch_p7ac.clicked.connect(self.switch_p7ac_clicked)
        self.switch_p7ac2.clicked.connect(self.switch_p7ac2_clicked)

        self.switch_p6dc1.clicked.connect(self.switch_p6dc1_clicked)
        self.switch_p6dc.clicked.connect(self.switch_p6dc_clicked)
        self.switch_p6dc2.clicked.connect(self.switch_p6dc2_clicked)

        self.switch_p6ac1.clicked.connect(self.switch_p6ac1_clicked)
        self.switch_p6ac.clicked.connect(self.switch_p6ac_clicked)
        self.switch_p6ac2.clicked.connect(self.switch_p6ac2_clicked)

        self.switch_p5dc1.clicked.connect(self.switch_p5dc1_clicked)
        self.switch_p5dc.clicked.connect(self.switch_p5dc_clicked)
        self.switch_p5dc2.clicked.connect(self.switch_p5dc2_clicked)

        self.switch_p5ac1.clicked.connect(self.switch_p5ac1_clicked)
        self.switch_p5ac.clicked.connect(self.switch_p5ac_clicked)
        self.switch_p5ac2.clicked.connect(self.switch_p5ac2_clicked)

        self.switch_p4dc1.clicked.connect(self.switch_p4dc1_clicked)
        self.switch_p4dc.clicked.connect(self.switch_p4dc_clicked)
        self.switch_p4dc2.clicked.connect(self.switch_p4dc2_clicked)

        self.switch_p4ac1.clicked.connect(self.switch_p4ac1_clicked)
        self.switch_p4ac.clicked.connect(self.switch_p4ac_clicked)
        self.switch_p4ac2.clicked.connect(self.switch_p4ac2_clicked)

        self.switch_p3dc1.clicked.connect(self.switch_p3dc1_clicked)
        self.switch_p3dc.clicked.connect(self.switch_p3dc_clicked)
        self.switch_p3dc2.clicked.connect(self.switch_p3dc2_clicked)

        self.switch_p3ac1.clicked.connect(self.switch_p3ac1_clicked)
        self.switch_p3ac.clicked.connect(self.switch_p3ac_clicked)
        self.switch_p3ac2.clicked.connect(self.switch_p3ac2_clicked)


        #Initialisation (Due to error in pyuic5 when converting from .ui to.py)
        #setFrameShadow for GUI 
        #line for dc bus
        self.line_dc_8to3_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_dc_8to3_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_dc_8to3_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_dc_8to3_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_dc_8to3_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_dc_3to4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_dc_4to5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_dc_5to6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_dc_6to7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_dc_7to8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p3dc1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p3dc2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p4dc1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p4dc2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p5dc1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p5dc2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p6dc1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p6dc2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p7dc1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p7dc2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p8dc1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p8dc2.setFrameShadow(QtWidgets.QFrame.Plain)
        #line for ac bus       
        self.line_ac_8to3_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_ac_8to3_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_ac_8to3_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_ac_8to3_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_ac_8to3_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_ac_3to4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_ac_4to5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_ac_5to6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_ac_6to7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_ac_7to8.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p3ac1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p3ac2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p3ac1_togrid.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p4ac1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p4ac2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p5ac1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p5ac2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p6ac1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p6ac2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p7ac1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p7ac2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p8ac1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_p8ac2.setFrameShadow(QtWidgets.QFrame.Plain)

        #Timer for updating data on the GUI
        timer = QTimer(self)
        timer.timeout.connect(self.update_array)
        timer.timeout.connect(self.update_hybridgrid_gui)
        timer.start(200)


def main(argv):
    # create Qt application
    app = PyQt5.QtWidgets.QApplication(argv)

    # create main window
    wnd = Hybridgrid()  # classname


    #wnd = Initialisation()
    #wnd = QWidget()
    wnd.showMaximized()

    # Connect signal for app finish
    #app.connect(app, QtCore.SIGNAL("lastWindowClosed()"), app, QtCore.SLOT("quit()"))

    # Start the app up
    sys.exit(app.exec_())


if __name__ == "__main__":
    main(sys.argv)
    print(sys.argv)

'''    
if __name__ == "__main__":    
    app = QApplication(sys.argv)
    wnd = Hybridgrid()
    wnd.show()
    sys.exit(app.exec_())
'''
    
    

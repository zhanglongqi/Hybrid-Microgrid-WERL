__author__ = 'alvin'
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QSlider
import PyQt5.QtCore

from PyQt5.QtCore import QTimer

# Create a Modbus TCP/IP Client
from pymodbus3.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.0.10')

# import the class 'Ui_batt' from 'battUI.py'
from bidircontrolUI import Ui_bidirControl

# import the class 'bidir' from 'bidirpymodbus.py'
from bidirpymodbus import bidir
# import the class 'panel3' from 'panel3pymodbus.py'
# from panel3pymodbus import panel3

class Mainbidir(QWidget, Ui_bidirControl):
    def update_bidir_array(self):
        bidir.bidir_array(self)
        # panel3.p3_dc1_real_array(self)

    def update_bidir_gui(self):
        self.bidir_vdc.setText("" + str(self.BiDirCon_Vdc))

        self.bidir_frequency.setText("" + str(self.BiDirCon_Freq))

        self.bidir_real_power.setText("" + str(self.BiDirCon_RealPower))

        self.bidir_reactive_power.setText("" + str(self.BiDirCon_ReactPower))

        self.bidir_current_a.setText("" + str(self.BiDirCon_CurrentA))

        self.bidir_current_b.setText("" + str(self.BiDirCon_CurrentB))

        self.bidir_current_c.setText("" + str(self.BiDirCon_CurrentC))

        self.bidir_voltage_a.setText("" + str(self.BiDirCon_VoltageA)[:5])

        self.bidir_voltage_b.setText("" + str(self.BiDirCon_VoltageB)[:5])

        self.bidir_voltage_c.setText("" + str(self.BiDirCon_VoltageC)[:5])

        if self.tabWidget.currentIndex() == 0:
            # print("Bus Monitoring Mode")
            client.write_register(1031, 1)
        elif self.tabWidget.currentIndex() == 1:
            # print("Power Dispatching Mode")
            client.write_register(1031, 2)
            # ----------------------------------------------------------------------------#

    # Pushbutton Functionality
    def bidir_apply_pb_clicked(self):
        # check bus monitoring mode (1031 to 1) to  or power dispatching mode (1031 to 2)
        # apply pb (1030 to 2)
        # start pb (1030 to 1)
        # BiDirCon_Vdc_BM_Write to 1032
        # BiDirCon_iq_BM_Write  to 1034
        # BiDirCon_id_PD_Write  to 1036
        # BiDirCon_iq_PD_Write to 1038

        # bidir is in bus monitoring mode
        if self.tabWidget.currentIndex() == 0:
            BiDirCon_Vdc_BM_Write_Actual = self.vdc_ref_bus.text()
            # print(BiDirCon_Vdc_BM_Write_Actual)
            BiDirCon_Vdc_BM_Write = int((float(BiDirCon_Vdc_BM_Write_Actual) - 200) * 10)
            # print(BiDirCon_Vdc_BM_Write)
            # BiDirCon_iq_BM_Write = self.iq_ref_bus.text() * 100
            client.write_register(1032, int(
                BiDirCon_Vdc_BM_Write))  # Write to reg 970 - Bat_1_Ref_Current_Write_Unit


            # client.write_register(1034, int(BiDirCon_iq_BM_Write))  #Write to reg 970 - Bat_1_Ref_Current_Write_Unit
        # bidir is in power dispatching mode
        elif self.tabWidget.currentIndex() == 1:
            BiDirCon_id_PD_Write = self.id_ref_pow.text() * 100
            client.write_register(1036, int(BiDirCon_id_PD_Write))  # Write to reg 970 - Bat_1_Ref_Current_Write_Unit

            BiDirCon_iq_PD_Write = self.iq_ref_pow.text() * 100
            client.write_register(1038, int(BiDirCon_iq_PD_Write))  # Write to reg 970 - Bat_1_Ref_Current_Write_Unit

    def bidir_start_pb_clicked(self):

        # print(self.MPPT_3_Coil_11)

        if self.MPPT_3_Coil_11 == 1:
            client.write_register(951, 0)  # MPPT_3_CoilSet_Word_0=0
        else:
            client.write_registers(951, 1)  # MPPT_3_CoilSet_Word_0=1
        client.write_register(952, 1)  # MPPT_3_ Write_Indicator_1=1


        #     ------------------------------------------------------------     #

    def __init__(self):  # initialisation, passing parameter during the intial state

        QWidget.__init__(self)
        # set up User Interface (widgets, layout...)
        self.setupUi(self)

        # Event handlers
        self.bidir_apply_pb.clicked.connect(self.bidir_apply_pb_clicked)  # Bind the event handlers to button       

        self.bidir_start_pb.clicked.connect(self.bidir_start_pb_clicked)  # Bind the event handlers to button       

        # Set up initial condition
        # self.initial()
        # self.lead_batt_control_mode.setText("initial Constant Current")


        # Timer for updating gui data
        timer = QTimer(self)
        timer.timeout.connect(self.update_bidir_array)
        timer.timeout.connect(self.update_bidir_gui)
        timer.start(200)

        # self.WIDGET.clicked.connect(self.WIDGET_clicked)


def main():
    # create Qt application
    app = QApplication(sys.argv)

    # create main window
    wndbidir = Mainbidir()  # classname
    wndbidir.show()

    # Connect signal for app finish
    # app.connect(app, QtCore.SIGNAL("lastWindowClosed()"), app, QtCore.SLOT("quit()")

    # Start the app up
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

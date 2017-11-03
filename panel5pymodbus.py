# This panel 5 is connected to Lithium Ion Battery.
__author__ = 'alvin'

import time
import math

from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.0.10')


class panel5():
    def p5_ac1_real_array(self):
        # p5ac1list = client.read_holding_registers(10477, 49, unit=1)
        ##print("p5_ac1 Real Array: " +str(p5ac1list.registers))       #print 'p5ac1list' - 16bit register
        p5ac1list = client.read_holding_registers(5200, 49, unit=1)
        # print("p5_ac1 Real Array: " +str(p5ac1list.registers))

        # AC to Real Conversion for Panel
        # self.p5ac1_LN_Voltage = 0.1 * p5ac1list.registers[11]          #reg 5216
        # self.p5ac1_Current= 0.001 * p5ac1list.registers[12]            #reg 5218
        # self.p5ac1_TotalRealPower= 0.01 * p5ac1list.registers[4]       #reg 5206
        self.p5ac1_LN_Voltage = float(p5ac1list.registers[16])  # reg 3216
        self.p5ac1_Current = float(p5ac1list.registers[18])  # reg 3218
        self.p5ac1_TotalRealPower = float(p5ac1list.registers[6])

    def p5_ac2_real_array(self):
        # p5ac2list = client.read_holding_registers(10526, 49, unit=1)
        p5ac2list = client.read_holding_registers(5300, 49, unit=1)
        # print("p5_ac2 Real Array: " +str(p5ac2list.registers))       #print 'p5ac2list' - 16bit register
        self.p5ac2_LN_Voltage = float(p5ac2list.registers[16])

        # Panel5 dc1 RealArray (Lithium Ion Battery)

    def p5_dc1_real_array(self):
        p5dc1list = client.read_holding_registers(10575, 10, unit=1)
        # print("p5_dc1 Real Array: " +str(p5dc1list.registers))       #print 'p5dc1list' - 16bit register

        # DC to Real Conversion for Panel
        # Voltage
        if (p5dc1list.registers[1] & 256) == 0:
            self.p5dc1list_voltage = round(
                -(float(p5dc1list.registers[0])) * (10.0 ** (float(p5dc1list.registers[1]) - 3)), 2)
            # print('voltage for reg=0')
        else:
            self.p5dc1list_voltage = round(1 * p5dc1list.registers[0] * (10.0 ** (p5dc1list.registers[1] - 259)), 2)
            # print('voltage for reg /= 0')
        # print("p5_dc1 Voltage: " +str(self.p5dc1list_voltage))
        # Current
        if (p5dc1list.registers[3] & 256) == 0:
            self.p5dc1list_current = round((-p5dc1list.registers[2]) * (10.0 ** (p5dc1list.registers[3] - 3)), 2)
        else:
            self.p5dc1list_current = round(1 * p5dc1list.registers[2] * (10 ** (p5dc1list.registers[3] - 259)), 2)
            # print("p5_dc1 Current: " +str(self.p5dc1list_current))
        # Power
        if (p5dc1list.registers[5] & 256) == 0:
            self.p5dc1list_power = round((((p5dc1list.registers[4]) * (10.0 ** (p5dc1list.registers[5] - 3))) / 1000.0),
                                         2)
        else:
            self.p5dc1list_power = round(
                (((-1.0 * float(p5dc1list.registers[4])) * (10.0 ** (float(p5dc1list.registers[5] - 259)))) / 1000.0),
                2)
        # print("p5_dc1 Power: " +str(self.p5dc1list_power))
        # Positive Energy
        self.p5dc1list_PositiveEnergy = (65536.0 * float(p5dc1list.registers[6])) + (
        float(p5dc1list.registers[7]) / 100.0)
        # print("p5_dc1 Positive Energy: " +str(self.p5dc1list_PositiveEnergy))    #Convert float to str before print
        # Negative Energy
        self.p5dc1list_NegativeEnergy = (65536.0 * p5dc1list.registers[8]) + (p5dc1list.registers[9] / 100.0)
        # print("p5_dc1 Negative Energy: " +str(self.p5dc1list_NegativeEnergy))     #Convert float to str before print

        # -------Calculation of parameters----------------------------------------------------------------------------------------------
        # Lithium Ion Battery SOC
        lithiumsub = self.p5dc1list_PositiveEnergy - self.p5dc1list_NegativeEnergy
        ##print("lithiumsub: " +str(self.lithiumsub) )
        lithiumdiv = lithiumsub / 20.0
        ##print("lithiumdiv: " +str(self.lithiumdiv) )
        # lithiumadd = 0.4 + lithiumdiv
        lithiumadd = 0.2 + lithiumdiv
        ##print("lithiumadd: " +str(self.lithiumadd) )
        self.lithium_batt_soc = (lithiumadd * 100.0)
        # print("SOC: " + (str(self.lithium_batt_soc)) + "%")

    # ------------------------------------------------------------------------------------------------------------------------------#

    def p5_dc2_real_array(self):
        p5dc2list = client.read_holding_registers(10585, 10, unit=1)
        # print("p5_dc2 Real Array: " +str(p5dc2list.registers))       #print 'p5dc1list' - 16bit register

        # DC to Real Conversion for Panel
        # Voltage
        if (p5dc2list.registers[1] & 256) == 0:
            self.p5dc2list_voltage = round(
                -(float(p5dc2list.registers[0])) * (10.0 ** (float(p5dc2list.registers[1]) - 3)), 2)
            # print('voltage for reg=0')
        else:
            self.p5dc2list_voltage = round(1 * p5dc2list.registers[0] * (10.0 ** (p5dc2list.registers[1] - 259)), 2)
            # print('voltage for reg /= 0')
        # print("p5_dc2 Voltage: " +str(self.p5dc2list_voltage))
        # Current
        if (p5dc2list.registers[3] & 256) == 0:
            self.p5dc2list_current = round((-p5dc2list.registers[2]) * (10.0 ** (p5dc2list.registers[3] - 3)), 2)
        else:
            self.p5dc2list_current = round(1 * p5dc2list.registers[2] * (10 ** (p5dc2list.registers[3] - 259)), 2)
            # print("p5_dc2 Current: " +str(self.p5dc2list_current))
        # Power
        if (p5dc2list.registers[5] & 256) == 0:
            self.p5dc2list_power = round((((p5dc2list.registers[4]) * (10.0 ** (p5dc2list.registers[5] - 3))) / 1000.0),
                                         2)
        else:
            self.p5dc2list_power = round(
                (((-1.0 * float(p5dc2list.registers[4])) * (10.0 ** (float(p5dc2list.registers[5] - 259)))) / 1000.0),
                2)
        # print("p5_dc2 Power: " +str(self.p5dc2list_power))
        # Positive Energy
        self.p5dc2list_PositiveEnergy = (65536.0 * float(p5dc2list.registers[6])) + (
        float(p5dc2list.registers[7]) / 100.0)
        # print("p5_dc2 Positive Energy: " +str(self.p5dc2list_PositiveEnergy))    #Convert float to str before print
        # Negative Energy
        self.p5dc2list_NegativeEnergy = (65536.0 * p5dc2list.registers[8]) + (p5dc2list.registers[9] / 100.0)
        # print("p5_dc2 Negative Energy: " +str(self.p5dc2list_NegativeEnergy))     #Convert float to str before print

    def p5_switches_status(self):
        p5_switches_status_list = client.read_holding_registers(15004, 1, unit=1)
        # print("p5_switches_status_list: " +str(p5_switches_status_list.registers))
        self.p5_switches_status_reg = p5_switches_status_list.registers[0]

        if ((self.p5_switches_status_reg & 1) == 0):  # check for 1st bits
            self.p5_dc_light1 = 0
        elif ((self.p5_switches_status_reg & 1) == 2):
            self.p5_dc_light1 = 1

        if ((self.p5_switches_status_reg & 2) == 0):  # check for 2nd bits
            self.p5_dc_light2 = 0
        elif ((self.p5_switches_status_reg & 2) == 2):
            self.p5_dc_light2 = 1

        if ((self.p5_switches_status_reg & 4) == 0):  # check for 3rd bits
            self.p5_ac1_status = 0
        elif ((self.p5_switches_status_reg & 4) == 4):
            self.p5_ac1_status = 1

        if ((self.p5_switches_status_reg & 8) == 0):  # check for 4th bits
            self.p5_ac_status = 0
        elif ((self.p5_switches_status_reg & 8) == 8):
            self.p5_ac_status = 1

        if ((self.p5_switches_status_reg & 16) == 0):  # check for 5th bits
            self.p5_ac2_status = 0
        elif ((self.p5_switches_status_reg & 16) == 16):
            self.p5_ac2_status = 1

        if ((self.p5_switches_status_reg & 32) == 0):  # check for 6th bits
            self.p5_dc1_status = 0
        elif ((self.p5_switches_status_reg & 32) == 32):
            self.p5_dc1_status = 1

        if ((self.p5_switches_status_reg & 64) == 0):  # check for 7th bits
            self.p5_dc_status = 0
        elif ((self.p5_switches_status_reg & 64) == 64):
            self.p5_dc_status = 1

        if ((self.p5_switches_status_reg & 128) == 0):  # check for 8th bits
            self.p5_dc2_status = 0
        elif ((self.p5_switches_status_reg & 128) == 128):
            self.p5_dc2_status = 1

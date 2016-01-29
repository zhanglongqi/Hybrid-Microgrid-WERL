import time
import math
from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.0.10')


class panel8():
    def p8_ac1_real_array(self):
        p8ac1list = client.read_holding_registers(10834, 49, unit=1)
        ##print("p8_ac1 Real Array: " + str(p8ac1list.registers))  # print 'p8ac1list' - 16bit register
        p8ac1list = client.read_holding_registers(8200, 49, unit=1)
        ##print("p8_ac1 Real Array: " + str(p8ac1list.registers))

        # AC to Real Conversion for Panel
        # self.p8ac1_LN_Voltage = 0.1 * p8ac1list.registers[11]          #reg 8216
        # self.p8ac1_Current= 0.001 * p8ac1list.registers[12]            #reg 8218
        # self.p8ac1_TotalRealPower= 0.01 * p8ac1list.registers[4]       #reg 8206
        self.p8ac1_LN_Voltage = float(p8ac1list.registers[16])  # reg 3216
        self.p8ac1_Current = float(p8ac1list.registers[18])  # reg 3218
        self.p8ac1_TotalRealPower = float(p8ac1list.registers[6])

    def p8_ac2_real_array(self):
        # p8ac2list = client.read_holding_registers(10883, 49, unit=1)
        p8ac2list = client.read_holding_registers(8300, 49, unit=1)
        ##print("p8_ac2 Real Array: " + str(p8ac2list.registers))  #print 'p8ac2list' - 16bit register
        self.p8ac2_LN_Voltage = float(p8ac2list.registers[16])

    def p8_dc1_real_array(self):
        p8dc1list = client.read_holding_registers(10932, 10, unit=1)
        ##print("p8_dc1 Real Array: " + str(p8dc1list.registers))  # print 'p8dc1list' - 16bit register

        # DC to Real Conversion for Panel
        # Voltage
        if (p8dc1list.registers[1] & 256) == 0:
            self.p8dc1list_voltage = round(
                -(float(p8dc1list.registers[0])) * (10.0 ** (float(p8dc1list.registers[1]) - 3)), 2)
            ##print('voltage for reg=0')
        else:
            self.p8dc1list_voltage = round(1 * p8dc1list.registers[0] * (10.0 ** (p8dc1list.registers[1] - 259)), 2)
            ##print('voltage for reg /= 0')
        ##print("p8_dc1 Voltage: " + str(self.p8dc1list_voltage))
        # Current
        if (p8dc1list.registers[3] & 256) == 0:
            self.p8dc1list_current = round((-p8dc1list.registers[2]) * (10.0 ** (p8dc1list.registers[3] - 3)), 2)
        else:
            self.p8dc1list_current = round(1 * p8dc1list.registers[2] * (10 ** (p8dc1list.registers[3] - 259)), 2)
        ##print("p8_dc1 Current: " + str(self.p8dc1list_current))
        # Power
        if (p8dc1list.registers[5] & 256) == 0:
            self.p8dc1list_power = round(
                (((p8dc1list.registers[4]) * (10.0 ** (p8dc1list.registers[5] - 3))) / 1000.0), 2)
        else:
            self.p8dc1list_power = round(
                (((-1.0 * float(p8dc1list.registers[4])) * (10.0 ** (float(p8dc1list.registers[5] - 259)))) / 1000.0),
                2)
        ##print("p8_dc1 Power: " + str(self.p8dc1list_power))
        # Positive Energy
        self.p8dc1list_PositiveEnergy = (65536.0 * float(p8dc1list.registers[6])) + (
            float(p8dc1list.registers[7]) / 100.0)
        ##print("p8_dc1 Positive Energy: " + str(self.p8dc1list_PositiveEnergy))  #Convert float to str before print
        # Negative Energy
        self.p8dc1list_NegativeEnergy = (65536.0 * p8dc1list.registers[8]) + (p8dc1list.registers[9] / 100.0)
        ##print("p8_dc1 Negative Energy: " + str( self.p8dc1list_NegativeEnergy))  #Convert float to str before print        #Positive Energy
        self.p8dc1list_PositiveEnergy = (65536.0 * float(p8dc1list.registers[6])) + (
            float(p8dc1list.registers[7]) / 100.0)
        ##print("p8_dc1 Positive Energy: " + str(self.p8dc1list_PositiveEnergy))  #Convert float to str before print
        # Negative Energy
        self.p8dc1list_NegativeEnergy = (65536.0 * p8dc1list.registers[8]) + (p8dc1list.registers[9] / 100.0)
        ##print("p8_dc1 Negative Energy: " + str(self.p8dc1list_NegativeEnergy))  #Convert float to str before print

    def p8_dc2_real_array(self):
        p8dc2list = client.read_holding_registers(10942, 10, unit=1)
        ##print("p8_dc2 Real Array: " + str(p8dc2list.registers))  # print 'p8dc2list' - 16bit register

        # DC to Real Conversion for Panel
        # Voltage
        if p8dc2list.registers[1] == 0:
            self.p8dc2list_voltage = -(float(p8dc2list.registers[0])) * (10.0 ** (float(p8dc2list.registers[1]) - 3))
        else:
            self.p8dc2list_voltage = 1 * p8dc2list.registers[0] * (10 ** (p8dc2list.registers[1] - 259))
        ##print("p8_dc2 Voltage: " + str(self.p8dc2list_voltage))
        # Current
        if p8dc2list.registers[3] == 0:
            self.p8dc2list_current = (-p8dc2list.registers[2]) * (10.0 ** (p8dc2list.registers[3] - 3))
        else:
            self.p8dc2list_current = 1 * p8dc2list.registers[2] * (10 ** (p8dc2list.registers[3] - 259))
        ##print("p8_dc2 Current: " + str(self.p8dc2list_current))
        # Power
        if p8dc2list.registers[5] == 0:
            self.p8dc2list_power = ((p8dc2list.registers[4]) * (10.0 ** (p8dc2list.registers[5] - 3))) / 1000.0
        else:
            self.p8dc2list_power = ((-1.0 * float(p8dc2list.registers[4])) * (
                10.0 ** (float(p8dc2list.registers[5] - 259)))) / 1000.0
        ##print("p8_dc2 Power: " + str(self.p8dc2list_power))
        # Positive Energy
        self.p8dc2list_PositiveEnergy = (65536.0 * float(p8dc2list.registers[6])) + (
            float(p8dc2list.registers[7]) / 100.0)
        ##print("p8_dc2 Positive Energy: " + str(self.p8dc2list_PositiveEnergy))  #Convert float to str before print
        # Negative Energy
        self.p8dc2list_NegativeEnergy = (65536.0 * p8dc2list.registers[8]) + (p8dc2list.registers[9] / 100.0)
        ##print("p8_dc2 Negative Energy: " + str(self.p8dc2list_NegativeEnergy))  #Convert float to str before print

    def p8_switches_status(self):
        p8_switches_status_list = client.read_holding_registers(15007, 1, unit=1)
        ##print("p8_switches_status_list: " + str(p8_switches_status_list.registers))
        self.p8_switches_status_reg = p8_switches_status_list.registers[0]

        if ((self.p8_switches_status_reg & 1) == 0):  # check for 1st bits
            self.p8_dc_light1 = 0
        elif ((self.p8_switches_status_reg & 1) == 2):
            self.p8_dc_light1 = 1

        if ((self.p8_switches_status_reg & 2) == 0):  # check for 2nd bits
            self.p8_dc_light2 = 0
        elif ((self.p8_switches_status_reg & 2) == 2):
            self.p8_dc_light2 = 1

        if ((self.p8_switches_status_reg & 4) == 0):  # check for 3rd bits
            self.p8_ac1_status = 0
        elif ((self.p8_switches_status_reg & 4) == 4):
            self.p8_ac1_status = 1

        if ((self.p8_switches_status_reg & 8) == 0):  # check for 4th bits
            self.p8_ac_status = 0
        elif ((self.p8_switches_status_reg & 8) == 8):
            self.p8_ac_status = 1

        if ((self.p8_switches_status_reg & 16) == 0):  # check for 5th bits
            self.p8_ac2_status = 0
        elif ((self.p8_switches_status_reg & 16) == 16):
            self.p8_ac2_status = 1

        if ((self.p8_switches_status_reg & 32) == 0):  # check for 6th bits
            self.p8_dc1_status = 0
        elif ((self.p8_switches_status_reg & 32) == 32):
            self.p8_dc1_status = 1

        if ((self.p8_switches_status_reg & 64) == 0):  # check for 7th bits
            self.p8_dc_status = 0
        elif ((self.p8_switches_status_reg & 64) == 64):
            self.p8_dc_status = 1

        if ((self.p8_switches_status_reg & 128) == 0):  # check for 8th bits
            self.p8_dc2_status = 0
        elif ((self.p8_switches_status_reg & 128) == 128):
            self.p8_dc2_status = 1

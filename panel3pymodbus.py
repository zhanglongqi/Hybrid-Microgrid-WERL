import time
import math
from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.0.10')


class panel3():
    def p3_ac1_real_array(self):
        p3ac1list = client.read_holding_registers(10239, 49, unit=1)
        # print("p3_ac1 Real Array: " + str(p3ac1list.registers))  # print 'p3ac1list' - 16bit register
        # p3ac1list = client.read_holding_registers(3200, 49, unit=1)
        ##print("p3_ac1 Real Array: " +str(p3ac1list.registers)) 
        # AC to Real Conversion for Panel
        self.p3ac1_LN_Voltage = round(0.1 * p3ac1list.registers[11], 2)  # reg 3216
        self.p3ac1_Current = round(0.001 * p3ac1list.registers[12], 2)  # reg 3218
        self.p3ac1_TotalRealPower = round(0.01 * p3ac1list.registers[6], 2)  # reg 3206
        # self.p3ac1_LN_Voltage = round(float(p3ac1list.registers[16]),2)        #reg 3216
        # self.p3ac1_Current= round(float(p3ac1list.registers[18]) , 2)           #reg 3218
        # self.p3ac1_TotalRealPower= round(float(p3ac1list.registers[6]) , 2)

    def p3_ac2_real_array(self):
        p3ac2list = client.read_holding_registers(10288, 49, unit=1)
        # print("p3_ac2 Real Array: " + str(p3ac2list.registers))  # print 'p3ac2list' - 16bit register
        # p3ac2list = client.read_holding_registers(3300, 49, unit=1)
        ##print("p3_ac2 Real Array: " +str(p3ac2list.registers))       #print 'p3ac2list' - 16bit register 

        # AC to Real Conversion for Panel
        self.p3ac2_LN_Voltage = round(0.1 * p3ac2list.registers[11], 2)  # reg 3316
        self.p3ac2_Current = round(0.001 * p3ac2list.registers[12], 2)  # reg 3318
        self.p3ac2_TotalRealPower = round(0.01 * p3ac2list.registers[6], 2)  # reg 3306
        # self.p3ac2_LN_Voltage = float(p3ac2list.registers[16])          #reg 7216
        # self.p3ac2_Current= float(p3ac2list.registers[18])            #reg 7218
        # self.p3ac2_TotalRealPower= float(p3ac2list.registers[6])

    def p3_dc1_real_array(self):
        p3dc1list = client.read_holding_registers(10337, 10, unit=1)
        # print("p3_dc1 Real Array: " + str(p3dc1list.registers))  # print 'p3dc1list' - 16bit register

        # DC to Real Conversion for Panel
        # Voltage
        if (p3dc1list.registers[1] & 256) == 0:
            self.p3dc1list_voltage = round(
                -(float(p3dc1list.registers[0])) * (10.0 ** (float(p3dc1list.registers[1]) - 3)), 2)
            # print('voltage for reg=0')
        else:
            self.p3dc1list_voltage = round(1 * p3dc1list.registers[0] * (10.0 ** (p3dc1list.registers[1] - 259)), 2)
            # print('voltage for reg /= 0')
        # print("p3_dc1 Voltage: " + str(self.p3dc1list_voltage))
        # Current
        if (p3dc1list.registers[3] & 256) == 0:
            self.p3dc1list_current = round((-p3dc1list.registers[2]) * (10.0 ** (p3dc1list.registers[3] - 3)), 2)
        else:
            self.p3dc1list_current = round(1 * p3dc1list.registers[2] * (10 ** (p3dc1list.registers[3] - 259)), 2)
        # print("p3_dc1 Current: " + str(self.p3dc1list_current))
        # Power
        if (p3dc1list.registers[5] & 256) == 0:
            self.p3dc1list_power = round(
                (((p3dc1list.registers[4]) * (10.0 ** (p3dc1list.registers[5] - 3))) / 1000.0), 2)
        else:
            self.p3dc1list_power = round(
                (((-1.0 * float(p3dc1list.registers[4])) * (10.0 ** (float(p3dc1list.registers[5] - 259)))) / 1000.0),
                2)
        # print("p3_dc1 Power: " + str(self.p3dc1list_power))
        # Positive Energy
        self.p3dc1list_PositiveEnergy = (65536.0 * float(p3dc1list.registers[6])) + (
            float(p3dc1list.registers[7]) / 100.0)
        # print("p3_dc1 Positive Energy: " + str(self.p3dc1list_PositiveEnergy))  #Convert float to str before print
        # Negative Energy
        self.p3dc1list_NegativeEnergy = (65536.0 * p3dc1list.registers[8]) + (p3dc1list.registers[9] / 100.0)
        # print("p3_dc1 Negative Energy: " + str(self.p3dc1list_NegativeEnergy))  #Convert float to str before print        #Positive Energy
        self.p3dc1list_PositiveEnergy = (65536.0 * float(p3dc1list.registers[6])) + (
            float(p3dc1list.registers[7]) / 100.0)
        # print("p3_dc1 Positive Energy: " + str(self.p3dc1list_PositiveEnergy))  #Convert float to str before print
        # Negative Energy
        self.p3dc1list_NegativeEnergy = (65536.0 * p3dc1list.registers[8]) + (p3dc1list.registers[9] / 100.0)
        # print("p3_dc1 Negative Energy: " + str(self.p3dc1list_NegativeEnergy))  #Convert float to str before print

    def p3_dc2_real_array(self):
        p3dc2list = client.read_holding_registers(10347, 10, unit=1)
        # print("p3_dc2 Real Array: " + str(p3dc2list.registers))  # print 'p3dc2list' - 16bit register

        # DC to Real Conversion for Panel
        # Voltage
        if (p3dc2list.registers[1] & 256) == 0:
            self.p3dc2list_voltage = round(
                -(float(p3dc2list.registers[0])) * (10.0 ** (float(p3dc2list.registers[1]) - 3)), 2)
            # print('voltage for reg=0')
        else:
            self.p3dc2list_voltage = round(1 * p3dc2list.registers[0] * (10.0 ** (p3dc2list.registers[1] - 259)), 2)
            # print('voltage for reg /= 0')
        # print("p3_dc2 Voltage: " + str(self.p3dc2list_voltage))
        # Current
        if (p3dc2list.registers[3] & 256) == 0:
            self.p3dc2list_current = round((-p3dc2list.registers[2]) * (10.0 ** (p3dc2list.registers[3] - 3)), 2)
        else:
            self.p3dc2list_current = round(1 * p3dc2list.registers[2] * (10 ** (p3dc2list.registers[3] - 259)), 2)
        # print("p3_dc2 Current: " + str(self.p3dc2list_current))
        # Power
        if (p3dc2list.registers[5] & 256) == 0:
            self.p3dc2list_power = round(
                (((p3dc2list.registers[4]) * (10.0 ** (p3dc2list.registers[5] - 3))) / 1000.0), 2)
        else:
            self.p3dc2list_power = round(
                (((-1.0 * float(p3dc2list.registers[4])) * (10.0 ** (float(p3dc2list.registers[5] - 259)))) / 1000.0),
                2)
        # print("p3_dc2 Power: " + str(self.p3dc2list_power))
        # Positive Energy
        self.p3dc2list_PositiveEnergy = (65536.0 * float(p3dc2list.registers[6])) + (
            float(p3dc2list.registers[7]) / 100.0)
        # print("p3_dc2 Positive Energy: " + str(self.p3dc2list_PositiveEnergy))  #Convert float to str before print
        # Negative Energy
        self.p3dc2list_NegativeEnergy = (65536.0 * p3dc2list.registers[8]) + (p3dc2list.registers[9] / 100.0)
        # print("p3_dc2 Negative Energy: " + str(self.p3dc2list_NegativeEnergy))  #Convert float to str before print         #Positive Energy
        self.p3dc2list_PositiveEnergy = (65536.0 * float(p3dc2list.registers[6])) + (
            float(p3dc2list.registers[7]) / 100.0)
        # print("p3_dc2 Positive Energy: " + str(self.p3dc2list_PositiveEnergy))  #Convert float to str before print
        # Negative Energy
        self.p3dc2list_NegativeEnergy = (65536.0 * p3dc2list.registers[8]) + (p3dc2list.registers[9] / 100.0)
        # print("p3_dc2 Negative Energy: " + str(self.p3dc2list_NegativeEnergy))  #Convert float to str before print

    def p3_switches_status(self):
        p3_switches_status_list = client.read_holding_registers(15002, 1, unit=1)
        # print("p3_switches_status_list: " + str(p3_switches_status_list.registers))
        self.p3_switches_status_reg = p3_switches_status_list.registers[0]

        if ((self.p3_switches_status_reg & 1) == 0):  # check for 1st bits
            self.p3_dc_light1 = 0
        elif ((self.p3_switches_status_reg & 1) == 2):
            self.p3_dc_light1 = 1

        if ((self.p3_switches_status_reg & 2) == 0):  # check for 2nd bits
            self.p3_dc_light2 = 0
        elif ((self.p3_switches_status_reg & 2) == 2):
            self.p3_dc_light2 = 1

        if ((self.p3_switches_status_reg & 4) == 0):  # check for 3rd bits
            self.p3_ac1_status = 0
        elif ((self.p3_switches_status_reg & 4) == 4):
            self.p3_ac1_status = 1

        if ((self.p3_switches_status_reg & 8) == 0):  # check for 4th bits
            self.p3_ac_status = 0
        elif ((self.p3_switches_status_reg & 8) == 8):
            self.p3_ac_status = 1

        if ((self.p3_switches_status_reg & 16) == 0):  # check for 5th bits
            self.p3_ac2_status = 0
        elif ((self.p3_switches_status_reg & 16) == 16):
            self.p3_ac2_status = 1

        if ((self.p3_switches_status_reg & 32) == 0):  # check for 6th bits
            self.p3_dc1_status = 0
        elif ((self.p3_switches_status_reg & 32) == 32):
            self.p3_dc1_status = 1

        if ((self.p3_switches_status_reg & 64) == 0):  # check for 7th bits
            self.p3_dc_status = 0
        elif ((self.p3_switches_status_reg & 64) == 64):
            self.p3_dc_status = 1

        if (self.p3_switches_status_reg & 128) == 0:  # check for 8th bits
            self.p3_dc2_status = 0
        elif (self.p3_switches_status_reg & 128) == 128:
            self.p3_dc2_status = 1

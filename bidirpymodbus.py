import time
import math
from pymodbus.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.0.10')


class bidir():
    def bidir_array(self):
        bidirlist = client.read_holding_registers(10952, 13, unit=1)
        # print("Bi-Directional Array: " +str(bidirlist.registers))

        # BiDirCon_Query_On - First 8 bits of Register 0               # '>>' Binary Right Shift Operator
        self.BiDirCon_Query_On = bidirlist.registers[0] >> 8  # perform right shift by 8
        # print("BiDirCon_Query_On: " + str(self.BiDirCon_Query_On))

        # BiDirCon_Mode - Last 8 bits of Register 0                    # '<<' Binary Right Shift Operator
        self.BiDirCon_Mode = (bidirlist.registers[
                                  0] << 8) >> 8  # perform left shift by 8  then right shirt by 8
        # print("BiDirCon_Mode: " + str(self.BiDirCon_Mode))

        # BiDirCon_Vdc - Register 1
        self.BiDirCon_Vdc = round(bidirlist.registers[1] * 0.1, 2)

        # BiDirCon__Freq - Register 2
        self.BiDirCon_Freq = round(bidirlist.registers[2] * 0.01, 2)

        # BiDirCon_RealPower - Register 3
        if (bidirlist.registers[3] >> 8) >= 128:
            self.BiDirCon_RealPower = round(0.1 * (bidirlist.registers[3] - 128 * 256), 2)
        else:
            self.BiDirCon_RealPower = round(0.1 * (bidirlist.registers[3]), 2)

        # BiDirCon_ReactPower - Register 4
        if (bidirlist.registers[4] >> 8) >= 128:
            self.BiDirCon_ReactPower = round(0.1 * (bidirlist.registers[4] - 128 * 256), 2)
        else:
            self.BiDirCon_ReactPower = round(0.1 * (bidirlist.registers[3]), 2)

            # BiDirCon_CurrentA - Register 5
        if (bidirlist.registers[5] >> 8) >= 128:
            self.BiDirCon_CurrentA = round(0.01 * (bidirlist.registers[5] - 128 * 256), 2)
        else:
            self.BiDirCon_CurrentA = round(0.01 * (bidirlist.registers[5]), 2)

            # BiDirCon_CurrentB - Register 6
        if (bidirlist.registers[6] >> 8) >= 128:
            self.BiDirCon_CurrentB = round(0.01 * (bidirlist.registers[6] - 128 * 256), 2)
        else:
            self.BiDirCon_CurrentB = round(0.01 * (bidirlist.registers[6]), 2)

            # BiDirCon_CurrentC - Register 7
        if (bidirlist.registers[7] >> 8) >= 128:
            self.BiDirCon_CurrentC = round((0.01 * (bidirlist.registers[7] - 128 * 256)), 2)
        else:
            self.BiDirCon_CurrentC = round((0.01 * (bidirlist.registers[7])), 2)
            # self.BiDirCon_CurrentC_str = (self.BiDirCon_CurrentC)[:3]
        ##print("BiDirCon_CurrentC: " + str(self.BiDirCon_CurrentC_str))     

        # BiDirCon_VoltageA - Register 8
        self.BiDirCon_VoltageA = round(bidirlist.registers[8] * 0.1, 2)

        # BiDirCon_VoltageB - Register 9
        self.BiDirCon_VoltageB = round(bidirlist.registers[9] * 0.1, 2)

        # BiDirCon_VoltageC - Register 10
        self.BiDirCon_VoltageC = round(bidirlist.registers[10] * 0.1, 2)

        # BiDirCon_Status - Register 11
        self.BiDirCon_Status = round((bidirlist.registers[11] << 8) >> 8, 2)

        # BiDirCon_FaultType - Register 12
        self.BiDirCon_FaultType = round((bidirlist.registers[12] << 8) >> 8, 2)

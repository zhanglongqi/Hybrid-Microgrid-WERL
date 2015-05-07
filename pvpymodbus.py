import time
import math
from pymodbus3.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.0.10')


class pv():
    def pv2_array(self):
        pv2list = client.read_holding_registers(11025, 20, unit=1)
        #print("PV2 Array: " +str(pv2list.registers))
    
        #PV2_V1_R - Register 4
        self.PV2_V1_R = pv2list.registers[4]
        
        #PV2_V1 - Register 5
        self.PV2_V1 = pv2list.registers[5]
        
        #PV2_V2_R - Register 6
        self.PV2_V2_R = pv2list.registers[6]
        
        #PV2_V2 - Register 7
        self.PV2_V2 = pv2list.registers[7]
        
        #PV2_C1_R - Register 8
        self.PV2_C1_R = pv2list.registers[8]
        
        #PV2_C1 - Register 9
        self.PV2_C1 = pv2list.registers[9]
        
        #PV2_C2_R - Register 10
        self.PV2_C2_R = pv2list.registers[10]
        
        #PV2_C2 - Register 11
        self.PV2_C2 = pv2list.registers[11]
        
        #PV2_Coils_RW - Register 12
        self.PV2_Coils_RW = pv2list.registers[12]
        
        #PV2_Coils_R - Register 13
        self.PV2_Coils_R = pv2list.registers[13]
        
        #PV2_V1_R - Register 14
        
        
        #PV2_V1_R - Register 15
        
        
        #PV2_V1_R - Register 16
        
        
        
        #PV2_Min_V - Register 17
        self.PV2_Min_V = pv2list.registers[17]
        
        #PV2_Min_I - Register 18
        self.PV2_Min_I = pv2list.registers[18]
        
        #PV2_Bus_V - Register 19
        self.PV2_Bus_V = pv2list.registers[19]
        
        #Read coils status from registers, from PV2_Coils_RW and PV2_Coils_R
        if ((self.PV2_Coils_RW & 2) == 0):    #check for 2th bits in PV2_Coils_RW(Register 11037) - MPPT_2_Coil_1 
            self.MPPT_2_Coil_1 = 0
        elif ((self.PV2_Coils_RW & 2) == 2):
            self.MPPT_2_Coil_1 = 1
        
        if ((self.PV2_Coils_R & 8) == 0):    #check for 4th bits in PV2_Coils_R- Register 11038, coil 3 - MPPT_2_Coil_11
            self.MPPT_2_Coil_11 = 0
        elif ((self.PV2_Coils_R & 8) == 8):
            self.MPPT_2_Coil_11 = 1
            
        if ((self.PV2_Coils_R & 128) == 0):    #check for 8th bits in PV2_Coils_R- Register 11038, coil 7 - MPPT_2_Coil_15
            self.MPPT_2_Coil_15 = 0
        elif ((self.PV2_Coils_R & 128) == 128):
            self.MPPT_2_Coil_15 = 1
         
        if ((self.PV2_Coils_R & 256) == 0):    #check for 9th bits in PV2_Coils_R- Register 11038, coil 8 - MPPT_2_Coil_16
            self.MPPT_2_Coil_16 = 0
        elif ((self.PV2_Coils_R & 256) == 256):
            self.MPPT_2_Coil_16 = 1
            
    def pv3_array(self):
        pv3list = client.read_holding_registers(11045, 20, unit=1)
        #print("PV1 Array: " +str(pv3list.registers))
        
        #PV3_V1_R - Register 4
        self.PV3_V1_R = pv3list.registers[4]
        
        #PV3_V1 - Register 5
        self.PV3_V1 = pv3list.registers[5]
        
        #PV3_V2_R - Register 6
        self.PV3_V2_R = pv3list.registers[6]
        
        #PV3_V2 - Register 7
        self.PV3_V2 = pv3list.registers[7]
        
        #PV3_C1_R - Register 8
        self.PV3_C1_R = pv3list.registers[8]
        
        #PV3_C1 - Register 9
        self.PV3_C1 = pv3list.registers[9]
        
        #PV3_C2_R - Register 10
        self.PV3_C2_R = pv3list.registers[10]
        
        #PV3_C2 - Register 11
        self.PV3_C2 = pv3list.registers[11]
        
        #PV3_Coils_RW - Register 12
        self.PV3_Coils_RW = pv3list.registers[12]
        
        #PV3_Coils_R - Register 13
        self.PV3_Coils_R = pv3list.registers[13]
        
        #PV3_V1_R - Register 14
        #PV3_V1_R - Register 15
        #PV3_V1_R - Register 16
        
        #PV3_Min_V - Register 17
        self.PV3_Min_V = pv3list.registers[17]
        
        #PV3_Min_I - Register 18
        self.PV3_Min_I = pv3list.registers[18]
        
        #PV3_Bus_V - Register 19
        self.PV3_Bus_V = pv3list.registers[19]
        
        #Read coils status from registers, from PV2_Coils_RW and PV2_Coils_R
        if ((self.PV3_Coils_RW & 2) == 0):    #check for 2th bits in PV3_Coils_RW(Register 11057) - MPPT_3_Coil_1
            self.MPPT_3_Coil_1 = 0
        elif ((self.Battr1_Coils_RW & 2) == 2):
            self.MPPT_3_Coil_1 = 1
        
        if ((self.PV3_Coils_R & 8) == 0):    #check for 4th bits in PV3_Coils_R- Register 11058 - MPPT_3_Coil_11
            self.MPPT_3_Coil_11 = 0
        elif ((self.PV3_Coils_R & 8) == 8):
            self.MPPT_3_Coil_11 = 1
        
        if ((self.PV3_Coils_R & 128) == 0):    #check for 4th bits in PV3_Coils_R- Register 11058, coil 7 - MPPT_3_Coil_15
            self.MPPT_3_Coil_15 = 0
        elif ((self.PV3_Coils_R & 128) == 128):
            self.MPPT_3_Coil_15 = 1
            
        if ((self.PV3_Coils_R & 256) == 0):    #check for 9th bits in PV3_Coils_R- Register 11058, coil 8 - MPPT_2_Coil_16
            self.MPPT_3_Coil_16 = 0
        elif ((self.PV3_Coils_R & 256) == 256):
            self.MPPT_3_Coil_16 = 1
            
        

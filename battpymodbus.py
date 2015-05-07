#This file extract all the data relevant to Lithium Ion Battery/Lead Acid Battery by modbus TCP/IP.
__author__ = 'alvin'

import time
import math
from pymodbus3.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.0.10')


class battery():    
    def battery1_inarray(self):
        #Lithium Ion Battery 1 Read Array  - Register %MW10965:20
        lithiumlist = client.read_holding_registers(10965, 20, unit=1)  #read_holding_registers(address, count=1, **kwargs)
        #print("Lithium Array: " +str(lithiumlist.registers))
        
        #Battr1_V1_R - Register 4
        self.Battr1_V1_R = lithiumlist.registers[4]
        
        #Batt1_V1 - Register 5
        self.Batt1_V1 = lithiumlist.registers[5]
        
        #Battr1_V2_R - Register 6
        self.Battr1_V2_R = lithiumlist.registers[6]
        
        #Battr1_V2 - Register 7
        self.Battr1_V2 = lithiumlist.registers[7]
        
        #Battr1_C1_R - Register 8
        self.Battr1_C1_R = lithiumlist.registers[8]
        
        #Battr1_C1 - Register 9
        self.Battr1_C1 = lithiumlist.registers[9]
        
        #Battr1_Coils_RW - Register 10
        self.Battr1_Coils_RW = lithiumlist.registers[10]
        #print("Batt1_Coils_RW: " + str(self.Battr1_Coils_RW))
        
        #Battr1_Coils_R - Register 11
        self.Battr1_Coils_R = lithiumlist.registers[11]
        #print("Batt1_Coils_R: " + str(self.Battr1_Coils_R))
                       
        #Battr1_Ref_Zero_C - Register 12
        self.Battr1_Ref_Zero_C = lithiumlist.registers[12]
        #print("Battr1_Ref_Zero_C: " + str(self.Battr1_Ref_Zero_C))
        
        #Battr1_Full_Chg_C - Register 13
        self.Battr1_Full_Chg_C = lithiumlist.registers[13]
        #print("Battr1_Full_Chg_C: " + str(self.Battr1_Full_Chg_C))
        
        #Battr1_Hour - Register 14
        self.Battr1_Hour = lithiumlist.registers[14]
        #print("Battr1_Hour: " + str(self.Battr1_Hour))
        
        #Battr1_Min - Register 15
        self.Battr1_Min = lithiumlist.registers[15]
        #print("Battr1_Min: " + str(self.Battr1_Min))
        
        #Battr1_Sec - Register 16            
        self.Battr1_Sec = lithiumlist.registers[16]
        #print("Battr1_Sec: " + str(self.Battr1_Sec))
                       
        #Battr1_Ref_V - Register 17
        self.Battr1_Ref_V=lithiumlist.registers[17]
        #print("Battr1_Ref_V: " +str(self.Battr1_Ref_V))          
        self.Bat_1_Ref_Voltage_Read_SIGNED = round(self.Battr1_Ref_V /100, 2)
        #print("Bat_1_Ref_Voltage_Read_SIGNED: " +str(self.Bat_1_Ref_Voltage_Read_SIGNED)) 
        
        #Battr1_Ref_I - Register 18  
        self.Battr1_Ref_I=lithiumlist.registers[18]
        #print("Batt1_Ref_I: " +str(self.Battr1_Ref_I))  
        self.Bat_1_Ref_Current_Read_SIGNED = round(self.Battr1_Ref_I - 5000, 2)
        #print("Bat_1_Ref_Current_Read_SIGNED: " +str(self.Bat_1_Ref_Current_Read_SIGNED))
        
        #Battr1_Bus_V - Register 19
        self.Battr1_Bus_V=lithiumlist.registers[19]      
        #print("Batt1_Bus_V: " +str(self.Battr1_Bus_V))                                              
        self.Bat_1_Bus_Voltage_Read_SIGNED = self.Battr1_Bus_V /100
        #print("Bat_1_Ref_Voltage_Read_SIGNED: " +str(self.Bat_1_Bus_Voltage_Read_SIGNED)) 
        
        #Read coils status from registers, from Battr1_Coils_RW and Battr1_Coils_R                
        if ((self.Battr1_Coils_RW & 2) == 0):    #check for 2th bits in Battr1_Coils_RW(Register 10975) - Bat_1_Coil_1 
            self.Bat_1_Coil_1 = 0
        elif ((self.Battr1_Coils_RW & 2) == 2):
            self.Bat_1_Coil_1 = 1
        
        if ((self.Battr1_Coils_R & 8) == 0):     #check for 4th bits in Battr1_Coils_R - Register 10976, coil 3 - Bat_1_Coil_11
            self.Bat_1_Coil_11 = 0
        elif ((self.Battr1_Coils_R & 8) == 8):
            self.Bat_1_Coil_11 = 1

        if ((self.Battr1_Coils_R & 16) == 0):     #check for 5th bits in Battr1_Coils_R- Register 10976, coil 4 - Bat_1_Coil_12
            self.Bat_1_Coil_12 = 0
        elif ((self.Battr1_Coils_R & 16) == 16):
            self.Bat_1_Coil_12 = 1
        
        if ((self.Battr1_Coils_R & 32) == 0):     #check for 6th bits in Battr1_Coils_R- Register 10976, coil 5 - Bat_1_Coil_13
            self.Bat_1_Coil_13 = 0
        elif ((self.Battr1_Coils_R & 32) == 32):
            self.Bat_1_Coil_13 = 1
                    
        if ((self.Battr1_Coils_R & 64) == 0):     #check for 7th bits in Battr1_Coils_R- Register 10976, coil 6 - Bat_1_Coil_14
            self.Bat_1_Coil_14 = 0
        elif ((self.Battr1_Coils_R & 64) == 64):
            self.Bat_1_Coil_14 = 1
          
        if ((self.Battr1_Coils_R & 128) == 0):     #check for 8th bits in Battr1_Coils_R- Register 10976, coil 7 - Bat_Coil_15
            self.Bat_1_Coil_15 = 0
        elif ((self.Battr1_Coils_R & 128) == 128):
            self.Bat_1_Coil_15 = 1          

        if ((self.Battr1_Coils_R & 2048) == 0):     #check for 8th bits in Battr1_Coils_R- Register 10976, coil 7 - Bat_Coil_19
            self.Bat_1_Coil_19 = 0
        elif ((self.Battr1_Coils_R & 2048) == 2048):
            self.Bat_1_Coil_19 = 1
            
'''       
#-------------------------------------------------------------------------------------------------------------------------        
    #Panel5 DC1 RealArray (Lithium Ion Battery)      
    def panel5_dc1_real_array(self):               
        p5dc1list = client.read_holding_registers(10575, 10, unit=1)
        #print("P5_DC1 Real Array: " +str(p5dc1list.registers))       #print 'p5dc1list' - 16bit register
        
        #Lithium Ion Battery Voltage
        if p5dc1list.registers[1] == 0:
            self.p5dc1list_voltage = -(float(p5dc1list.registers[0])) * (10.0** (float(p5dc1list.registers[1])-3))
        else:
            self.p5dc1list_voltage = 1*p5dc1list.registers[0] * (10**(p5dc1list.registers[1]-259))   
        #print("Lithium Battery Panel 5_DC1 Voltage: " +str(self.p5dc1list_voltage))       
       
        #Lithium Ion Battery Current
        if p5dc1list.registers[3] == 0:
            self.p5dc1list_current = (-p5dc1list.registers[2]) * (10.0** (p5dc1list.registers[3]-3))
        else:
            self.p5dc1list_current = 1*p5dc1list.registers[2] * (10**(p5dc1list.registers[3]-259))    
        #print("Lithium Battery Panel 5_DC1 Current: " +str(self.p5dc1list_current))
    
        #Lithium Ion Battery Power
        if p5dc1list.registers[5] == 0:
            self.p5dc1list_power = ( (p5dc1list.registers[4]) * (10.0** (p5dc1list.registers[5]-3)) )/1000.0            
        else:
            self.p5dc1list_power = ( (-1.0*float(p5dc1list.registers[4])) * (10.0**(float(p5dc1list.registers[5]-259))) )/1000.0
        #print("Lithium Battery Panel 5_DC1 Power: " +str(self.p5dc1list_power))
            
        #Lithium Ion Battery Positive Energy
        self.p5dc1list_PositiveEnergy = (65536.0*float(p5dc1list.registers[6])) + (float(p5dc1list.registers[7])/100.0)
        #print("Lithium Battery Panel 5_DC1 Positive Energy: " +str(self.p5dc1list_PositiveEnergy))    #Convert float to str before print
       
        #Lithium Ion Battery Negative Energy
        self.p5dc1list_NegativeEnergy = (65536.0*p5dc1list.registers[8]) + (p5dc1list.registers[9]/100.0)
        #print("Lithium Battery Panel 5_DC1 Negative Energy: " +str(self.p5dc1list_NegativeEnergy))     #Convert float to str before print
            
        #Lithium Ion Battery SOC   
        lithiumsub = self.p5dc1list_PositiveEnergy - self.p5dc1list_NegativeEnergy
        lithiumdiv = lithiumsub/ 20.0
        lithiumadd = 0.4 + lithiumdiv 
        self.lithium_batt_soc = lithiumadd * 100.0
        #print("SOC: " +str(self.lithium_batt_soc) + "%")
#-------------------------------------------------------------------------------------------------------------------------#
'''
'''      
def battery2_inarray(self):
    #Lead Acid Battery 2 Read Array  - Register %MW10965:20
        leadacid_list = client.read_holding_registers(10985, 20, unit=1)  #read_holding_registers(address, count=1, **kwargs)
        print ("Lead Acid Array: " +str(leadacid_list.registers))
        
        #Battr2_V1_R - Register 4
        self.Battr2_V1_R = leadacid_list.registers[4]
        
        #Batt2_V1 - Register 5
        self.Batt2_V1 = leadacid_list.registers[5]
        
        #Battr2_V2_R - Register 6
        self.Battr2_V2_R = leadacid_list.registers[6]
        
        #Battr2_V2 - Register 7
        self.Battr2_V2 = leadacid_list.registers[7]
        
        #Battr2_C1_R - Register 8
        self.Battr2_C1_R = leadacid_list.registers[8]
        
        #Battr2_C1 - Register 9
        self.Battr2_C1 = leadacid_list.registers[9]
        
        #Battr2_Coils_RW - Register 10
        self.Battr2_Coils_RW = leadacid_list.registers[10]
        #print("Batt2_Coils_RW: " + str(self.Battr2_Coils_RW))
        
        #Battr2_Coils_R - Register 11
        self.Battr2_Coils_R = leadacid_list.registers[11]
        #print("Batt2_Coils_R: " + str(self.Battr2_Coils_R))
                       
        #Battr2_Ref_Zero_C - Register 12
        #Battr2_Full_Chg_C - Register 13
        #Battr2_Hour - Register 14
        #Battr2_Min - Register 15
        #Battr2_Sec - Register 16             
                       
        #Battr2_Ref_V - Register 17
        self.Battr2_Ref_V=leadacid_list.registers[17]
        #print("Battr2_Ref_V: " +str(self.Battr2_Ref_V))          
        self.Bat_2_Ref_Voltage_Read_SIGNED = self.Battr2_Ref_V /100
        #print("Bat_2_Ref_Voltage_Read_SIGNED: " +str(self.Bat_2_Ref_Voltage_Read_SIGNED)) 
        
        #Battr2_Ref_I - Register 18  
        self.Battr2_Ref_I=leadacid_list.registers[18]
        #print("Batt2_Ref_I: " +str(self.Battr2_Ref_I))  
        self.Bat_1_Ref_Current_Read_SIGNED = self.Battr2_Ref_I - 5000
        #print("Bat_2_Ref_Current_Read_SIGNED: " +str(self.Bat_2_Ref_Current_Read_SIGNED))
        
        #Battr2_Bus_V - Register 19
        self.Battr2_Bus_V=leadacid_list.registers[19]      
        #print("Batt2_Bus_V: " +str(self.Battr2_Bus_V))                                              
        self.Bat_2_Bus_Voltage_Read_SIGNED = self.Battr2_Bus_V /100
        #print("Bat_2_Ref_Voltage_Read_SIGNED: " +str(self.Bat_2_Bus_Voltage_Read_SIGNED)) 
        
        #Read coils status from registers, from Battr2_Coils_RW and Battr1_Coils_R                
        if ((self.Battr2_Coils_RW & 2) == 0):    #check for 2th bits in Battr2_Coils_RW(Register 10975) - Battr2_Coils_1 
            self.Battr2_Coils_1 = 0
        elif ((self.Battr2_Coils_RW & 2) == 2):
            self.Battr2_Coils_1 = 1
        
        if ((self.Battr2_Coils_R & 8) == 0):    #check for Battr1_Coils_11, 4th bits in Battr1_Coils_R - Register 10976
            self.Battr2_Coils_11 = 0
        elif ((self.Battr2_Coils_R & 8) == 8):
            self.Battr2_Coils_11 = 1
        
    #Panel7 DC1 RealArray (Lithium Ion Battery)      
    def panel7_dc1_real_array(self):               
        p7dc1list = client.read_holding_registers(10813, 10, unit=1)
        #print("P7_DC1 Real Array: " +str(p7dc1list.registers))       #print 'p7dc1list' - 16bit register
        
        #Lithium Ion Battery Voltage
        if p7dc1list.registers[1] == 0:
            self.p7dc1list_voltage = -(float(p7dc1list.registers[0])) * (10.0** (float(p7dc1list.registers[1])-3))
        else:
            self.p7dc1list_voltage = 1*p7dc1list.registers[0] * (10**(p7dc1list.registers[1]-259))   
        #print("Lithium Battery Panel 7_DC1 Voltage: " +str(self.p7dc1list_voltage))       
       
        #Lithium Ion Battery Current
        if p7dc1list.registers[3] == 0:
            self.p7dc1list_current = (-p7dc1list.registers[2]) * (10.0** (p7dc1list.registers[3]-3))
        else:
            self.p7dc1list_current = 1*p7dc1list.registers[2] * (10**(p7dc1list.registers[3]-259))    
        #print("Lithium Battery Panel 7_DC1 Current: " +str(self.p7dc1list_current))
    
        #Lithium Ion Battery Power
        if p7dc1list.registers[5] == 0:
            self.p7dc1list_power = ( (p7dc1list.registers[4]) * (10.0** (p7dc1list.registers[5]-3)) )/1000.0            
        else:
            self.p7dc1list_power = ( (-1.0*float(p7dc1list.registers[4])) * (10.0**(float(p7dc1list.registers[5]-259))) )/1000.0
        #print("Lithium Battery Panel 7_DC1 Power: " +str(self.p7dc1list_power))
            
        #Lithium Ion Battery Positive Energy
        self.p7dc1list_PositiveEnerygy = (65536.0*float(p7dc1list.registers[6])) + (float(p7dc1list.registers[7])/100.0)
        #print("Lithium Battery Panel 5_DC1 Positive Energy: " +str(self.p5dc1list_PositiveEnerygy))    #Convert float to str before print
       
        #Lithium Ion Battery Negative Energy
        self.p7dc1list_NegativeEnerygy = (65536.0*p7dc1list.registers[8]) + (p7dc1list.registers[9]/100.0)
        #print("Lithium Battery Panel 7_DC1 Negative Energy: " +str(self.p7dc1list_NegativeEnerygy))     #Convert float to str before print
            
        #Lithium Ion Battery SOC   
        lithiumsub = self.p7dc1list_PositiveEnerygy - self.p7dc1list_NegativeEnerygy
        lithiumdiv = lithiumsub/ 20.0
        lithiumadd = 0.4 + lithiumdiv 
        self.lithium_batt_soc = lithiumadd * 100.0
        #print("SOC: " +str(self.lithium_batt_soc) + "%")
       
'''                
#--------------------------------------------------------------------------------------------------------------------------------------   
  
#testing program to run this program individually
#j=2          #loop of 2 times
#while j:   
#while True:    #infinite loop      
#    lithiumbatt.lithium_array() 
#    lithiumbatt.panel5_dc1_real_array()
#    time.sleep(2)       #Delay of 2 sec, ie 2 sec update

'''
Program in the lab computer (Unity Pro XL - DC_To_Real

IF InArray[1].8=0 THEN Voltage:=-INT_TO_REAL(InArray[0])*EXPT_REAL_INT(10.0, Inarray[1]-3);
ELSE Voltage:=1.0*INT_TO_REAL(InArray[0])*EXPT_REAL_INT(10.0,Inarray[1]-259);
END_IF;
OutArray[0]:=Voltage

'''

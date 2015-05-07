import time
import math
from pymodbus3.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.0.10')

class panel4():        
    def p4_ac1_real_array(self):               
        #p4ac1list = client.read_holding_registers(10358, 49, unit=1)
        ##print("p4_ac1 Real Array: " +str(p4ac1list.registers))       #print 'p4ac1list' - 16bit register
        p4ac1list = client.read_holding_registers(4200, 49, unit=1)
        #print("p4_ac1 Real Array: " +str(p4ac1list.registers)) 

        #AC to Real Conversion for Panel 
        #self.p4ac1_LN_Voltage = 0.1 * p4ac1list.registers[11]          #reg 4216
        #self.p4ac1_Current= 0.001 * p4ac1list.registers[12]            #reg 4218
        #self.p4ac1_TotalRealPower= 0.01 * p4ac1list.registers[4]       #reg 4206
        self.p4ac1_LN_Voltage = float(p4ac1list.registers[16])        #reg 3216
        self.p4ac1_Current= float(p4ac1list.registers[18])            #reg 3218
        self.p4ac1_TotalRealPower= float(p4ac1list.registers[6])  
            
    def p4_ac2_real_array(self):               
        #p4ac2list = client.read_holding_registers(10407, 49, unit=1)
        p4ac2list = client.read_holding_registers(4300, 49, unit=1)
        #print("p4_ac2 Real Array: " +str(p4ac2list.registers))       #print 'p4ac2list' - 16bit register
        
        self.p4ac2_LL_Voltage = float(p4ac2list.registers[14])  
        self.p4ac2_LN_Voltage = float(p4ac2list.registers[16])                  
         
    def p4_dc1_real_array(self):               
        p4dc1list = client.read_holding_registers(10456, 10, unit=1)
        #print("p4_dc1 Real Array: " +str(p4dc1list.registers))       #print 'p4dc1list' - 16bit register
        
         #DC to Real Conversion for Panel
        #Voltage
        if (p4dc1list.registers[1] & 256) == 0:
            self.p4dc1list_voltage = round(-(float(p4dc1list.registers[0])) * (10.0** (float(p4dc1list.registers[1])-3)), 2)
            #print('voltage for reg=0')
        else:
            self.p4dc1list_voltage = round(1*p4dc1list.registers[0] * (10.0**(p4dc1list.registers[1]-259)), 2)   
            #print('voltage for reg /= 0')
        #print("p4_dc1 Voltage: " +str(self.p4dc1list_voltage))              
        #Current
        if (p4dc1list.registers[3] & 256) == 0:
            self.p4dc1list_current = round((-p4dc1list.registers[2]) * (10.0** (p4dc1list.registers[3]-3)), 2)
        else:
            self.p4dc1list_current = round(1*p4dc1list.registers[2] * (10**(p4dc1list.registers[3]-259)), 2)    
        #print("p4_dc1 Current: " +str(self.p4dc1list_current))    
        #Power
        if (p4dc1list.registers[5] & 256) == 0:
            self.p4dc1list_power = round((((p4dc1list.registers[4]) * (10.0** (p4dc1list.registers[5]-3)) )/1000.0 ), 2)           
        else:
            self.p4dc1list_power = round((((-1.0*float(p4dc1list.registers[4])) * (10.0**(float(p4dc1list.registers[5]-259))) )/1000.0), 2)
        #print("p4_dc1 Power: " +str(self.p4dc1list_power))            
        #Positive Energy
        self.p4dc1list_PositiveEnergy = (65536.0*float(p4dc1list.registers[6])) + (float(p4dc1list.registers[7])/100.0)
        #print("p4_dc1 Positive Energy: " +str(self.p4dc1list_PositiveEnergy))    #Convert float to str before print       
        #Negative Energy
        self.p4dc1list_NegativeEnergy = (65536.0*p4dc1list.registers[8]) + (p4dc1list.registers[9]/100.0)
        #print("p4_dc1 Negative Energy: " +str(self.p4dc1list_NegativeEnergy))     #Convert float to str before print        
        #Positive Energy
        self.p4dc1list_PositiveEnergy = (65536.0*float(p4dc1list.registers[6])) + (float(p4dc1list.registers[7])/100.0)
        #print("p4_dc1 Positive Energy: " +str(self.p4dc1list_PositiveEnergy))    #Convert float to str before print       
        #Negative Energy
        self.p4dc1list_NegativeEnergy = (65536.0*p4dc1list.registers[8]) + (p4dc1list.registers[9]/100.0)
        #print("p4_dc1 Negative Energy: " +str(self.p4dc1list_NegativeEnergy))     #Convert float to str before print
            
        
    def p4_dc2_real_array(self):               
        p4dc2list = client.read_holding_registers(10466, 10, unit=1)
        #print("p4_dc2 Real Array: " +str(p4dc2list.registers))       #print 'p4dc2list' - 16bit register

        #DC to Real Conversion for Panel
        #Voltage
        if p4dc2list.registers[1] == 0:
            self.p4dc2list_voltage = -(float(p4dc2list.registers[0])) * (10.0** (float(p4dc2list.registers[1])-3))
        else:
            self.p4dc2list_voltage = 1*p4dc2list.registers[0] * (10**(p4dc2list.registers[1]-259))   
        #print("p4_dc2 Voltage: " +str(self.p4dc2list_voltage))              
        #Current
        if p4dc2list.registers[3] == 0:
            self.p4dc2list_current = (-p4dc2list.registers[2]) * (10.0** (p4dc2list.registers[3]-3))
        else:
            self.p4dc2list_current = 1*p4dc2list.registers[2] * (10**(p4dc2list.registers[3]-259))    
        #print("p4_dc2 Current: " +str(self.p4dc2list_current))    
        #Power
        if p4dc2list.registers[5] == 0:
            self.p4dc2list_power = ( (p4dc2list.registers[4]) * (10.0** (p4dc2list.registers[5]-3)) )/1000.0            
        else:
            self.p4dc2list_power = ( (-1.0*float(p4dc2list.registers[4])) * (10.0**(float(p4dc2list.registers[5]-259))) )/1000.0
        #print("p4_dc2 Power: " +str(self.p4dc2list_power))            
        #Positive Energy
        self.p4dc2list_PositiveEnergy = (65536.0*float(p4dc2list.registers[6])) + (float(p4dc2list.registers[7])/100.0)
        #print("p4_dc2 Positive Energy: " +str(self.p4dc2list_PositiveEnergy))    #Convert float to str before print       
        #Negative Energy
        self.p4dc2list_NegativeEnergy = (65536.0*p4dc2list.registers[8]) + (p4dc2list.registers[9]/100.0)
        #print("p4_dc2 Negative Energy: " +str(self.p4dc2list_NegativeEnergy))     #Convert float to str before print
            
        

    def p4_switches_status(self):               
        p4_switches_status_list = client.read_holding_registers(15003, 1, unit=1)
        #print("p4_switches_status_list: " +str(p4_switches_status_list.registers))  
        self.p4_switches_status_reg = p4_switches_status_list.registers[0]
        
        if ((self.p4_switches_status_reg & 1) == 0):    #check for 1st bits 
            self.p4_dc_light1 = 0
        elif ((self.p4_switches_status_reg & 1) == 2):
            self.p4_dc_light1 = 1
        
        if ((self.p4_switches_status_reg & 2) == 0):    #check for 2nd bits 
            self.p4_dc_light2 = 0
        elif ((self.p4_switches_status_reg & 2) == 2):
            self.p4_dc_light2 = 1
        
        if ((self.p4_switches_status_reg & 4) == 0):    #check for 3rd bits 
            self.p4_ac1_status = 0
        elif ((self.p4_switches_status_reg & 4) == 4):
            self.p4_ac1_status = 1
        
        if ((self.p4_switches_status_reg & 8) == 0):    #check for 4th bits 
            self.p4_ac_status = 0
        elif ((self.p4_switches_status_reg & 8) == 8):
            self.p4_ac_status = 1

        if ((self.p4_switches_status_reg & 16) == 0):    #check for 5th bits
            self.p4_ac2_status = 0
        elif ((self.p4_switches_status_reg & 16) == 16):
            self.p4_ac2_status = 1
        
        if ((self.p4_switches_status_reg & 32) == 0):    #check for 6th bits 
            self.p4_dc1_status = 0
        elif ((self.p4_switches_status_reg & 32) == 32):
            self.p4_dc1_status = 1
                    
        if ((self.p4_switches_status_reg & 64) == 0):    #check for 7th bits 
            self.p4_dc_status = 0
        elif ((self.p4_switches_status_reg & 64) == 64):
            self.p4_dc_status = 1
          
        if ((self.p4_switches_status_reg & 128) == 0):    #check for 8th bits 
            self.p4_dc2_status = 0
        elif ((self.p4_switches_status_reg & 128) == 128):
            self.p4_dc2_status = 1
            
            

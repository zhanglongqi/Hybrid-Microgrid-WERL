import time
import math
from pymodbus3.client.sync import ModbusTcpClient

client = ModbusTcpClient('192.168.0.10')

class panel6():
    def p6_ac1_real_array(self):  
        #p6ac1list = client.read_holding_registers(10596, 49, unit=1)                 
        p6ac1list = client.read_holding_registers(6200, 49, unit=1)
        #print("p6_ac1 Real Array: " +str(p6ac1list.registers))       #print 'p6ac1list' - 16bit register
        self.p6ac1_LN_Voltage = float(p6ac1list.registers[16])  
        
    def p6_ac2_real_array(self):               
        #p6ac2list = client.read_holding_registers(10645, 49, unit=1)
        p6ac2list = client.read_holding_registers(6300, 49, unit=1)
        #print("p6_ac2 Real Array: " +str(p6ac2list.registers))       #print 'p6ac2list' - 16bit register
        self.p6ac2_LN_Voltage = float(p6ac2list.registers[16])  
                                   
    def p6_dc1_real_array(self):               
        p6dc1list = client.read_holding_registers(10694, 10, unit=1)
        #print("p6_dc1 Real Array: " +str(p6dc1list.registers))       #print 'p6dc2list' - 16bit register
        
        #DC to Real Conversion for Panel
        #Voltage
        if (p6dc1list.registers[1] & 256) == 0:
            self.p6dc1list_voltage = round(-(float(p6dc1list.registers[0])) * (10.0** (float(p6dc1list.registers[1])-3)), 2)
            #print('voltage for reg=0')
        else:
            self.p6dc1list_voltage = round(1*p6dc1list.registers[0] * (10.0**(p6dc1list.registers[1]-259)), 2)   
            #print('voltage for reg /= 0')
        #print("p6_dc1 Voltage: " +str(self.p6dc1list_voltage))              
        #Current
        if (p6dc1list.registers[3] & 256) == 0:
            self.p6dc1list_current = round((-p6dc1list.registers[2]) * (10.0** (p6dc1list.registers[3]-3)), 2)
        else:
            self.p6dc1list_current = round(1*p6dc1list.registers[2] * (10**(p6dc1list.registers[3]-259)), 2)    
        #print("p6_dc1 Current: " +str(self.p6dc1list_current))    
        #Power
        if (p6dc1list.registers[5] & 256) == 0:
            self.p6dc1list_power = round((((p6dc1list.registers[4]) * (10.0** (p6dc1list.registers[5]-3)) )/1000.0 ), 2)           
        else:
            self.p6dc1list_power = round((((-1.0*float(p6dc1list.registers[4])) * (10.0**(float(p6dc1list.registers[5]-259))) )/1000.0), 2)
        #print("p6_dc1 Power: " +str(self.p6dc1list_power))            
        #Positive Energy
        self.p6dc1list_PositiveEnergy = (65536.0*float(p6dc1list.registers[6])) + (float(p6dc1list.registers[7])/100.0)
        #print("p6_dc1 Positive Energy: " +str(self.p6dc1list_PositiveEnergy))    #Convert float to str before print       
        #Negative Energy
        self.p6dc1list_NegativeEnergy = (65536.0*p6dc1list.registers[8]) + (p6dc1list.registers[9]/100.0)
        #print("p6_dc1 Negative Energy: " +str(self.p6dc1list_NegativeEnergy))     #Convert float to str before print        
        '''
        #new
        p6dc1list = client.read_holding_registers(6400, 10, unit=1)
        #print("p6_dc1 Real Array: " +str(p6dc1list.registers))       #print 'p6dc2list' - 16bit register
        self.p6dc1list_voltage = p6dc1list.registers[0]
        self.p6dc1list_current = p6dc1list.registers[2]
        self.p6dc1list_power = p6dc1list.registers[4]
        self.p6dc1list_PositiveEnergy = p6dc1list.registers[6]
        self.p6dc1list_NegativeEnergy = p6dc1list.registers[8]
        '''
#-------Calculation of parameters-----------------------------------------------------------------------------------------------#
        #PV power
#        if p6dc1list.registers[5] == 0:
#           self.p6dc1list_power = ( (p6dc1list.registers[4]) * (10.0** (p6dc1list.registers[5]-3)) )/1000.0            
#        else:
#            self.p6dc1list_power = ( (-1.0*float(p6dc1list.registers[4])) * (10.0**(float(p6dc1list.registers[5]-259))) )/1000.0
#        #print("PV Power: " +str(self.p6dc1list_power))
#-------------------------------------------------------------------------------------------------------------------------------#  
    
    def p6_dc2_real_array(self):               
        p6dc2list = client.read_holding_registers(10704, 10, unit=1)
        #print("p6_dc2 Real Array: " +str(p6dc2list.registers))       #print 'p6dc2list' - 16bit register
        
        #DC to Real Conversion for Panel
        #Voltage
        if (p6dc2list.registers[1] & 128) == 0:
            self.p6dc2list_voltage = -(float(p6dc2list.registers[0])) * (10.0** (float(p6dc2list.registers[1])-3))
        else:
            self.p6dc2list_voltage = 1*p6dc2list.registers[0] * (10**(p6dc2list.registers[1]-259))   
        #print("p6_dc2 Voltage: " +str(self.p6dc2list_voltage))              
        #Current
        if (p6dc2list.registers[3] & 128) == 0:
            self.p6dc2list_current = (-p6dc2list.registers[2]) * (10.0** (p6dc2list.registers[3]-3))
        else:
            self.p6dc2list_current = 1*p6dc2list.registers[2] * (10**(p6dc2list.registers[3]-259))    
        #print("p6_dc2 Current: " +str(self.p6dc2list_current))    
        #Power
        if (p6dc2list.registers[5] & 128) == 0:
            self.p6dc2list_power = ( (p6dc2list.registers[4]) * (10.0** (p6dc2list.registers[5]-3)) )/1000.0            
        else:
            self.p6dc2list_power = ( (-1.0*float(p6dc2list.registers[4])) * (10.0**(float(p6dc2list.registers[5]-259))) )/1000.0
        #print("p6_dc2 Power: " +str(self.p6dc2list_power))            
        #Positive Energy
        self.p6dc2list_PositiveEnergy = (65536.0*float(p6dc2list.registers[6])) + (float(p6dc2list.registers[7])/100.0)
        #print("p6_dc2 Positive Energy: " +str(self.p6dc2list_PositiveEnergy))    #Convert float to str before print
        #Negative Energy
        self.p6dc2list_NegativeEnergy = (65536.0*p6dc2list.registers[8]) + (p6dc2list.registers[9]/100.0)
        #print("p6_dc2 Negative Energy: " +str(self.p6dc2list_NegativeEnergy))     #Convert float to str before print

#-------Calculation of parameters-----------------------------------------------------------------------------------------------#
        #PV power
        if p6dc2list.registers[5] == 0:
            self.p6dc2list_power = ( (p6dc2list.registers[4]) * (10.0** (p6dc2list.registers[5]-3)) )/1000.0            
        else:
            self.p6dc2list_power = ( (-1.0*float(p6dc2list.registers[4])) * (10.0**(float(p6dc2list.registers[5]-259))) )/1000.0
        #print("PV Power: " +str(self.p6dc2list_power))
#-------------------------------------------------------------------------------------------------------------------------------#       

    def p6_switches_status(self):               
        p6_switches_status_list = client.read_holding_registers(15005, 1, unit=1)
        #print("p6_switches_status_list: " +str(p6_switches_status_list.registers))  
        self.p6_switches_status_reg = p6_switches_status_list.registers[0]
        
        if ((self.p6_switches_status_reg & 1) == 0):    #check for 1st bits 
            self.p6_dc_light1 = 0
        elif ((self.p6_switches_status_reg & 1) == 2):
            self.p6_dc_light1 = 1
        
        if ((self.p6_switches_status_reg & 2) == 0):    #check for 2nd bits 
            self.p6_dc_light2 = 0
        elif ((self.p6_switches_status_reg & 2) == 2):
            self.p6_dc_light2 = 1
        
        if ((self.p6_switches_status_reg & 4) == 0):    #check for 3rd bits 
            self.p6_ac1_status = 0
        elif ((self.p6_switches_status_reg & 4) == 4):
            self.p6_ac1_status = 1
        
        if ((self.p6_switches_status_reg & 8) == 0):    #check for 4th bits 
            self.p6_ac_status = 0
        elif ((self.p6_switches_status_reg & 8) == 8):
            self.p6_ac_status = 1

        if ((self.p6_switches_status_reg & 16) == 0):    #check for 5th bits
            self.p6_ac2_status = 0
        elif ((self.p6_switches_status_reg & 16) == 16):
            self.p6_ac2_status = 1
        
        if ((self.p6_switches_status_reg & 32) == 0):    #check for 6th bits 
            self.p6_dc1_status = 0
        elif ((self.p6_switches_status_reg & 32) == 32):
            self.p6_dc1_status = 1
                    
        if ((self.p6_switches_status_reg & 64) == 0):    #check for 7th bits 
            self.p6_dc_status = 0
        elif ((self.p6_switches_status_reg & 64) == 64):
            self.p6_dc_status = 1
          
        if ((self.p6_switches_status_reg & 128) == 0):    #check for 8th bits 
            self.p6_dc2_status = 0
        elif ((self.p6_switches_status_reg & 128) == 128):
            self.p6_dc2_status = 1
            
                    

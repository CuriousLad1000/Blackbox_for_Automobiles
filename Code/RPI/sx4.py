import serial
import time

#========================================================================================================================================

#NOTE 1 INPUT BUFFER IS THE BUFFER USED TO STORE DATA RECEIVED FROM THE DEVICE.
#NOTE 2 OUTPUT BUFFER IS THE BUFFER USED TO STORE DATA TO TRANSMIT TO DEVICE.

# example 2  USING READLINES() FUNCTION
#port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.5,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()

#========================================================================================================================================
# COMMAND:-  ATZ    # RESETS OBD SCANNER AND TELLS VERSION
# EXPECTED OUTPUT :-  ELM327 v1.3a OBDGPSLogger
def reset():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=1,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 port.flushInput()      
 port.flushOutput()
 a="ATZ"
 port.write(a+"\r")
 lst1= port.readlines()        # Note that this function only returns on a timeout.
 a1=lst1[0].rstrip('\r\r>')   # # returns OBDGPSLogger WITHOUT new line char.
 a2= (a1[3:])
 print(a2)
 port.flushInput()        #clears atz
 port.flushOutput()
 port.close()
 return a2

#========================================================================================================================================
# COMMAND:-  ATRV   # TELLS BATTERY VOLTAGE
# EXPECTED OUTPUT :-  11.3  (RANDOM)
def bat():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.015,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 b="ATRV"
 port.write(b+"\r")
 lst2= port.readlines()        # Note that this function only returns on a timeout.
 b1=lst2[0].rstrip('\r\r>')   # # returns OBDGPSLogger WITHOUT new line char.
 b2= (b1[4:])
 print(b2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return b2

#========================================================================================================================================
# COMMAND:-  ATDP   # DESCRIBE THE CURRENT PROTOCOL
# EXPECTED OUTPUT :-  Automatic
def protocol():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.015,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 c="ATDP"
 port.write(c+"\r")
 lst3= port.readlines()        # Note that this function only returns on a timeout.
 c1=lst3[0].rstrip('\r\r>')   # # returns OBDGPSLogger WITHOUT new line char.
 c2= (c1[4:])
 print(c2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return c2

#========================================================================================================================================
# COMMAND:-  AT@1   # DISPLAY DEVICE DESCRIPTION
# EXPECTED OUTPUT :-  OBDGPSLogger
def device():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.015,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 f="AT@1"
 port.write(f+"\r")
 lst6=port.readlines()  # Note that this function only returns on a timeout.
 f1=lst6[0].rstrip('\r\r>')   # # returns OBDGPSLogger WITHOUT new line char.
 f2= (f1[4:])
 print(f2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return f2

#========================================================================================================================================
# COMMAND:-  0100   #  TELLS PID SUPPORTED
# EXPECTED OUTPUT :-  41 00 BE 3E B8 00 
def support():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.015,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 PID="0100"
 port.write(PID+"\r")
 lstp=port.readlines()          # Note that this function only returns on a timeout.
 PID1=lstp[0].rstrip('\r\r>')   # returns data WITHOUT "\r\r>" char.
 PID1a = (PID1[4:])
 print(PID1a)

 #time.sleep(3)    
 #lstp1=port.readlines()  
 #PID2=lstp1[0].rstrip('\r\r>')   
 #print(PID2)
 port.flushInput()
 port.flushOutput()
 port.close()
 time.sleep(.25)
 return PID1a

#========================================================================================================================================
# COMMAND:-  010C   #  ENGINE RPM   2B                              ((A*256)+B)/4 
# EXPECTED OUTPUT :-  hex no.
def rpm():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 i="010C"
 port.write(i+"\r")
 lst9= (port.readlines())        # Note that this function only returns on a timeout.
 i0=lst9[0].rstrip(' \r\r>')
 i1 = (i0[-5:]).replace(" ", "")
 i2 = (int(i1, base=16))/4
 print (i2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return i2

#========================================================================================================================================
# COMMAND:-  010D   #  SPEED        1B                                  A
# EXPECTED OUTPUT :-  hex no.
def speed():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 j="010D"
 port.write(j+"\r")
 lst10= (port.readlines())        # Note that this function only returns on a timeout.
 j0=lst10[0].rstrip(' \r\r>')
 j1 = int((j0[-3:]), base=16)
 print (j1)
 port.flushInput()
 port.flushOutput()
 port.close()
 return j1

#========================================================================================================================================
# COMMAND:-  0105   #  TELLS ENGINE COOLANT TEMP.   1B               A-40
# EXPECTED OUTPUT :-  hex no.
def enginet():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 h="0105"
 port.write(h+"\r")
 lst8= (port.readlines())        # Note that this function only returns on a timeout.
 h1=lst8[0].rstrip(' \r\r>')
 h2 = (int((h1[-3:]), base=16))-40
 print(h2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return h2

#========================================================================================================================================
# COMMAND:-  0111   #  THROTTLE POS.   1B      A*100/255
# EXPECTED OUTPUT :-  hex no.
def throttle():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 l="0111"
 port.write(l+"\r")
 lst12= port.readlines()        # Note that this function only returns on a timeout.
 l1=lst12[0].rstrip(' \r\r>')
 l2 = (int((l1[-2:]), base=16)*100)/255
 print(l2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return l2

#========================================================================================================================================
# COMMAND:-  0106   # Short term fuel trim, Bank 1.   1B      (A-128) * 100/128
# EXPECTED OUTPUT :-  hex no.
def sft():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 M="0106"
 port.write(M+"\r")
 lst13= port.readlines()        # Note that this function only returns on a timeout.
 M1=lst13[0].rstrip(' \r\r>')
 M2 = ((int((M1[-2:]), base=16)-128)*100)/128
 print(M2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return M2

#========================================================================================================================================
# COMMAND:-  0107   # Long term fuel trim, Bank 1.   1B      (A-128) * 100/128
# EXPECTED OUTPUT :-  hex no.
def lft():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 n="0107"
 port.write(n+"\r")
 lst14= port.readlines()        # Note that this function only returns on a timeout.
 n1=lst14[0].rstrip(' \r\r>')
 n2 = ((int((n1[-2:]), base=16)-128)*100)/128
 print(n2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return n2

#========================================================================================================================================
# COMMAND:-  010E   # Timing advance.   1B      A/2 - 64
# EXPECTED OUTPUT :-  hex no.
def timingadv():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 o="010E"
 port.write(o+"\r")
 lst15= port.readlines()        # Note that this function only returns on a timeout.
 o1=lst15[0].rstrip(' \r\r>')
 o2 = ((int((o1[-2:]), base=16))/2)-64
 print(o2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return o2

#========================================================================================================================================
# COMMAND:-  010F   # Intake air temperature.   1B      A-40
# EXPECTED OUTPUT :-  hex no.
def airtemp():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 p="010F"
 port.write(p+"\r")
 lst16= port.readlines()        # Note that this function only returns on a timeout.
 p1=lst16[0].rstrip(' \r\r>')
 p2 = (int((p1[-2:]), base=16))-40
 print(p2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return p2

#========================================================================================================================================
# COMMAND:-  0110   #  MAF RATE   2B              ((A*256)+B)/100 >>>  err. (get complete val. with decimal part not just round off)
# EXPECTED OUTPUT :-  hex no.
def maf():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 q="0110"
 port.write(q+"\r")
 lst17= (port.readlines())        # Note that this function only returns on a timeout.
 q0=lst17[0].rstrip(' \r\r>')
 q1 = (q0[-5:]).replace(" ", "")
 q2 = (int(q1, base=16))/100
 print (q2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return q2

#========================================================================================================================================
# COMMAND:-  011F   #  Time since engine start (max 65535 sec)   (A*256)+B
# EXPECTED OUTPUT :-  hex no.
def est():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 r="011F"
 port.write(r+"\r")
 lst18= (port.readlines())        # Note that this function only returns on a timeout.
 r0=lst18[0].rstrip(' \r\r>')
 r1 = (r0[-5:]).replace(" ", "")
 r2 = (int(r1, base=16))
 print (r2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return r2

#========================================================================================================================================
# COMMAND:-  0121   #  Dist travelled with mil on  2B  (max 65535 sec)       (A*256)+B
# EXPECTED OUTPUT :-  hex no.
def mildist():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 s="0121"
 port.write(s+"\r")
 lst19= (port.readlines())        # Note that this function only returns on a timeout.
 s0=lst19[0].rstrip(' \r\r>')
 s1 = (s0[-5:]).replace(" ", "")
 s2 = (int(s1, base=16))
 print (s2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return s2

#========================================================================================================================================
# COMMAND:-  0104   #  calculated load value         1B     A*100/255    in %
# EXPECTED OUTPUT :-  hex no.
def load():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 t="0104"
 port.write(t+"\r")
 lst20= port.readlines()        # Note that this function only returns on a timeout.
 t1=lst20[0].rstrip(' \r\r>')
 t2 = (int((t1[-2:]), base=16)*100)/255
 print(t2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return t2

#========================================================================================================================================
# COMMAND:-  012E   # Commanded Evaporative purge      1B         100*A/255
# EXPECTED OUTPUT :-  hex no.
def evappurge():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 u="012E"
 port.write(u+"\r")
 lst21= port.readlines()        # Note that this function only returns on a timeout.
 u1=lst21[0].rstrip(' \r\r>')
 u2 = (int((u1[-2:]), base=16)*100)/255
 print(u2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return u2

#========================================================================================================================================
# COMMAND:-  0130   #  No. of warm-ups since dtc codes cleared     1B                A
# EXPECTED OUTPUT :-  hex no.
def warmups():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 v="0130"
 port.write(v+"\r")
 lst22= (port.readlines())        # Note that this function only returns on a timeout.
 v0=lst22[0].rstrip(' \r\r>')
 v1 = int((v0[-3:]), base=16)
 print (v1)
 port.flushInput()
 port.flushOutput()
 port.close()
 return v1

#========================================================================================================================================
# COMMAND:-  0131   #  0131 dist. since dtc cleared.      2B      (A*256)+B
# EXPECTED OUTPUT :-  hex no.
def dtcdist():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 w="0131"
 port.write(w+"\r")
 lst23= (port.readlines())        # Note that this function only returns on a timeout.
 w0=lst23[0].rstrip(' \r\r>')
 w1 = (w0[-5:]).replace(" ", "")
 w2 = (int(w1, base=16))
 print (w2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return w2

#========================================================================================================================================
# COMMAND:-  0133   #  Barometric pressure      1B     A      Kpa (Absolute)
# EXPECTED OUTPUT :-  hex no.
def baro():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 x="0133"
 port.write(x+"\r")
 lst24= (port.readlines())        # Note that this function only returns on a timeout.
 x0=lst24[0].rstrip(' \r\r>')
 x1 = int((x0[-3:]), base=16)
 print (x1)
 port.flushInput()
 port.flushOutput()
 port.close()
 return x1

#========================================================================================================================================
# COMMAND:-  0142   #  control module voltage        2B          ((A*256)+B)/1000
# EXPECTED OUTPUT :-  hex no.
def cmv():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 y="0142"
 port.write(y+"\r")
 lst25= (port.readlines())        # Note that this function only returns on a timeout.
 y0=lst25[0].rstrip(' \r\r>')
 y1 = (y0[-5:]).replace(" ", "")
 y2 = (int(y1, base=16))/1000
 print (y2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return y2

#========================================================================================================================================
# COMMAND:-  0143   #  absolute load value         2B         ((A*256)+B)*100/255        in %
# EXPECTED OUTPUT :-  hex no.
def absld():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 z="0143"
 port.write(z+"\r")
 lst26= (port.readlines())        # Note that this function only returns on a timeout.
 z0=lst26[0].rstrip(' \r\r>')
 z1 = (z0[-5:]).replace(" ", "")
 z2 = ((int(z1, base=16))*100)/255
 print (z2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return z2

#========================================================================================================================================
# COMMAND:-  0145   #  Relative throttle pos          1B         A*100/255     in %
# EXPECTED OUTPUT :-  hex no.
def relthrottle():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 aa="0145"
 port.write(aa+"\r")
 lst27= port.readlines()        # Note that this function only returns on a timeout.
 aa1=lst27[0].rstrip(' \r\r>')
 aa2 = (int((aa1[-2:]), base=16)*100)/255
 print(aa2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return aa2

#========================================================================================================================================
# COMMAND:-  0147   #  Absolute throttle pos B          1B       A*100/255         in %
# EXPECTED OUTPUT :-  hex no.
def absthrottleB():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 ab="0147"
 port.write(ab+"\r")
 lst28= port.readlines()        # Note that this function only returns on a timeout.
 ab1=lst28[0].rstrip(' \r\r>')
 ab2 = (int((ab1[-2:]), base=16)*100)/255
 print(ab2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return ab2

#========================================================================================================================================
# COMMAND:-  0149   #  Accelerator pedal pos D       1B      A*100/255         in %
# EXPECTED OUTPUT :-  hex no.
def accelposD():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 ac="0149"
 port.write(ac+"\r")
 lst29= port.readlines()        # Note that this function only returns on a timeout.
 ac1=lst29[0].rstrip(' \r\r>')
 ac2 = (int((ac1[-2:]), base=16)*100)/255
 print(ac2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return ac2

#========================================================================================================================================
# COMMAND:-  014A   #  Accelerator pedal pos E       1B      A*100/255         in %
# EXPECTED OUTPUT :-  hex no.
def accelposE():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 ad="014A"
 port.write(ad+"\r")
 lst30= port.readlines()        # Note that this function only returns on a timeout.
 ad1=lst30[0].rstrip(' \r\r>')
 ad2 = (int((ad1[-2:]), base=16)*100)/255
 print(ad2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return ad2

#========================================================================================================================================
# COMMAND:-  014C   #  Commanded throttle actuator control  1B     A*100/255    in %
# EXPECTED OUTPUT :-  hex no.
def throttleact():
 port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 ae="014C"
 port.write(ae+"\r")
 lst31= port.readlines()        # Note that this function only returns on a timeout.
 ae1=lst31[0].rstrip(' \r\r>')
 ae2 = (int((ae1[-2:]), base=16)*100)/255
 print(ae2)
 port.flushInput()
 port.flushOutput()
 port.close()
 return ae2




#reset()
#protocol()
#device()
#support()
   
#bat()
#rpm()
#speed()
#enginet()
#throttle()
#sft()
#lft()
#timingadv()
#airtemp()
#maf()
#est()
#mildist()
#load()
#evappurge()
#warmups()
#dtcdist()
#baro()
#cmv()
#absld()
#relthrottle()
#absthrottleB()
#accelposD()
#accelposE()
#throttleact()

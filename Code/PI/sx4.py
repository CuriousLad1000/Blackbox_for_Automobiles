import serial
import time
import sys
#========================================================================================================================================

#NOTE 1 INPUT BUFFER IS THE BUFFER USED TO STORE DATA RECEIVED FROM THE DEVICE.
#NOTE 2 OUTPUT BUFFER IS THE BUFFER USED TO STORE DATA TO TRANSMIT TO DEVICE.

# example 2  USING READLINES() FUNCTION
#port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.5,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()

#========================================================================================================================================
# COMMAND:-  ATZ    # RESETS OBD SCANNER AND TELLS VERSION
# EXPECTED OUTPUT :-  ELM327 v1.3a OBDGPSLogger
def reset():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=1,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
#  print ("Could Not open Serial Port")
  return "Port open Error"
#  sys.exit()
#  raise
 port.flushInput()      
 port.flushOutput()
 a="ATZ"
 try:
  port.write(a+"\r")
  lst1= port.readlines()        # Note that this function only returns on a timeout.
  a1=lst1[0].rstrip('\r\r>')   # # returns OBDGPSLogger WITHOUT new line char.
  a2= (a1[3:])
  print(a2)
  port.flushInput()        #clears atz
  port.flushOutput()
  port.close()
 except:
  return "Reset Error"
 else:
  return a2

#========================================================================================================================================
# COMMAND:-  ATRV   # TELLS BATTERY VOLTAGE
# EXPECTED OUTPUT :-  11.3  (RANDOM)
def bat():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.015,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 b="ATRV"
 try:
  port.write(b+"\r")
  lst2= port.readlines()        # Note that this function only returns on a timeout.
  b1=lst2[0].rstrip('\r\r>')   # # returns OBDGPSLogger WITHOUT new line char.
  b2= (b1[4:])
  print(b2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:
  return b2

#========================================================================================================================================
# COMMAND:-  ATDP   # DESCRIBE THE CURRENT PROTOCOL
# EXPECTED OUTPUT :-  Automatic
def protocol():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.015,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
#  print ("Could Not open Serial Port")
  return "Port open Error"
#  sys.exit()
#  raise
 c="ATDP"
 try:
  port.write(c+"\r")
  lst3= port.readlines()        # Note that this function only returns on a timeout.
  c1=lst3[0].rstrip('\r\r>')   # # returns OBDGPSLogger WITHOUT new line char.
  c2= (c1[4:])
  print(c2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "Protocol Error"
 else:
  return c2

#========================================================================================================================================
# COMMAND:-  AT@1   # DISPLAY DEVICE DESCRIPTION
# EXPECTED OUTPUT :-  OBDGPSLogger
def device():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.015,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
# print ("Could Not open Serial Port")
  return "Port open Error"
#  sys.exit()
#  raise
 f="AT@1"
 try:
  port.write(f+"\r")
  lst6=port.readlines()  # Note that this function only returns on a timeout.
  f1=lst6[0].rstrip('\r\r>')   # # returns OBDGPSLogger WITHOUT new line char.
  f2= (f1[4:])
  print(f2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "Device Desc. Error"
 else:
  return f2

#========================================================================================================================================
# COMMAND:-  0100   #  TELLS PID SUPPORTED
# EXPECTED OUTPUT :-  41 00 BE 3E B8 00 
def support():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.015,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
#  print ("Could Not open Serial Port")
  return "Port open Error"
#  sys.exit()
#  raise
 PID="0100"
 try:
  port.write(PID+"\r")
  lstp=port.readlines()          # Note that this function only returns on a timeout.
  PID1=lstp[0].rstrip('\r\r>')   # returns data WITHOUT "\r\r>" char.
  PID1a = (PID1[4:])
  print(PID1a)
  port.flushInput()
  port.flushOutput()
  port.close()
  time.sleep(.25)
 except:
  return "Supported PIDs Error"
 else:
  return PID1a

#========================================================================================================================================
# COMMAND:-  010C   #  ENGINE RPM   2B                              ((A*256)+B)/4 
# EXPECTED OUTPUT :-  hex no.
def rpm():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise

 i="010C"
 try:
  port.write(i+"\r")
  lst9= (port.readlines())        # Note that this function only returns on a timeout.
  i0=lst9[0].rstrip(' \r\r>')
  i1 = (i0[-5:]).replace(" ", "")
  i2 = (int(i1, base=16))/4
  print (i2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:
  return i2

#========================================================================================================================================
# COMMAND:-  010D   #  SPEED        1B                                  A
# EXPECTED OUTPUT :-  hex no.
def speed():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 j="010D"
 try:
  port.write(j+"\r")
  lst10= (port.readlines())        # Note that this function only returns on a timeout.
  j0=lst10[0].rstrip(' \r\r>')
  j1 = int((j0[-3:]), base=16)
  print (j1)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:
  return j1

#========================================================================================================================================
# COMMAND:-  0105   #  TELLS ENGINE COOLANT TEMP.   1B               A-40
# EXPECTED OUTPUT :-  hex no.
def enginet():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 h="0105"
 try:
  port.write(h+"\r")
  lst8= (port.readlines())        # Note that this function only returns on a timeout.
  h1=lst8[0].rstrip(' \r\r>')
  h2 = (int((h1[-3:]), base=16))-40
  print(h2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:
  return h2

#========================================================================================================================================
# COMMAND:-  0111   #  THROTTLE POS.   1B      A*100/255
# EXPECTED OUTPUT :-  hex no.
def throttle():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 l="0111"
 try:
  port.write(l+"\r")
  lst12= port.readlines()        # Note that this function only returns on a timeout.
  l1=lst12[0].rstrip(' \r\r>')
  l2 = (int((l1[-2:]), base=16)*100)/255
  print(l2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else: 
  return l2

#========================================================================================================================================
# COMMAND:-  0106   # Short term fuel trim, Bank 1.   1B      (A-128) * 100/128
# EXPECTED OUTPUT :-  hex no.
def sft():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 M="0106"
 try:
  port.write(M+"\r")
  lst13= port.readlines()        # Note that this function only returns on a timeout.
  M1=lst13[0].rstrip(' \r\r>')
  M2 = ((int((M1[-2:]), base=16)-128)*100)/128
  print(M2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else: 
  return M2

#========================================================================================================================================
# COMMAND:-  0107   # Long term fuel trim, Bank 1.   1B      (A-128) * 100/128
# EXPECTED OUTPUT :-  hex no.
def lft():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 n="0107"
 try:
  port.write(n+"\r")
  lst14= port.readlines()        # Note that this function only returns on a timeout.
  n1=lst14[0].rstrip(' \r\r>')
  n2 = ((int((n1[-2:]), base=16)-128)*100)/128
  print(n2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else: 
  return n2

#========================================================================================================================================
# COMMAND:-  010E   # Timing advance.   1B      A/2 - 64
# EXPECTED OUTPUT :-  hex no.
def timingadv():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 o="010E"
 try:
  port.write(o+"\r")
  lst15= port.readlines()        # Note that this function only returns on a timeout.
  o1=lst15[0].rstrip(' \r\r>')
  o2 = ((int((o1[-2:]), base=16))/2)-64
  print(o2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:  
  return o2

#========================================================================================================================================
# COMMAND:-  010F   # Intake air temperature.   1B      A-40
# EXPECTED OUTPUT :-  hex no.
def airtemp():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 p="010F"
 try:
  port.write(p+"\r")
  lst16= port.readlines()        # Note that this function only returns on a timeout.
  p1=lst16[0].rstrip(' \r\r>')
  p2 = (int((p1[-2:]), base=16))-40
  print(p2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:  
  return p2

#========================================================================================================================================
# COMMAND:-  0110   #  MAF RATE   2B              ((A*256)+B)/100 >>>  err. (get complete val. with decimal part not just round off)
# EXPECTED OUTPUT :-  hex no.
def maf():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 q="0110"
 try:
  port.write(q+"\r")
  lst17= (port.readlines())        # Note that this function only returns on a timeout.
  q0=lst17[0].rstrip(' \r\r>')
  q1 = (q0[-5:]).replace(" ", "")
  q2 = (int(q1, base=16))/100
  print (q2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else: 
  return q2

#========================================================================================================================================
# COMMAND:-  011F   #  Time since engine start (max 65535 sec)   (A*256)+B
# EXPECTED OUTPUT :-  hex no.
def est():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 r="011F"
 try:
  port.write(r+"\r")
  lst18= (port.readlines())        # Note that this function only returns on a timeout.
  r0=lst18[0].rstrip(' \r\r>')
  r1 = (r0[-5:]).replace(" ", "")
  r2 = (int(r1, base=16))
  print (r2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:
  return r2

#========================================================================================================================================
# COMMAND:-  0121   #  Dist travelled with mil on  2B  (max 65535 sec)       (A*256)+B
# EXPECTED OUTPUT :-  hex no.
def mildist():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 s="0121"
 try:
  port.write(s+"\r")
  lst19= (port.readlines())        # Note that this function only returns on a timeout.
  s0=lst19[0].rstrip(' \r\r>')
  s1 = (s0[-5:]).replace(" ", "")
  s2 = (int(s1, base=16))
  print (s2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:
  return s2

#========================================================================================================================================
# COMMAND:-  0104   #  calculated load value         1B     A*100/255    in %
# EXPECTED OUTPUT :-  hex no.
def load():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 t="0104"
 try:
  port.write(t+"\r")
  lst20= port.readlines()        # Note that this function only returns on a timeout.
  t1=lst20[0].rstrip(' \r\r>')
  t2 = (int((t1[-2:]), base=16)*100)/255
  print(t2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:  
  return t2

#========================================================================================================================================
# COMMAND:-  012E   # Commanded Evaporative purge      1B         100*A/255
# EXPECTED OUTPUT :-  hex no.
def evappurge():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 u="012E"
 try:
  port.write(u+"\r")
  lst21= port.readlines()        # Note that this function only returns on a timeout.
  u1=lst21[0].rstrip(' \r\r>')
  u2 = (int((u1[-2:]), base=16)*100)/255
  print(u2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:  
  return u2

#========================================================================================================================================
# COMMAND:-  0130   #  No. of warm-ups since dtc codes cleared     1B                A
# EXPECTED OUTPUT :-  hex no.
def warmups():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 v="0130"
 try:
  port.write(v+"\r")
  lst22= (port.readlines())        # Note that this function only returns on a timeout.
  v0=lst22[0].rstrip(' \r\r>')
  v1 = int((v0[-3:]), base=16)
  print (v1)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:  
  return v1

#========================================================================================================================================
# COMMAND:-  0131   #  0131 dist. since dtc cleared.      2B      (A*256)+B
# EXPECTED OUTPUT :-  hex no.
def dtcdist():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 w="0131"
 try:
  port.write(w+"\r")
  lst23= (port.readlines())        # Note that this function only returns on a timeout.
  w0=lst23[0].rstrip(' \r\r>')
  w1 = (w0[-5:]).replace(" ", "")
  w2 = (int(w1, base=16))
  print (w2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:  
  return w2

#========================================================================================================================================
# COMMAND:-  0133   #  Barometric pressure      1B     A      Kpa (Absolute)
# EXPECTED OUTPUT :-  hex no.
def baro():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 x="0133"
 try:
  port.write(x+"\r")
  lst24= (port.readlines())        # Note that this function only returns on a timeout.
  x0=lst24[0].rstrip(' \r\r>')
  x1 = int((x0[-3:]), base=16)
  print (x1)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:  
  return x1

#========================================================================================================================================
# COMMAND:-  0142   #  control module voltage        2B          ((A*256)+B)/1000
# EXPECTED OUTPUT :-  hex no.
def cmv():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 y="0142"
 try:
  port.write(y+"\r")
  lst25= (port.readlines())        # Note that this function only returns on a timeout.
  y0=lst25[0].rstrip(' \r\r>')
  y1 = (y0[-5:]).replace(" ", "")
  y2 = (int(y1, base=16))/1000
  print (y2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:  
  return y2

#========================================================================================================================================
# COMMAND:-  0143   #  absolute load value         2B         ((A*256)+B)*100/255        in %
# EXPECTED OUTPUT :-  hex no.
def absld():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 z="0143"
 try:
  port.write(z+"\r")
  lst26= (port.readlines())        # Note that this function only returns on a timeout.
  z0=lst26[0].rstrip(' \r\r>')
  z1 = (z0[-5:]).replace(" ", "")
  z2 = ((int(z1, base=16))*100)/255
  print (z2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:  
  return z2

#========================================================================================================================================
# COMMAND:-  0145   #  Relative throttle pos          1B         A*100/255     in %
# EXPECTED OUTPUT :-  hex no.
def relthrottle():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 aa="0145"
 try:
  port.write(aa+"\r")
  lst27= port.readlines()        # Note that this function only returns on a timeout.
  aa1=lst27[0].rstrip(' \r\r>')
  aa2 = (int((aa1[-2:]), base=16)*100)/255
  print(aa2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:  
  return aa2

#========================================================================================================================================
# COMMAND:-  0147   #  Absolute throttle pos B          1B       A*100/255         in %
# EXPECTED OUTPUT :-  hex no.
def absthrottleB():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 ab="0147"
 try:
  port.write(ab+"\r")
  lst28= port.readlines()        # Note that this function only returns on a timeout.
  ab1=lst28[0].rstrip(' \r\r>')
  ab2 = (int((ab1[-2:]), base=16)*100)/255
  print(ab2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:  
  return ab2

#========================================================================================================================================
# COMMAND:-  0149   #  Accelerator pedal pos D       1B      A*100/255         in %
# EXPECTED OUTPUT :-  hex no.
def accelposD():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 ac="0149"
 try:
  port.write(ac+"\r")
  lst29= port.readlines()        # Note that this function only returns on a timeout.
  ac1=lst29[0].rstrip(' \r\r>')
  ac2 = (int((ac1[-2:]), base=16)*100)/255
  print(ac2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:  
  return ac2

#========================================================================================================================================
# COMMAND:-  014A   #  Accelerator pedal pos E       1B      A*100/255         in %
# EXPECTED OUTPUT :-  hex no.
def accelposE():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 ad="014A"
 try:
  port.write(ad+"\r")
  lst30= port.readlines()        # Note that this function only returns on a timeout.
  ad1=lst30[0].rstrip(' \r\r>')
  ad2 = (int((ad1[-2:]), base=16)*100)/255
  print(ad2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:  
  return ad2

#========================================================================================================================================
# COMMAND:-  014C   #  Commanded throttle actuator control  1B     A*100/255    in %
# EXPECTED OUTPUT :-  hex no.
def throttleact():
 try:
  port = serial.Serial("/dev/ttyUSB0", baudrate=38400, timeout=.07,bytesize=8,stopbits=1)  # CONFIGURE TIMEOUT FOR READLINES()
 except:
  print ("Could Not open Serial Port")
  sys.exit()
  raise
 ae="014C"
 try:
  port.write(ae+"\r")
  lst31= port.readlines()        # Note that this function only returns on a timeout.
  ae1=lst31[0].rstrip(' \r\r>')
  ae2 = (int((ae1[-2:]), base=16)*100)/255
  print(ae2)
  port.flushInput()
  port.flushOutput()
  port.close()
 except:
  return "-0001"
 else:  
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

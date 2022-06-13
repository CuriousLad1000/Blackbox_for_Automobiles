import serial
import time
import sys
from time import strftime

def speed():
    for i in range(2):
     try:
      port = serial.Serial("COM4", baudrate=38400, timeout=0.25,bytesize=8,stopbits=1)
      port.flushInput()
      port.flushOutput()
     except:
            print ("Could Not open Serial Port")
            sys.exit()
            raise
     port.write("\r")
     rcv = port.readline()
#     time.sleep(0.0025)  
     port.write("010D\r")
     rcv = port.readline()
     port.flushInput()
     port.flushOutput()
     port.close()
     #print(rcv)
    try:
     a = int((rcv[-4:]), base=16)
     print (a)
     print(strftime("%H:%M:%S"))
    except ValueError:
            #return -1
        print 'ERROR'
             

while True:
 speed()
#sys.exit()


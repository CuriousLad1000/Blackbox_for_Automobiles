import serial
import time
import sys

def RPM():
    for i in range(2):
     try:
      #port = serial.Serial("/dev/ttyUSB0", baudrate=9600, timeout=2.0,bytesize=8,stopbits=1)
      port = serial.Serial("COM4", baudrate=38400, timeout=0.25,bytesize=8,stopbits=1)
      port.flushInput()
      port.flushOutput()
     except:
            print ("Could Not open Serial Port")
            sys.exit()
            raise          

     port.write("\r")
     rcv = port.readline()
     time.sleep(0.0025)  
     port.write("010C\r")
     rcv = port.readline()
     port.flushInput()
     port.flushOutput()
     port.close()
     #print(rcv)

    try:
     
      b = (rcv[-7:]).replace(" ", "")
      a = (int(b, base=16))/4
      print (a)     
    except ValueError:
            #return -1
        print 'ERROR'
             

#while True:
RPM()
#sys.exit()


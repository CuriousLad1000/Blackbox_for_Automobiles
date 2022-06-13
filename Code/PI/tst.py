import sx4
import OBDGPS
import db
import serial
import sqlite3
from adxl345 import ADXL345
import time
  
adxl345 = ADXL345()

rst=sx4.reset()
print(rst)

pro=sx4.protocol()
print(pro)


dev=sx4.device()
print(dev)

sup=sx4.support()
print(sup)

db.create_base()
db.create_db(rst,pro,dev,sup)


#sx4.port.close()
#sx4.port = serial.Serial("COM5", baudrate=38400, timeout=.25,bytesize=8,stopbits=1)


while True:
 #================= OBD LOG =========================   
 battery=sx4.bat()
 print(battery)

 rpm=sx4.rpm()
 print(rpm)

 speed=sx4.speed()
 print(speed)

 absld=sx4.absld()
 print(absld)

 load=sx4.load()
 print(load)

 evappurge=sx4.evappurge()
 print(evappurge)

 maf=sx4.maf()
 print(maf)

 timingadv=sx4.timingadv()
 print(timingadv)

 throttle=sx4.throttle()
 print(throttle)

 relthrottle=sx4.relthrottle()
 print(relthrottle)

 absthrottleB=sx4.absthrottleB()
 print(absthrottleB)

 accelposD=sx4.accelposD()
 print(accelposD)
 
 accelposE=sx4.accelposE()
 print(accelposE)

 throttleact=sx4.throttleact()
 print(throttleact)

 enginet=sx4.enginet()
 print(enginet)

 airtemp=sx4.airtemp()
 print(airtemp)

 baro=sx4.baro()
 print(baro)

 sft=sx4.sft()
 print(sft)

 lft=sx4.lft()
 print(lft)

 cmv=sx4.cmv()
 print(cmv)

 est=sx4.est()
 print(est)

 mildist=sx4.mildist()
 print(mildist)

 warmups=sx4.warmups()
 print(warmups)

 dtcdist=sx4.dtcdist()
 print(dtcdist)
 
 #=================ACCEL=====================

 axes = adxl345.getAxes(True)
 time.sleep(.2)
 acx = axes['x']
 print acx
 acy = axes['y']
 print acy
 acz = axes['z']
 print acz
 db.data(battery,rpm,speed,absld,load,evappurge,maf,timingadv,throttle,relthrottle,absthrottleB,accelposD,accelposE,throttleact,enginet,airtemp,baro,sft,lft,cmv,est,mildist,warmups,dtcdist,acx,acy,acz)

 #================ GPS LOG ============================
 
 mode=OBDGPS.mode()
 print mode
 lat=OBDGPS.latitude()
 print lat
 lon=OBDGPS.longitude()
 print lon
 alt=OBDGPS.altitude()
 print alt
 speed=OBDGPS.speed()
 print speed
 climb=OBDGPS.climb()
 print climb
 laterr=OBDGPS.latierr()
 print laterr
 longerr=OBDGPS.longierr()
 print longerr
 verterr=OBDGPS.vertierr()
 print verterr
 heading=OBDGPS.heading()
 print heading
 gpst=OBDGPS.gpst()
 print gpst
 db.gps_data(mode,lat,lon,alt,speed,climb,laterr,longerr,verterr,heading,gpst)
 

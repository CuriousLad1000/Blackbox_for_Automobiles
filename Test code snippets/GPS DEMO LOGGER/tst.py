import db
import sqlite3
import OBDGPS
import os


db.create_base()
while True:
    
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


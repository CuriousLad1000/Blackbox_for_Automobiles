#!/usr/bin/python

import sqlite3
from time import strftime

a=strftime("%d-%m-%Y--%H#%M#%S")


def create_base():
    
# conn = sqlite3.connect('/home/pi/BB/DATABASE/'+a+'.db')
 conn = sqlite3.connect(a+'.db')

 conn.execute('''CREATE TABLE OBD_INIT
       (ID INTEGER PRIMARY KEY   AUTOINCREMENT    NOT NULL,
       TIME                  TEXT                 NOT NULL,
       RESET                 TEXT                 NOT NULL,
       PROTOCOL              TEXT                 NOT NULL,
       DEVICE                TEXT                 NOT NULL,
       SUPPORTED_PIDs        TEXT                 NOT NULL);''')

 conn.execute('''CREATE TABLE OBD_DATA
       (ID INTEGER PRIMARY KEY   AUTOINCREMENT       NOT NULL,
       TIME                  TEXT                    NOT NULL,
       BATTERY               FLOAT                   NOT NULL,
       RPM                   INTEGER                 NOT NULL,
       SPEED                 INTEGER                 NOT NULL,
       Abs_LOAD              FLOAT                   NOT NULL,
       Calc_LOAD             FLOAT                   NOT NULL,
       Cmd_Evap_PURGE        FLOAT                   NOT NULL,
       MAF                   FLOAT                   NOT NULL,
       TIMING_ADV            FLOAT                   NOT NULL,
       THROTTLE              FLOAT                   NOT NULL,
       Rel_T_Pos             FLOAT                   NOT NULL,
       Abs_T_PosB            FLOAT                   NOT NULL,
       ACCEL_PosD            FLOAT                   NOT NULL,
       ACCEL_PosE            FLOAT                   NOT NULL,
       Cmd_THROTTLE_ACTUATOR_CTRL     FLOAT          NOT NULL,
       ENGINE_TEMP           INTEGER                 NOT NULL,
       INTAKE_AIR_TEMP       INTEGER                 NOT NULL,
       BARO_PRESSURE         INTEGER                 NOT NULL,
       SHORT_FUEL_TRIM       INTEGER                 NOT NULL,
       LONG_FUEL_TRIM        INTEGER                 NOT NULL,
       CTRL_MOD_VOLT         FLOAT                   NOT NULL,
       ENGINE_RUN_TIME       TEXT                    NOT NULL,
       MIL_DIST              INTEGER                 NOT NULL,
       WARMUPs_DTC_CLR       TEXT                    NOT NULL,
       DIST_DTC_CLR          INTEGER                 NOT NULL,    
       ACCEL_X_G             TEXT                    NOT NULL,
       ACCEL_Y_G             TEXT                    NOT NULL,
       ACCEL_Z_G             TEXT                    NOT NULL);''')

 conn.execute('''CREATE TABLE GPS_DATA
       (ID INTEGER PRIMARY KEY   AUTOINCREMENT      NOT NULL,
       TIME                  TEXT                   NOT NULL,
       STATUS                TEXT                   NOT NULL,
       LATITUDE              FLOAT                  NOT NULL,
       LONGITUDE             FLOAT                  NOT NULL,
       ALTITUDE              FLOAT                  NOT NULL,
       SPEED                 FLOAT                  NOT NULL,
       CLIMB                 TEXT                   NOT NULL,
       LAT_ERR               TEXT                   NOT NULL,
       LONG_ERR              TEXT                   NOT NULL,
       VERT_ERR              TEXT                   NOT NULL,
       HEADING               TEXT                   NOT NULL,
       GPS_TIME              TEXT                   NOT NULL);''')

 conn.commit()
 conn.close()


#=======================================================================

def create_db(rst,pro,dev,sup):
 #conn = sqlite3.connect('/home/pi/BB/DATABASE/'+a+'.db')
 conn = sqlite3.connect(a+'.db')
 da=strftime("%H:%M:%S")
 conn.execute("INSERT INTO OBD_INIT(TIME,RESET,PROTOCOL,DEVICE,SUPPORTED_PIDs) VALUES(?,?,?,?,?)", (da,rst,pro,dev,sup));
 conn.commit()
 conn.close()

#=================================================================

def data(battery,rpm,speed,absld,load,evappurge,maf,timingadv,throttle,relthrottle,absthrottleB,accelposD,accelposE,throttleact,enginet,airtemp,baro,sft,lft,cmv,est,mildist,warmups,dtcdist,acx,acy,acz):
   
 #conn = sqlite3.connect('/home/pi/BB/DATABASE/'+a+'.db')
 conn = sqlite3.connect(a+'.db')
 da=strftime("%H:%M:%S")
 conn.execute("INSERT INTO OBD_DATA(TIME,BATTERY,RPM,SPEED,Abs_LOAD,Calc_LOAD,Cmd_Evap_PURGE,MAF,TIMING_ADV,THROTTLE,Rel_T_Pos,Abs_T_PosB,ACCEL_PosD,ACCEL_PosE,Cmd_THROTTLE_ACTUATOR_CTRL,ENGINE_TEMP,INTAKE_AIR_TEMP,BARO_PRESSURE,SHORT_FUEL_TRIM,LONG_FUEL_TRIM,CTRL_MOD_VOLT,ENGINE_RUN_TIME,MIL_DIST,WARMUPs_DTC_CLR,DIST_DTC_CLR,ACCEL_X_G,ACCEL_Y_G,ACCEL_Z_G) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (da,battery,rpm,speed,absld,load,evappurge,maf,timingadv,throttle,relthrottle,absthrottleB,accelposD,accelposE,throttleact,enginet,airtemp,baro,sft,lft,cmv,est,mildist,warmups,dtcdist,acx,acy,acz));
 conn.commit()
 conn.close()

#====================================================================================

def gps_data(mode,lat,lon,alt,speed,climb,laterr,longerr,verterr,heading,gpst):
   
# conn = sqlite3.connect('/home/pi/BB/DATABASE/'+a+'.db')
 conn = sqlite3.connect(a+'.db')
 
 da=strftime("%H:%M:%S")

 conn.execute("INSERT INTO GPS_DATA(TIME,STATUS,LATITUDE,LONGITUDE,ALTITUDE,SPEED,CLIMB,LAT_ERR,LONG_ERR,VERT_ERR,HEADING,GPS_TIME) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (da,mode,lat,lon,alt,speed,climb,laterr,longerr,verterr,heading,gpst));
 conn.commit()
 conn.close()

 

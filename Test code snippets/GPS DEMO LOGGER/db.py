#!/usr/bin/python

import sqlite3
from time import strftime

a=strftime("%d-%m-%Y--%H#%M#%S")


def create_base():
 conn = sqlite3.connect(a+'.db')
 conn.execute('''CREATE TABLE OBD_INIT
       (ID INTEGER PRIMARY KEY   AUTOINCREMENT  NOT NULL,
       TIME                  TEXT                 NOT NULL,
       RESET                 BLOB                 NOT NULL,
       AUTO                  TEXT                 NOT NULL,
       PROTOCOL              BLOB                 NOT NULL,
       PROTOCOL_NUMBER       TEXT                 NOT NULL,
       DEVICE                BLOB                 NOT NULL,
       SUPPORTED_PIDs        TEXT                 NOT NULL);''')
 conn.execute('''CREATE TABLE OBD_DATA
       (ID INTEGER PRIMARY KEY   AUTOINCREMENT       NOT NULL,
       TIME                  TEXT                    NOT NULL,
       BATTERY               FLOAT                   NOT NULL,
       RPM                   INTEGER                 NOT NULL,
       SPEED                 INTEGER                 NOT NULL,
       ENGINE_TEMP           INTEGER                 NOT NULL,
       THROTTLE              INTEGER                 NOT NULL,
       MASS_AIRFLOW          INTEGER                 NOT NULL);''')
 conn.execute('''CREATE TABLE GPS_DATA
       (NAME INTEGER PRIMARY KEY   AUTOINCREMENT      NOT NULL,
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

def create_db(rst,aut,pro,num,dev,sup):

 da=strftime("%H:%M:%S")
 conn.execute("INSERT INTO OBD_INIT(TIME,RESET,AUTO,PROTOCOL,PROTOCOL_NUMBER,DEVICE,SUPPORTED_PIDs) VALUES(?,?,?,?,?,?,?)", (da,rst,aut,pro,num,dev,sup));
 conn.commit()
 conn.close()

#=================================================================

def data(battery,rpm,speed,enginet,throttle,maf):
   
 conn = sqlite3.connect(a+'.db')
 da=strftime("%H:%M:%S")

 conn.execute("INSERT INTO OBD_DATA(TIME,BATTERY,RPM,SPEED,ENGINE_TEMP,THROTTLE,MASS_AIRFLOW) VALUES(?,?,?,?,?,?,?)", (da,battery,rpm,speed,enginet,throttle,maf));
 conn.commit()
 conn.close()

def gps_data(mode,lat,lon,alt,speed,climb,laterr,longerr,verterr,heading,gpst):
   
 conn = sqlite3.connect(a+'.db')
 da=strftime("%H:%M:%S")

 conn.execute("INSERT INTO GPS_DATA(TIME,STATUS,LATITUDE,LONGITUDE,ALTITUDE,SPEED,CLIMB,LAT_ERR,LONG_ERR,VERT_ERR,HEADING,GPS_TIME) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)", (da,mode,lat,lon,alt,speed,climb,laterr,longerr,verterr,heading,gpst));
 conn.commit()
 conn.close()

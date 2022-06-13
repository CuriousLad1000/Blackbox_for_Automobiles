import gps
import time
# Listen on port 2947 (gpsd) of localhost
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

#while True:
# report = session.next()
# if report['class'] == 'TPV':   #time Pos Vel report
#  if hasattr(report, 'time'):
#     print report.time    #time in UTC
#     print report.lat     #lat  + ---> N   - ------> S
#     print report.lon     #lon  + ---> E   - ------> W
#     print report.alt     #alt in meters
#     print report.speed   #speed in meters per sec 
#     print report.climb   #climb in meters + or -
#     print report.mode # fix mode 1- no  2- 2d fix  3- 3d fix
#     print report.epx  #LONG est. err (m)
#     print report.epy  #Lat est. err (m)
#     print report.epv  #Vert. err (m)
#     print report.track  #Course over gnd degrees from true north
     
def mode():
 while True:
     report = session.next()
     if report['class'] == 'TPV':   #time Pos Vel report
      if hasattr(report, 'mode'):
          a=report.mode
          break
 return a

def latitude():
 while True:
     report = session.next()
     if report['class'] == 'TPV':   #time Pos Vel report
      if hasattr(report, 'lat'):
          b=report.lat
          break
 return b


def longitude():
 while True:
     report = session.next()
     if report['class'] == 'TPV':   #time Pos Vel report
      if hasattr(report, 'lon'):
          c=report.lon
          break
 return c

def altitude():
 while True:
     report = session.next()
     if report['class'] == 'TPV':   #time Pos Vel report
      if hasattr(report, 'alt'):
          d=report.alt
          break
 return d

def speed():
 while True:
     report = session.next()
     if report['class'] == 'TPV':   #time Pos Vel report
      if hasattr(report, 'speed'):
          e=report.speed
          break
 return e

def climb():
 while True:
     report = session.next()
     if report['class'] == 'TPV':   #time Pos Vel report
      if hasattr(report, 'climb'):
          f=report.climb
          break
 return f

def latierr():
 while True:
     report = session.next()
     if report['class'] == 'TPV':   #time Pos Vel report
      if hasattr(report, 'epy'):
          g=report.epy
          break
 return g

def longierr():
 while True:
     report = session.next()
     if report['class'] == 'TPV':   #time Pos Vel report
      if hasattr(report, 'epx'):
          h=report.epx
          break
 return h

def vertierr():
 while True:
     report = session.next()
     if report['class'] == 'TPV':   #time Pos Vel report
      if hasattr(report, 'epv'):
          i=report.epv
          break
 return i

def heading():
 while True:
     report = session.next()
     if report['class'] == 'TPV':   #time Pos Vel report
      if hasattr(report, 'track'):
          j=report.track
          break
 return j

def gpst():
 while True:
     report = session.next()
     if report['class'] == 'TPV':   #time Pos Vel report
      if hasattr(report, 'time'):
          k=report.time
          break
 return k

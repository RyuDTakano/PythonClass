#python test3.py P1 P2
#python test3.py Lamp on
#python test3.py Lamp off
import sys
from Ctrl import Crtl2 as Lamp
from Ctrl import Crtl1 as Pump

##print(sys.argv[1])
##print(sys.argv[2])
print ('0')

if __name__ == '__main__':
 Lamp.ControlLamp('Lamp1','ON')
 Pump.ControlPump('Pump1','OFF')
  

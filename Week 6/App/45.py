#python test3.py P1 P2
#python test3.py Lamp on
#python test3.py Lamp off
import sys
from Ctrl import Crtl2 as LampCrtl
from Ctrl import Crtl1 as PumpCrtl

#print(sys.argv[1])
#print(sys.argv[2])


Arg1 = str(sys.argv[1])
Arg2 = str(sys.argv[2])

if __name__ == '__main__':
   # Lamp.ControlLamp('Lamp1','ON')
   Pump.ControlPump(Arg1 ,Arg2 )
   #print('run main='+__name__)
   input('kk')

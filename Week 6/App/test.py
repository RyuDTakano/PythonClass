import sys
from Ctrl import Crtl2 as LampCrtl
from Ctrl import Crtl1 as PumpCrtl


Arg1 = str(sys.argv[1])
Arg2 = str(sys.argv[2])

if __name__ == '__main__':
   
   PumpCrtl.ControlPump(Arg1,Arg2)
 
   input('__')

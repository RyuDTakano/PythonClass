print('ctrl2='+__name__)
def ControlPump(L,S):
    if L=='Pump1':
        if S =='ON':
          print('Pump1 on')
        elif S =='OFF':
          print('Pump1 off')
        else :
            print('error')

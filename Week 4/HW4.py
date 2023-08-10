while(1):
  Speed = int(input('True Speed Value'))
  Setpoint = int(input('Setpoint Value'))
  if Speed < Setpoint and Speed < 10:
     Speed = Speed +1
  elif  Speed > Setpoint and -10 < Speed :
      Speed = Speed - 1
  print(Speed)    

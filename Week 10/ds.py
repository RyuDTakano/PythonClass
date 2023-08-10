def myfunctionCtoF(a,gu=1):
    for i in range(0, 10):
        a[i] = (5/9)*((a[i]-32))*gu
    return a

a = [1,2,3,4,5,6,7,8,9,10]
myfunctionCtoF(a)
for gundam  in range(0,10):
  print( gundam+1 ,'Celsius to Fahrenheita is :',a[gundam])






























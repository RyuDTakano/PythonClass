a='123456789'
A1 =(a[0:3]+' '+a[6:9])
A2 =(a[7:]+'_'+a[3:6])
A3 =(a[-1::-7]+'\n'+a[-5:-7:-1])
print(A1)
print(A2)
print(A3)

class Tcar:
    Color = 'Black'
    Price = 'Free'
    age   = '19'
    Speed     = 'LightSpeed'
    Turn      = 'back'
    Light     = 'on'
    OwnerName = 'BMX'
    def __init__(self, Color, Price,age,OwnerName):
        self.Color = Color 
        self.Price = Price
        self.age = age
        self.OwnerName = OwnerName

    def RunSpeed(self, Speed):
        print('Speed = ' + str(Speed))
        self.Speed = Speed
        
    def FlashLight(self, Light):
        print('Light = ' + str(Light))
        self.Light = Light
        
    def Turn(self, Turn):
        print('Light = ' + str(Turn))
        self.Turn = Turn
        
D1 = Tcar('Green', 'Expensive','10','Prayuth')

D1.RunSpeed(input('Put Car speed :'))
D1.FlashLight(input('Put FlashLight status : '))
D1.Turn(input('Put Car direction :'))

print('OwnerName : ',D1.OwnerName)
print('Color     : ',D1.Color)
print('Price     :' ,D1.Price)
print('Age       :',D1.age)
print('speed     :',D1.Speed)
print('direction :',D1.Turn)
print('FlashLight:',D1.Light)

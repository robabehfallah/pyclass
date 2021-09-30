class car():
    def __init__ (self,brand,model,motor_volume,current_speed):
        self.brand = brand
        self.model = model
        self.motor_volume = motor_volume
        self.current_speed = current_speed

    def boogh (self,boogh_length): #method
        my_boogh = 'b' + 'o' * boogh_length + 'gh'
        print(my_boogh)

    def light (self,mode):
        if mode == 1 :
            print('bala')
        elif mode == 2 :
            print('paeen')
    def gaz_bede(self):
        while self.current_speed < 120:
            self.current_speed+=10
            print('daram ba sorate {} km/h harekat mikonam'.format(self.current_speed))
        print('Sorate bish az 120km/h mamnoo ast')

my_new_car = car('KIA','RIO',2,10).gaz_bede()

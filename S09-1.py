class car():
    def __init__ (self,brand,model,motor_volume):
        self.brand = brand
        self.model = model
        self.motor_volume = motor_volume

    def boogh (self,boogh_length): #method
        my_boogh = 'b' + 'o' * boogh_length + 'gh'
        print(my_boogh)

    def light (self,mode):
        if mode == 1 :
            print('bala')
        elif mode == 2 :
            print('paeen')

my_new_bmw = car('bmw','i8',2).light(1)

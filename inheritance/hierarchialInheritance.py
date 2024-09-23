class Vehicle:
    def vehicle_info(self):
        print('this is vehicle')

class Car(Vehicle):
    def car_info(self,name):
        print('car name is: ', name)

class Lorry(Vehicle):
    def lorry_info(self,name):
        print('Lorry name: ',name)

nganyas = Lorry()
nganyas.vehicle_info()
nganyas.lorry_info('Fuso')

nganya = Car()
nganya.vehicle_info()
nganya.car_info('BMW')
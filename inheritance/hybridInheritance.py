class Vehicle:
    def vehicle_info(self):
        print('inside vehicle class')

class Car(Vehicle):
    def car_info(self):
        print('inside car class')

class Truck(Vehicle):
    def truck_info(self):
        print('inside truck class')

class SportsCar(Car,Vehicle):
    def sportsCar_info(self):
        print('inside sportscar class')

nganya = SportsCar()
nganya.vehicle_info()
nganya.car_info()
nganya.sportsCar_info()

nganyas = Truck()
nganyas.truck_info()
nganyas.vehicle_info()
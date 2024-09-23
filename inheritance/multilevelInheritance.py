class Vehicle:
    def vehicle_info(self):
        print('inside vehicle class')

class Car(Vehicle):
    def car_info(self):
        print('inside car class')

class SportsCar(Car):
    def sportsCar_info(self):
        print('inside sportscar class')

cars = SportsCar()
cars.vehicle_info()
cars.car_info()
cars.sportsCar_info()
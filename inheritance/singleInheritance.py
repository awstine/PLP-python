#Base parent
class Vehicle:
    def Vehicle_info(self):
        print('inside Parent(Vehicle) class')
class Car(Vehicle):
    def car_info(self):
        print('inside Child(Car) class')

car = Car()
car.Vehicle_info()
car.car_info()
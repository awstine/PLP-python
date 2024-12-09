class Animal:
    def move(self):
        pass

class Vehicle:
    def move(self):
        pass

class Dog(Animal):
        print("Running 🐕")

class Bird(Animal):
        print("Flying 🦅")

class Car(Vehicle):
        print("Driving 🚗")

class Plane(Vehicle):
        print("Flying ✈️")

# Creating instances of each class
dog = Dog()
bird = Bird()
car = Car()
plane = Plane()

# Calling the move method on each instance
dog.move()   
bird.move()  
car.move()   
plane.move() 
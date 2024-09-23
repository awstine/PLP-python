class Person:
    def displayInfo(self):
        print("Personal Information")

p1 = Person()
p1.displayInfo()

class Person1:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def displayInfo2(self):
        print('Person name: ',self.name, 'Age: ', self.age)

p2 = Person1("Maiko", 33)
p2.displayInfo2()

class Person:
    #Members of a class
    nationality = 'Kenyan' #attribute
    def __init__(self):#constructor
        self.name = ''
        self.age = 0

p1 = Person() #Instance
p1.name = "Maiko"
p1.age = 30

print(p1.name,p1.age)
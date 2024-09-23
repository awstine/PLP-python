class Person:
    name = ''
    age = 0
    gender = ''

    def person_info(self,name,age,gender):
        print('My name is',name, 'am',age, 'years old and am a',gender)

p1 = Person()
p1.person_info("Awstine",33,"Male")
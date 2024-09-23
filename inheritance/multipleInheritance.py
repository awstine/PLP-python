class Person:
    def person_info(self,name,age):
        print('inside Person Class')
        print('name: ',name, 'age: ',age)

class Company:
    def company_info(self,company_name,location):
        print('inside company class')
        print('name: ', company_name, 'location: ',location)

class Employee(Person,Company):
    def employee_info(self,salary,skill):
        print('inside Employee class')
        print('salary: ',salary, 'skill: ',skill)

emp = Employee()
emp.person_info('jessica',23)
emp.company_info('Badlands','uthiru')
emp.person_info('Maiko',30)

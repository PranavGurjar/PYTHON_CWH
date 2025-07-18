# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
        
# e1 = Employee("Pranav", 45000)
# print(e1.name)
# print(e1.salary)

# string = "Ram-18500"
# e2 = Employee( string.split("-")[0], string.split("-")[1])
# print(e2.name)
# print(e2.salary)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
       
    @classmethod 
    def fromStr(self, string):
        return self(string.split("-")[0], int(string.split("-")[1]))
        
e1 = Employee("Pranav", 45000)
print(e1.name)
print(e1.salary)

string = "Ram-18500"
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)



# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_string(cls, string):
#         name, age = string.split(',')
#         return cls(name, int(age))

# person = Person.from_string("John Doe, 30")
# print(person.name, person.age)
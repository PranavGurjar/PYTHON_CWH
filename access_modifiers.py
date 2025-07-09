
# public
# class Employee:
#     pass

# a = Employee()
# a.emp1 = 5

# class Employee:
#     def __init__(self):
#         self.name = "Pranav"

# a = Employee()
# print(a.name)


# Private (use name mangling method)
# class Employee:
#     def __init__(self):
#         self.__name = "Pranav"

# a = Employee()
# # print(a.__name) #Cannot be used directly
# print(a._Employee__name)  #Can be used indirectly
# print(a.__dir__())

# protected

class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))

# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName())
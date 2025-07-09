# class Employeee:
#     def __init__(self, name):
#         self.name = name
        
#     def __len__(self):
#         i = 0
#         for item in self.name:
#             i+=1
#             return i

from emp import Employee
        
e = Employee("Pranav")
print(e)
print(str(e))
print(repr(e))
e()
# print(e.name)
# print(len(e.name))



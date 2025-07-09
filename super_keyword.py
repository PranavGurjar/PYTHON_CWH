# class Parent:
#     def parent_meth(self):
#         print("Hello From Parent Class I am Parent Method")
        
# class Child(Parent):
#     def parent_meth(self):
#         print("Hello From Child Class I am Parent Method")
#         super().parent_meth()
        
#     def child_meth(self):
#         print("Hello From Child Class I am Child Method")
#         super().parent_meth()
        
        
# test = Child()
# test.child_meth()
# test.parent_meth()


# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
        
# class Programmer(Employee):
#     def __init__(self, name, id, lang):
#         self.name = name
#         self.id = id
#         self.lang = lang
        
# rohan = Employee("Rohan Das", "450")
# pranav = Programmer("Pranav", "110", "java")
# print(pranav.name)
# print(pranav.id)
# print(pranav.lang)

# print(rohan.name)
# print(rohan.id)



class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
        
rohan = Employee("Rohan Das", "450")
pranav = Programmer("Pranav", "110", "java")
print(pranav.name)
print(pranav.id)
print(pranav.lang)

print(rohan.name)
print(rohan.id)
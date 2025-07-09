# class Employee:
#     company = "Apple"
#     def __init__(self, name):
#         self.name = name
        
        
#     def showEmp(self):
#         print(f"The name is {self.name} and company is {self.company}")
        
#     def changeCompany(self, newCompany):
#         self.company = newCompany
        
# emp1 = Employee("Raj")
# emp1.showEmp()
# print(Employee.company)
# emp1.changeCompany("Tesla")
# emp1.showEmp()
# print(Employee.company)


class Employee:
    company = "Apple"
    def __init__(self, name):
        self.name = name
        
        
    def showEmp(self):
        print(f"The name is {self.name} and company is {self.company}")
    
    @classmethod 
    def changeCompany(self, newCompany):
        self.company = newCompany
        
emp1 = Employee("Raj")
emp1.showEmp()
print(Employee.company)
emp1.changeCompany("Tesla")
emp1.showEmp()
print(Employee.company)
class Employee:
    def __init__(self, name):
        self.name = name
        
    def show(self):
        print(f"The name of Employee is {self.name}")
        
        
class Dancer:
    def __init__(self, dance):
        self.dance = dance
        
    def show(self):
        print(f"The name of dance is {self.dance}")
        
        
class DancerEmployee(Employee, Dancer):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance
        
    def showDancerEmployee(self):
        print(f"The Dancer Employee : {self.name} : {self.dance}")
    
        
de = DancerEmployee("Pranav", "Kathak")
print(de.name)
print(de.dance)
de.showDancerEmployee()
de.show()
print(DancerEmployee.mro())
de.show()
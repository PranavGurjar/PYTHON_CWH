class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        
    def showDetails(self):
        print(f"The employee details : {self.id} is {self.name}")
        
class Programmer(Employee):
    def showLang(self):
        print("The Default langauge is python")
    
    
e1 = Employee(101,"Pranav Mahajan")
e1.showDetails()

e2 = Programmer(111, "Raj Mahajan")
e2.showDetails()
e2.showLang() 
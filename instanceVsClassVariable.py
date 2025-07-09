class Employee:
    companyName = "Apple"  #class variable
    noOfEmp = 0     #class variable
    def __init__(self, name):
        self.name = name
        self.raise_amount = 10.2
        Employee.noOfEmp += 1
        
    def showDetails(self):
        print(f"The companay is {self.companyName} employee size {self.noOfEmp} name {self.name} is raise amount is {self.raise_amount}")
        
emp1 = Employee("Roshan")
emp1.companyName = "Nestle" #instance variable because it object change it
emp1.showDetails()

emp2 = Employee("Shan")
emp2.raise_amount = 25.5   #instance variable
emp2.showDetails()
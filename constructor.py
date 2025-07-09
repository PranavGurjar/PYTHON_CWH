# class Person:
#     def __init__(self):
#         print("I am Default Constructor")

        
#     def init(self):
#         print(f"{self.name} is a {self.occupation}")
        
# a = Person()
# a.name = "Pranav"
# a.occupation = "Developer"
# a.init()

# b = Person()
# b.name = "Om"
# b.occupation = "HR"
# b.init() 

class Person:
    def __init__(self, name, occupation):
        print("I am Parameterize Constructor")
        self.name = name
        self.occupation = occupation
        
    def init(self):
        print(f"{self.name} is a {self.occupation}")
  
        
a = Person("Raj", "CA")
a.name = "Pranav"
a.occupation = "Developer"
a.init()


b = Person("Shiv", "Scientist") 
# b.name = "Om"
# b.occupation = "HR"
b.init() 
      
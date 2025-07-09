class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def makeSound(self):
        print(f"The {self.name} is make sound")
        
class Dog(Animal):
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def makeSound(self):
        print(f"Bark")
        
class Cat(Animal):
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def makeSound(self):
        print(f"mau")
        
        
a = Animal("tiger", "tiger")
a.makeSound()

d = Dog("dog", "dog")
d.makeSound()

c = Cat("cat", "cat")
c.makeSound()
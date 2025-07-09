class Person:
    name = "Pranav"
    work = "Software Developer"
    networth = 10
    def info(self):
        print(f"{self.name} is a {self.work}")
    
a = Person()
b = Person()
c = Person()


# print(a.name)
# print(a.work)
# print(a.networth)

b.name = "Raj"
b.work = "HR"


c.name = "Krish"
c.work = "Accountant"

print(a.name, a.work)
a.info()
b.info()
c.info()



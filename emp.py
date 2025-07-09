class Employee:
    def __init__(self, name):
        self.name = name
        
    def __len__(self):
        i = 0
        for item in self.name:
            i+=1
            return i
        
    def __str__(self):
        return f"The name of the employee are {self.name} str"
    
    def __repr__(self):
        # return f"The name of the employee are {self.name} repr"
        return f"Employee is ('{self.name}')"
    
    def __call__(self, *args, **kwds):
        print(f"Hey I am Call method")
    
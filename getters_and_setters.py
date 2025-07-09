class MyClass:
    def __init__(self, value):
        self.value = value
        
    def show(self):
        print(f"value is {self.value}")
        
    # getter
    @property
    def ten_value(self):
        return self.value*10
    
    # setter
    @ten_value.setter
    def ten_value(self, new_value):
        self.value = new_value/10
        
obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()
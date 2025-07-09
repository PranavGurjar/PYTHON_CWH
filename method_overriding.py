# class Rectangle:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def area(self):
#         return self.x * self.y
    
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
        
#     def area(self):
#         return 3.14 * self.radius * self.radius
    
    
# rect = Rectangle(5, 3)
# print("Rectangle Area : ",rect.area())

# cc = Circle(5)
# print("Circle Area : ",cc.area())




class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def area(self):
        return self.x * self.y
    
class Circle(Rectangle):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)
        
    def area(self):
        return 3.14 * super().area()
    
    
rect = Rectangle(5, 3)
print("Rectangle Area : ",rect.area())

cc = Circle(5)
print("Circle Area : ",cc.area())



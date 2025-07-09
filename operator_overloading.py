# class Vector:
#     def __init__(self, i, j, k):
#         self.i = i
#         self.j = j
#         self.k = k
        
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
        
#     def __add__(self, x):
#         return f"{self.i + x.i}i + {self.j + x.j}j + {self.k + x.k}k"
    
# v1 = Vector(2, 3, 4)
# print(v1)

# v2 = Vector(4, 3, 2)
# print(v2)

# print("Sum Of Vector : ", v1 + v2)
# print("type of Sum Of Vector : ", type(v1 + v2))




class Vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
        
    def __add__(self, x):
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)
    
v1 = Vector(2, 3, 4)
print(v1)

v2 = Vector(4, 3, 2)
print(v2)

print("Sum Of Vector : ", v1 + v2)
print("type of Sum Of Vector : ", type(v1 + v2))
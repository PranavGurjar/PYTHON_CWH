class Math:
    def __init__(self, num):
        self.num = num
        
    def addtonum(self, n):
        self.num = self.num + n
    
    @staticmethod
    def add(a, b):
        return a + b
    
# res = Math.add(5, 4) 
# print(res)
a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(a.add(5, 1))
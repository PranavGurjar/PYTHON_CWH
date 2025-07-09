
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning!")
        fx(*args, **kwargs)
        print("Thank You Sir for using function")
    return mfx
  
  

def hello():
    print("Hello World")
  
@greet  
def add(a, b):
    print(a+b)

# hello()    
greet(hello)()
add(2, 5)
# greet(add)(2, 5)
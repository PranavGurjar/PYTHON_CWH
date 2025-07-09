# a = 10

# def func():
#     a = 5
#     print(f"local value of a : {a}")
#     print("This is global and local difference")
    

# print(f"Global value of a : {a}")
# func()
# print(f"local value of a : {a}")


num = 150

def my_func():
    global num
    num = 120
    print(f"local value of num : {num}")
    
    

print(f"Global value of num : {num}")
my_func()
print(f"Global value of num : {num}")
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)

# num = 5      
# res = factorial(num)
# print("Factorial Of ",num," is ",res)



 # Quick Quiz: Write a program to print the Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)

# 0 1 1 2 3 5 8....   

# print("Fibonacci sequence : ")
# a = 0
# print(a)
# b = 1
# print(b)
# sum = 0
# for i in range(2, 10):
#     sum = a + b
#     print(sum)
#     a = b
#     b = sum
    
    


def fibonacci(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
  
for i in range(10):
    print(f"f{i} : ",{fibonacci(i)})
    
    
    
    
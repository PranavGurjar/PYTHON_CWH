import time

# def usingFor():
#     for i in range(50000):
#         print(i)
        
# def usingWhile():
#     i = 0
#     while i<50000:
#         print(i)
#         i += 1
        
# init1 = time.time()        
# usingFor()
# t1 = time.time() - init1

# init2 = time.time()  
# usingWhile()
# t2 = time.time() - init2

# print(t1)
# print(t2)


# print(4)
# time.sleep(3)
# print("This is print after 3 second")

t = time.localtime()
print(t)
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(formatted_time)
formatted_time = time.strftime("%d-%m-%Y %H:%M:%S", t)
print(formatted_time)



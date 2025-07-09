import threading
import time
from concurrent.futures import ThreadPoolExecutor


def function(second):
    print(f"Sleeping for {second} second")
    time.sleep(second)
    return second


# # Normal Code
# time1 = time.perf_counter()  
# function(4)
# function(2)
# function(1)
# time2 = time.perf_counter()  
# print("Normal Code : ",time2 - time1)

# # same code using Thread
# ttime1 = time.perf_counter()  
# t1 = threading.Thread(target=function, args=[4])
# t2 = threading.Thread(target=function, args=[2])
# t3 = threading.Thread(target=function, args=[1])
# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# ttime2 = time.perf_counter()  
# print("Thread Code : ",ttime2 - ttime1)


def poolingDemo1():
    with ThreadPoolExecutor() as executor:
        future = executor.submit(function, 3)
        print(future.result())
        future = executor.submit(function, 2)
        print(future.result())
        future = executor.submit(function, 4)
        print(future.result())
    
def poolingDemo2():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(function, 3)
        future2 = executor.submit(function, 2)
        future3 = executor.submit(function, 4)
        print(future1.result())
        print(future2.result())
        print(future3.result())
    
# poolingDemo1()
# poolingDemo2()


def poolingDemo3():
    with ThreadPoolExecutor() as executor:
        l = [3, 5, 1, 2]
        results = executor.map(function, l)
        for result in results:
            print(result)
        
poolingDemo3()
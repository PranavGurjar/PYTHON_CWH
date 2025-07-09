
def func1():
    try:
        arr = [1, 2, 3, 4, 5, 6]
        i = int(input("Enter the index : "))
        print(arr[i])
        return 1
    except:
        print("Some error occured!")
        return 0
    finally:
        print("It is always excuted.")
    # print("It is always excuted.")
    
x = func1()
print(bool(x))
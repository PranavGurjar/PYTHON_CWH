def duosum(a=1, b=2):
    print("Sum : ",a+b)

def trisum(a, b, c=2):
    print("Sum : ",a+b+c)



duosum(1)
trisum(1,2)


def average(*number):
    print(type(number))
    sum = 0
    for i in number:
        sum += i
        
    # print("Average : ",sum/len(number))
    return sum/len(number)


# average(4, 6)
# average(b=9)
c = average(10, 20, 30)
print(c)


def name(**name):
    print(type(name))
    print("Hello",name["fname"],name["mname"],name["lname"])

name(fname = "Pranav", mname = "Rajendra", lname = "Mahajan")





a = int(input("Enter the value between 5 and 9 : "))

if(a<5 or a>9):
    raise ValueError("Value should between 5 and 9")


# str = "QUIT"

# if(str=="QUIT"):
#     raise ValueError("String is not the 'QUIT' ")
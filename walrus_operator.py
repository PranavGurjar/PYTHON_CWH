# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# a = False
# print(a)
# print(a:=True)


# foods = list()
# while True:
#     food = input("Enter the food name : ")
#     if(food == "quit"):
#         break
#     foods.append(food)

# print(foods)


foods = list()
while (food := input("Enter the food name : ")) != "quit":
    foods.append(food)
    
print(foods)

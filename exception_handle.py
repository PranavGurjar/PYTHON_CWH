# num = input("Enter the number : ")
# # num = int(input("Enter the number : "))
# print(f"Print the Table of {num}")

# try:
#     for i in range(1, 11):
#         # print(f"{num} X {i} = {num*i}")
#         print(f"{int(num)} X {i} = {int(num)*i}")
# # except Exception as e:
# #     print(e)
# except:
#     print("Invalid input")
    
# print("Some imp line for execution")
# print("Program is done")


try:
    a = int(input("Enter the number : "))
    arr = [1, 2, 3]
    print(arr[a])
except ValueError:
    print("Invalid number")
except IndexError:
    print("Invalid index")






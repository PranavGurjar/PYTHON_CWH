dic = {
    "name" : "Pranav",
    "age" : 23,
    "gender" :  "Male"
}
# print(dic)
# print(dic["name"])
# print(dic.keys())
# print(dic.values())

# for key in dic.keys():
#     print(f"The value of key {key} is {dic[key]}")

print(dic.items())    
for key, value in dic.items():
    print(f"The value of key {key} is {value}")
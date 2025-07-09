import os

folders = os.listdir("Python_Day46/data")

print(os.getcwd)
os.chdir("../Python_Day46/Users")
print(os.getcwd)

for folder in folders:
    print(folder)
    print(os.listdir(f"../data/{folder}"))
    



import os

files = os.listdir("F:/Python/CWH_Python/Python_Day75/clutter")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        
        os.rename(f"F:/Python/CWH_Python/Python_Day75/clutter/{file}", f"F:/Python/CWH_Python/Python_Day75/clutter/{i}.png")
        
        i = i+1
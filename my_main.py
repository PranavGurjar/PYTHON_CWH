import os

if(not os.path.exists("Python_Day46/data")):
    os.mkdir("Python_Day46/data")
    
for i in range(0, 100):
    os.mkdir(f"Python_Day46/data/tutorial_{i+1}")
    
    
    
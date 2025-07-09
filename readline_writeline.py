f = open("F:/Python/CWH_Python/Python_Day50/myfile1.txt", "r")


# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)



# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         print(line, type(line))
#         break
 
 
f = open("F:/Python/CWH_Python/Python_Day50/myfile2.txt", "r")

# i = 0
# while True:
#     i+=1
#     line = f.readline()
    
#     if not line:
#         break
    
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])
    
#     print(f"Marks of student {i} is math is : {m1}")
#     print(f"Marks of student {i} is english is : {m2}")
#     print(f"Marks of student {i} is biology is : {m3}")

#     print(line)
    
# f.close()   

f = open("F:/Python/CWH_Python/Python_Day50/myfile3.txt", "w")
line = ['line1\n', 'line2\n', 'line3\n']
f.writelines(line)
f.close()



    
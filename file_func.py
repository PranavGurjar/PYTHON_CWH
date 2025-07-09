
# with open("F:/Python/CWH_Python/Python_Day51/file.txt", 'r') as f:
#     print(type(f))
    
#     f.seek(15) #print after 15 character
#     print(f.tell()) #current position of sick
#     data = f.read()
#     print(data)


with open("F:/Python/CWH_Python/Python_Day51/sample.txt",'w') as f:
    f.write("Hello World!")
    f.truncate(5) #delete after 5 character
    
with open("F:/Python/CWH_Python/Python_Day51/sample.txt",'r') as f:
    print(f.read())
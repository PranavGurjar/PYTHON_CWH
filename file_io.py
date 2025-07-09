# WRITING A FILE using write

base_path = "F:/Python/CWH_Python/Python_Day49/"


f = open(f"{base_path} + my_text1.txt", "w")
f.write("Hello i am a Pranav Rajendra Mahajan ")
f.close()

with open(f"{base_path} + my_text1.txt", "a") as f:
    f.write("I am live in Jalgaon")

f = open(f"{base_path} + my_text2.txt", "w")
f.write("I am a text file 2 in this file format ")
f.close

# WRITING A FILE using append
f = open(f"{base_path} + my_text2.txt", "a")
f.write("Hello i am a Pranav Rajendra Mahajan ")
f.close()

# READING A FILE
f = open(f"{base_path} + my_text1.txt", "r")
text = f.read()
print(text)
f.close()

f = open(f"{base_path} + my_text2.txt", "r")
text = f.read()
print(text)
f.close()
# string are immutable
a = "Pranav"
print(len(a))
print(a)
print(a.lower())
print(a.upper())

b = "!!!Rajendra! !!!!!!! Rajendra!!!"
print(b.rstrip("!"))
print(b.replace("Rajendra", "Ram"))
print(b.split(" ")) # convert in list
print(b.count("Rajendra"))

blogHeading = "introduction tO jS"
print(blogHeading.capitalize())

str1 = "Welcome to the Console!!!"
print(str1)
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))

# email = "mahajan@gmail.com"
# print(email.endswith("@gmail.com"))
# print(email.endswith(".com", 13, 17))
# quote = "Welcome to the Console !!!"
# print(quote.endswith("to", 4, 10))

str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))
# print(str1.index("ishh"))

str1 = "WelcomeToTheConsole510"
print(str1.isalnum())
str1 = "Welcome"
print(str1.isalpha())

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())

str1 = "World Health Organization" 
print(str1.istitle())

str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())

str1 = "pYTHON IS A iNTERPRETED lANGUAGE"
print(str1.swapcase())

str1 = "His name is Dan. Dan is an honest man."
print(str1.title())



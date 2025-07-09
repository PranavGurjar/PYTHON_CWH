# explicit typecasting

a = "1"
b = 1
c = "2"
d = 2

print(int(a) + int(c))
print(b + d)
print(int(a) + b)
print(int(c) + d)


# implicit typecasting
e = 9.9
f = 10
print(e + f," ",type(e+f))

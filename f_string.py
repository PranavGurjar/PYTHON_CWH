line = "Hey My name is {1} and I am From {0}"

country = "India"
name = "Pranav Mahajan"

# print(line.format(name, country))
print(line.format(country, name))


print(f"Hey My name is {name} and I am From {country}")
print(f"Hey My name is {{name}} and I am From {{country}}")


price = 45.5899
txt = f"For Only {price:.2f} Dollars"
print(txt)
# print(txt.format())


print(type(f"{2 * 30}"))
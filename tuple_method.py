tup = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
# res = tup.count(3)
# res = tup.index(3)
# res = tup.index(3, 4, 8)
res = len(tup)
print("The result : ",res)



# countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
# countries2 = ("Vietnam", "India", "China")
# southEastAsia = countries + countries2
# print(southEastAsia)



countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

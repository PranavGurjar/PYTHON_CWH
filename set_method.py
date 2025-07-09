# s1 = {1, 2, 5, 6}
# s2 = {3, 6, 7}
# print(s1.union(s2))
# s1.update(s2)
# print(s1, s2)



# cities1 = {"Delhi", "pune", "mumbai", "indore"}
# cities2 = {"Bhopal", "pune", "Nagpur", "indore"}
# cities3 = cities1.intersection_update(cities2)
# print(cities3)

# cities1 = {"Delhi", "pune", "mumbai", "indore"}
# cities2 = {"Bhopal", "pune", "Nagpur", "indore"}
# cities3 = cities1.symmetric_difference(cities2)
# print(cities3)

# cities1 = {"Delhi", "pune", "mumbai", "indore"}
# cities2 = {"Bhopal", "pune", "Nagpur", "indore"}
# cities3 = cities1.difference(cities2)
# print(cities3)



# cities1 = {"Delhi", "pune1", "mumbai", "indore1"}
# cities2 = {"Bhopal", "pune", "Nagpur", "indore"}
# cities3 = cities1.isdisjoint(cities2)
# print(cities3)  


# cities1 = {"Delhi", "pune", "mumbai", "indore"}
# cities2 = {"pune", "indore"}
# cities3 = cities1.issuperset(cities2)
# print(cities3)
# cities3 = cities2.issubset(cities1)
# print(cities3)


# cities = {"Delhi", "pune", "mumbai", "indore"}
# cities.add("Nagpur")
# print(cities)
# cities.remove("Nagpur")
# print(cities)
# # cities.remove("Bhopal")
# # print(cities)
# cities.discard("Bhopal")
# print(cities)


# cities = {"Delhi", "pune", "mumbai", "indore"}
# item = cities.pop()
# print(cities)
# print(item)

# cities = {"Delhi", "pune", "mumbai", "indore"}
# cities.clear() 
# print(cities)

# cities = {"Delhi", "pune", "mumbai", "indore"}
# del cities
# # print(cities)

cities = {"Delhi", "pune", "mumbai", "indore"}
if "Delhi" in cities:
    print("Delhi is present")
else:
    print("Delhi is not present")
    
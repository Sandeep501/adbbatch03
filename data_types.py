# # list

# fruits = ["apple", "banana", "mango", "cherry"]
# # print(fruits)

# # methods
# fruits.append("orange")
# # print(fruits)

# fruits.remove("banana")
# # print(fruits)

# fruits.insert(1, "apple")
# # print(fruits)

# # fruits.pop()
# # print(fruits)

# fruits.sort()
# # print(fruits)

# fruits.sort(reverse=True)
# # print(fruits)

# # print(fruits[1:4])

# # fruits[2] = "Tomato"
# # print(fruits)

# # tuple

# vals = (1, 2, 3, "apple", True, False, 78.89, "apple", "apple")
# # print(vals[1:4])

# # print(vals.count("apple"))


# # sets
# my_set = {1, 2, 3, 4, "apple", "mango", 34.90, "mango", "mango"}
# # print(my_set)


# my_set.add(5)
# # print(my_set)

# my_set.remove(4)
# # print(my_set)

# my_set.discard("mango")
# # print(my_set)


# my_set.discard("cherry")
# # print(my_set)

# my_set.remove("Orange")
# print(my_set)


# --------------------------------------

# dictionary

person = {
    "name": "John",
    "age": 24,
    "city": "Bangalore",
    "languages": ["English", "Kannada", "Telugu"],
    "Prog Languages": {"Python": 4, "C": 3, "Java": 3.5}
}

# print(person["name"])

person["Job"] = "Data Engineer"
person["age"] = 32
del person["city"]

# print(person["languages"][0])
# print(person["Prog Languages"]["Python"])

person.pop("languages")

print(person)


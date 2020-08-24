""" Strings and Lists are Iterable. Lists are mutable. """

fruit = list()
print(fruit)

fruits = ["Apple", "Orange", "Pear"]
fruits.append("Banana")

print(fruits)

print(fruits[2])

fruits[2] = "Plum"

print(fruits[2])

fruits.pop()

print(fruits)



# Combine two lists
color1 = ["blue", "green"]
color2 = ["black", "red"]
colors = color1 + color2
print(colors)

if "red" in colors:
    print("Found red")
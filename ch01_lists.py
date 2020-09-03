""" Lists [] are Iterable. Lists are mutable. """

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

# Slice list
print(f"Sliced list: {colors[0:2]}")

# Lists in a tuple
eights = ["Edgar Allan Poe", "Charles Dickens"]

nines = ["Hemingway", "Fitzgerald", "Orwell", "Sinclair"]

authors = (eights, nines)
print(authors)
print(authors[0])
print(authors[1][3])



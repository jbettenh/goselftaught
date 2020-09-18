""" Dictionaries {} are mutable. They don't store data in order, benefit is mapping of key and value pairing. Dictionary
keys must be immutable. Therefore Tuples can be keys but not lists. Can use keyword in for keys, but not values."""

my_dict = dict()
print(my_dict)

fruits = {"Apple": "Red", "Banana": "Yellow"}
print(fruits)

facts = dict()
facts["founded"] = 1776

print(facts["founded"])

del facts["founded"]

""" Dictionary contains a tuple, list, and dictionary. Tuple since GPS coordinates won't change, List since it could
change, and Dictionary since key value pairs is the best way to represent facts about NY. """

ny = {"location": (40.7128, 74.0059),
      "celebs": ["W. Allen", "Jay Z", "K. Bacon"],
      "facts": {"state": "NY", "country": "USA"}}
print(ny)


my_stats = {"height": 178,
            "weight": 86,
            "color": "blue",
            "band": "Tool"}

question = input("What do you want to know?")

if question in my_stats:
    result = my_stats[question]
    print(result)

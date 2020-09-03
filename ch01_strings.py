""" Strings
are iterable, index 0
are immutable"""

author = "Kafka"
print(author[-1])

book = "cat " + "in " + "the " + "hat"
print(book.capitalize())

gps = "Tom"*2
print(gps)

# Format to add values, can be multiple
writer = "William {}".format("Faulkner")
print(writer)


jump = """I jumped over the puddle. It was 12 feet!""".split(".")
print(jump)

# Join with space
words = ["The", "fox", "jumped", "over", "the", "fence."]
my_sentence = " ".join(words)
print(my_sentence)

# Strip the white space
s = "  The   "
s = s.strip()
print(s)

print("cat" in "cat in the hat")

# Escape character
print("She said \"Surely.\" ")

print("line 1\nline 2\nline 3")
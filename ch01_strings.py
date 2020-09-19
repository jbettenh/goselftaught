""" Strings
are iterable, index 0
are immutable"""

author = "Kafka"
print(author[-1])

book = "The" + "cat " + "in " + "the " + "hat"
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


"""" 
1. Print every character in the string "Camus". 
"""
ex1 = "Camus"
for c in ex1:
    print(c)


""" 
2. Write a program that collects two strings from a user, inserts them into the string "Yesterday I wrote a 
[response_one]. I sent it to [response_ two]!" and prints a new string.
"""
response_one = input("Enter a written item: ")
response_two = input("Enter a person: ")
story = "Yesterday I wrote a {}. I sent it to {}!".format(response_one, response_two)
print(story)


""" 
3. Use a method to make the string "aldous Huxley was born in 1894." grammatically correct by capitalizing the 
first letter in the sentence. 
"""


def grammar_fixer(sentence):

    return sentence.title()


bio = "aldous Huxley was born in 1894."
print(grammar_fixer(bio))

""" 
4. Take the string "Where now? Who now? When now?" and call a method that returns a list that looks like: 
["Where now?", "Who now?", "When now?"].
"""
lst = "Where now?. Who now?. When now?.".split(".")
print(lst)
""" 
5. Replace every instance of "s" in "A screaming comes across the sky." with a dollar sign. 
"""
src_str = "A screaming comes across the sky."
replace_a = src_str.replace("a", "@").replace("A", "@").replace("s", "$")
print(replace_a)


""" 
6. Use a method to find the first index of the character "m" in the string "Hemingway".
"""

author = "Hemingway".index("m")
print(author)



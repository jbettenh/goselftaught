
lotto_numbers = [9, 23, 8, 57, 12, 11]
print("Type q to quit")

while True:
    answer = input("Guess a number:")

    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("Please type a number or q to quit.")

    if answer in lotto_numbers:
        print("You guessed correctly!")
        break
    else:
        print("You guessed incorrectly!")


"""
2.
"""


list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
    for j in list2:
        mult = i * j
        list3.append(mult)

print(list3)

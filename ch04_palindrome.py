def is_palindrome(word):
    word = word.lower()
    return word[::-1] == word


result = is_palindrome("racecar")
print(result)
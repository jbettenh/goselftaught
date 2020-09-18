# 1. Remainder
def is_even(check_num):
    result = check_num % 2

    if result == 0:
        return True
    else:
        return False


if is_even(80):
    print('It is even!')
else:
    print('It is odd!')


# 2. Quotient
def apples(x, y):
    # can check if even with 2
    remainder = x/y
    print(f'Each person gets {remainder} apples.')


total_apples = 11
people = 2
apples(total_apples,people)


# 3. Raise to third power
print(f'2 raised to the third power is {2**3}')


def formula(a, b, c, e=5, m=100):
    return c*(a + b**e) - m


print(formula(4, 7, 2, 2, 50))


# Built-In Function convert to float
def mk_float(input_str):
    """

    :param input_str: string
    :return: float
    """
    try:
        return float(input_str)
    except ValueError:
        print("Could not convert the string to a float.")


c = mk_float('high')
print(c)


# Exception Handling
def mk_int(number):
    """

    :param number:
    :return:
    """

    try:
        return int(number)
    except ValueError:
        print('Please type an integer')


num = input("Type a number to convert to Integer:")
print(mk_int(num))


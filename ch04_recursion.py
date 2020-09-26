"""
Base Case: A condition that ends a recursive algorithm to stop it from continuing.
3 Laws of Recursion
1. Must have a base case
2. Must change its state and move towards base case
3. Must call itself, recursively
"""


def bottles_of_beer(bob):
    if bob < 1:
        print("""No more bottles of beer on the wall. No more bottles of beer.""")

        return
    tmp = bob
    bob -= 1

    print("""{} bottles of beer on the wall. {} bottles of beer. Take one down, pass it around, {} 
    bottles of beer on the wall.""".format(tmp, tmp, bob))

    bottles_of_beer(bob)


bottles_of_beer(99)


def print_to_zero(n):
    if n < 0:
        return
    print(n)

    print_to_zero(n-1)


print_to_zero(5)


""" Fibonacci Sequence
   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
   Fn = Fn-1 + Fn-2
   with seed values 
   F0 = 0 and F1 = 1.
"""


def parabola(t, n, f1, f2):
    if n == t:
        return
    else:
        fibonacci = f1 + f2
        print(fibonacci)
        f1 = f2
        f2 = fibonacci
        n += 1
        parabola(t, n, f1, f2)


print('--- Fibonacci ---')
parabola(9, 2, 0, 1)







"""
Module which defines a fizzbuzz function and then calls it
"""

def fizzbuzz(n):
    """
    Print every number from 1 to n, except when the number is a multiple of 3, 5 or both
    in which case print "fizz", "buzz", and "fizzbuzz" respectively
    
    Arg:
        n: The number to count to
    """
    for i in range(1, n+1):
        if i%3 == 0 and i%5 == 0:
            print("fizzbuzz")
        elif i%3 == 0:
            print("fizz")
        elif i%5 == 0:
            print("buzz")
        else:
            print(i)

fizzbuzz(50)

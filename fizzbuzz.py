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
    fizz_count = 1
    buzz_count = 1
    for i in range(1, n+1):
        if i/fizz_count == 3 and i/buzz_count == 5:
            print("fizzbuzz")
            fizz_count += 1
            buzz_count += 1
        elif i/fizz_count == 3:
            print("fizz")
            fizz_count += 1
        elif i/buzz_count == 5:
            print("buzz")
            buzz_count += 1
        else:
            print(i)

fizzbuzz(50)

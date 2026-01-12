"""
Module which defines fizzbuzz_factorial then calls it
"""

def fizzbuzz_factorial():
    """
    Ask user for a number and then calculate the sum of all multiples of 3 
    and 5 from 1 up to said number and print this
    """
    n = int(input("Give me a number laddy\n"))
    n_factorial = 0
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            n_factorial += i
    print("The sum of all multiples of 3 and/or 5 between 1 up to your number is "\
           + str(n_factorial))

fizzbuzz_factorial()

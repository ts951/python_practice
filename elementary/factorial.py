"""
Contains factorial function and calls it
"""

def factorial():
    """
    Ask user for a number and then calculate the factorial of said number and print this
    """
    n = int(input("Give me a number laddy\n"))
    n_factorial = 0
    for i in range(1, n+1):
        n_factorial += i
    print("The sum of all integers from 1 to your number is " + str(n_factorial))

factorial()

"""
Module containing function for providing sum of numbers 1 to a given number,
function for providing product of numbers 1 to a given number, and function
asking user for a number and then calling either of the previous functions at user's request.
"""

def sum_1_to_n(n):
    """
    Take n as input and return sum of all numbers from 1 to n.
    Assumes n is a number.
    """
    my_sum = 0
    for i in range(1, n+1):
        my_sum += i
    return my_sum

def product_1_to_n(n):
    """
    Take n as input and return product of all numbers from 1 to n.
    Assumes n is a number.
    """
    my_product = 1
    for i in range(1, n+1):
        my_product *= i
    return my_product

def sum_or_product_1_to_n():
    """
    Ask user for a number, as them for sum or product and then provide
    sum or product of all numbers from 1 to given number.
    """
    n = int(input("Gimme a number bruh.\n"))
    operation = input("Sum or product?\n").strip().lower()

    if operation == "sum":
        ans = sum_1_to_n(n)
    elif operation == "product":
        ans = product_1_to_n(n)
    else:
        print("That's not an accepted operation dude. I'm leaving.")
        return
    print("The " + operation + " of all numbers from 1 to " + str(n) + " is: " + str(ans))

sum_or_product_1_to_n()

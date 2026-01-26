"""
Module containing a variety of functions relating to lists and strings as outline in the 
"Lists, Strings" section of "https://adriann.github.io/programming_problems.html"
"""

def largest_element(a):
    """
    Returns the largest numerical element in the list "a" without just using .max()
    Returns None if  with at least one int or float
    
    :param a: input list to find the largest numerical element in
    """

    if not isinstance(a, list):
        print("Give me a list, not whatever that is.")
        return None

    max_a = None
    for element in a:
        if not isinstance(element, (int, float)):
            continue
        if max_a is None or element > max_a:
            max_a = element

    return max_a

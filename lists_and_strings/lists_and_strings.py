"""
Module containing a variety of functions relating to lists and strings as outline in the 
"Lists, Strings" section of "https://adriann.github.io/programming_problems.html"
"""

def largest_element(a):
    """
    Returns the largest numerical element in the list "a" without just using max()
    Returns None if there is not at least one int or float in "a"
    
    :param a: input list to find the largest numerical element in
    """

    if not isinstance(a, list):
        return None

    max_a = None
    for element in a:
        if not isinstance(element, (int, float)):
            continue
        if max_a is None or element > max_a:
            max_a = element

    return max_a

def reverse_list(a):
    """
    Reverse a given list without using reverse()
    
    :param a: Input list to be reversed
    """

    if not isinstance(a, list):
        return None

    reverse_a = [None] * len(a)
    curr_index = -1
    for element in a:
        reverse_a[curr_index] = element
        curr_index -= 1

    return reverse_a

def check_if_contains(check_element, a):
    """
    Check if an input list contains an input element and output
    True or False, without just sing "if check_element in a"
    
    :param check_element: Element to check a for
    :param a: List to check for presence of check_element
    """

    is_contained = False
    for element in a:
        if element == check_element:
            is_contained = True
            break

    return is_contained

def odd_elements(a):
    """
    Function that returns only the elements in odd positions
    (starting at 1, so index 0 is position one)
    
    :param a: Input list
    """

    if not isinstance(a, list):
        return None

    odd_a = []
    for i in range(1, len(a)+1):
        if i%2 != 0:
            odd_a.append(a[i-1])

    return odd_a

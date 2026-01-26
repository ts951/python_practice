"""
A series of test functions for each function in the module lists_and_strings.py
"""

from lists_and_strings import largest_element, reverse_list


def test_largest_element():
    """
    Test function for largest_element
    Should output 4, None, None, 2, and None for each test
    """
    print("largest_element tests:")
    test_cases = [[2, 4, 1, -1, -3],
                  ["ploops", "floops", "scloops"],
                  (1, 2, 3, 4, 5),
                  ["AA", 2, 1, "BB"],
                  [[5, -3, 2], [2, 1, -5]]]
    for a in test_cases:
        print(f"\ta = {a}\n\tLargest element = {largest_element(a)}")

def test_reverse_list():
    """
    Test function for reverse_list
    Should output the reverse of each of the inputs, 
    except when they are not lists, when it should output None
    """
    test_cases = [[1, 2, 3, 4, 5],
                  3,
                  ["a", 1, "b", 2, "c", 3]]
    print("reverse_list tests:")
    for a in test_cases:
        print(f"\ta = {a}\n\tReversed list = {reverse_list(a)}")

# Call test function(s) here
test_reverse_list()

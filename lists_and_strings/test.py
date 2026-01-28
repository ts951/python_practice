"""
A series of test functions for each function in the module lists_and_strings.py
"""

from lists_and_strings import largest_element, reverse_list, check_if_contains, odd_elements


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

def test_check_if_contains():
    """
    Test function for check_if_contains
    Should state that the 1st and 3rd test cases are contained in the test list
    and that the 2nd and 4th test cases are not containe din the test list
    """
    test_list = [1, "a", 2, "b", 3, "c"]
    test_cases = [2, 5, "b", "Hey!"]
    print("check_if_contains tests:")
    for test_case in test_cases:
        if check_if_contains(test_case, test_list):
            print(f"\t{test_case} is contained within {test_list}")
        elif not check_if_contains(test_case, test_list):
            print(f"\t{test_case} is not contained within {test_list}")

def test_odd_elements():
    """
    Test function for odd_elements
    Should output None, [1, 3, 5] and ["a", "c", "e"]
    """
    test_cases = ["Plip Plop",
                  [1, 2, 3, 4, 5, 6],
                  ["a", "b", "c", "d", "e"]]
    print("odd_elements tests:")
    for test_case in test_cases:
        print(f"\tThe odd elements in {test_case} are: {odd_elements(test_case)}")

# Call test function(s) here
test_odd_elements()

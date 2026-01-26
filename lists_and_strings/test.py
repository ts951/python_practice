"""
A series of test functions for each function in the module lists_and_strings.py
"""

from lists_and_strings import largest_element

def test_largest_element():
    """
    Test function for largest_element
    """
    print("largest_element tests:")
    test_cases = [[2, 4, 1, -1, -3],
                  ["ploops", "floops", "scloops"],
                  ["AA", 2, 1, "BB"],
                  [[5, -3, 2], [2, 1, -5]]]
    for a in test_cases:
        print(f"\ta = {a}\n\tLargest element = {largest_element(a)}")

# Call test function(s) here
test_largest_element()

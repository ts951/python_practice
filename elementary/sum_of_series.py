"""
Computes the sum of an alternating series where each element of the series equals
4*((-1)^(k+1))/(2k-1) where k ranges from 1 to 1 million.
In other words, it uses the Leibniz formula for pi!
"""

def apply_formula(k):
    """
    Function that returns 4*((-1)^(k+1))/(2k-1), where k is the input argument
    """
    return 4*((-1)**(k+1))/(2*k-1)

rolling_sum = 0
for k_val in range(1, 1000001):
    rolling_sum += apply_formula(k_val)

print(f"Behold! The sum is: {rolling_sum}")

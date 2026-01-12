"""
Script that prints every prime number until interrupted, printing
each one then waiting a 0.5s interval and printing the next
"""

import time

n = 2 # Start at 2, the first prime number

while True:
    is_prime = True # Set to true to start with then check whether prime or not
    for i in range(2, n):
        if n%i == 0:
            is_prime = False # Set to false since this would mean the number is not prime
            break
    if is_prime:
        print(n)
        time.sleep(0.5)
    n += 1

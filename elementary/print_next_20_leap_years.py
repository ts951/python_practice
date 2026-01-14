"""
Prints to the terminal the next 20 leap years following the current year.
"""

import datetime

year = datetime.datetime.now().year

if year%4 == 0:
    # Ensures the listed years do not start on the current year
    # if the current year happens to be a leap year
    first_leap_year = year + 4
else:
    first_leap_year = year + year%4

leap_years_str = str(first_leap_year)

for i in range(1, 19):
    leap_years_str += f", {first_leap_year + 4*i}"

# 20th year is added outside of the loop so it can say "and" before it
leap_years_str += f", and {first_leap_year + 4*19}"

print(f"The next 20 leap years following this year ({year}) are:")
print(leap_years_str)

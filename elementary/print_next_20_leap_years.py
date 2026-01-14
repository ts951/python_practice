import datetime

year = datetime.datetime.now().year

print(f"The next 20 leap years following this year ({year}) are:")

num_printed = 0
while num_printed < 20:
    year += 1
    if year%4 == 0:
        print(year)
        num_printed += 1
"""
Script that prints the 12 times table in the form of nested lists
"""

for i in range(0, 13):
    for j in range(0, 13):
        if i == 0 and j == 0:
            print("X", end="\t")
        elif i == 0:
            print(f"{j}", end="\t")
        elif j == 0:
            print(f"{i}", end="\t")
        else:
            print(f"{i*j}", end="\t")
    print()

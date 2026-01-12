"""
Contains definition of greet_alice_or_bob function and calls it
"""

def greet_alice_or_bob():
    """
    Ask user for name and print greeting addressing them by name if they are Alice or Bob.
    If not, spurn them for the wretches they are
    """

    name = input("What is thine name friend?\n").strip().lower().capitalize()
    if name in ("Alice", "Bob"):
        print("Ahh greetings " + name + ". It has been far too long.")
    else:
        print(name + "? Disgusting! Get away from me you wretch!")

greet_alice_or_bob()

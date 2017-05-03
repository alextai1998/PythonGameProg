"""
This program pluralizes the noun entered...or at least attempts to.
"""

numbers = {1: "One ", 2: "Two ", 3: "Three ", 4: "Four ", 5: "Five ", 6: "Six ", 7: "seven ", 8: "eight ", 9: "nine ", 10: "ten "}  # Text version of numbers
exceptions = {"man": "men", "fish": "fish", "roof": "roofs", "focus": "foci", "child": "children", "person": "people"}  # Lists out common exceptions

noun = input("Enter a noun! ")
num = int(input("How many? "))

if 1 < num <= 10:
    if noun in exceptions:
        print(numbers[num] + exceptions[noun])
        exit()
    elif noun[-1:] == "a" or noun[-1:] == "i" or noun[-1:] == "o" or noun[-1:] == "u" or noun[-1:] == "s" or noun[-1:] == "x" or noun[-1:] == "z" or noun[-1:] == "ch" or noun[-1:] == "sh":
        noun += "es"
    elif noun[-1:] == "f":
        noun = noun.replace("f", "ves")
    elif "oo" in noun:
        noun = noun.replace("oo", "ee")
    elif noun[-1:] == "y":
        noun = noun.replace("y", "ies")
    else:
        noun += "s"

print(numbers[num] + noun)

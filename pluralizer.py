"""
This program pluralizes the noun entered.
"""

numbers = {1: "One ", 2: "Two ", 3: "Three ", 4: "Four ", 5: "Five ", 6: "Six ", 7: "seven ", 8: "eight ", 9: "nine ", 10: "ten "}

noun = input("Enter a noun! ")
num = int(input("How many? "))

if 1 < num <= 10:
    if noun[-1:] == "a" or noun[-1:] == "i" or noun[-1:] == "o" or noun[-1:] == "u" or noun[-1:] == "s" or noun[-1:] == "x" or noun[-1:] == "z" or noun[-1:] == "ch" or noun[-1:] == "sh":
        noun += "es"
    else:
        noun += "s"

print(numbers[num] + noun)

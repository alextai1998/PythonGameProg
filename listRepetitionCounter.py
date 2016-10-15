"""
This program includes a function that counts how many times a word appears in a text.
"""


def count(a):
    # A function that counts how many times a word appears in a text
    # conditions: 'a' should be a string
    a = a.lower()
    list_a = a.split()
    list_b = []
    counter = []

    for j in list_a:
        if j in list_b:
            counter[list_b.index(j)] += 1
        else:
            list_b.append(j)
            counter.append(1)

    for i in range(len(list_b)):
        print("Number of occurrences of '" + list_b[i] + "' = " + str(counter[i]))


value = "Hello HELLO hello alex ALEX Alex jason tai Tai"


count(value)

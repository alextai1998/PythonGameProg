"""
This program includes a function that counts how many times a word appears in a text.
"""


def count(a):
    alist = a
    blist = []
    counter = []

    for j in alist:
        if j in blist:
            counter[blist.index(j)] += 1
        else:
            blist.append(j)
            counter.append(1)

    for i in range(len(blist)):
        print("Number of occurrences of '" + blist[i] + "' = " + str(counter[i]))


value = input("Enter a string of words: ")
value = value.lower()

mlist = value.split()


print(mlist)

count(mlist)

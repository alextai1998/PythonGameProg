"""
This program includes a function that combines two lists by alternating taking elements
It will also validate that the inputs have the same length before attempting to join them.
"""


def combine(a, b):
    for i in range(0, len(a)):
        clist.append(a[i])
        clist.append(b[i])
    print(clist)

alist = []
blist = []
clist = []

while True:
        value = input("Enter the values of the first list. (or enter nothing to stop.): ")
        if value == "":
            break
        alist.append(value)  # list concatenation

while True:
        value = input("Enter the values of the second list. (or enter nothing to stop.): ")
        if value == "":
            break
        blist.append(value)  # list concatenation

if len(alist) == len(blist):
    combine(alist, blist)
else:
    print("")
    print("Please make sure the two lists have the same number of elements!")


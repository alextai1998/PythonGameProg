"""
This program prints the accumulated sum of a list.
"""

acc = 0
mlist = []
acclist = []
while True:
    value = input("Enter the value that should be accumulated. (or enter nothing to stop.): ")
    if value == "":
        break
    mlist.append(value)  # list concatenation

for value in mlist:
        acc += int(value)
        acclist.append(acc)

print(acclist)

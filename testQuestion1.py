"""
binary = 2

while sum(int(x) for x in str(binary)) > len(str(binary))-2:
    binary = input("Enter only 1's and 0's (10111) ")
dec = 0
for c in range(len(binary)):
    dec += int(str(binary[c]))*(2**c)
print("Decimal number is %r" % dec)
"""

binary = 2

while sum(int(x) for x in str(binary)) > len(str(binary))-2:
    binary = input("Enter only 1's and 0's (10111) ")
dec = 0
for c in range(len(binary)):
    dec += int(str(binary[c]))*(2**(len(binary) - 1 - c))
print("Decimal number is %r" % dec)

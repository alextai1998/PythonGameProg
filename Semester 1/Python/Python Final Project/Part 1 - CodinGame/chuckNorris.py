"""
This program takes an incoming message as input and displays as output the message encoded using Chuck Norris’ method.
"""

msg = input()
msgList = []

for c in msg:  # converts c to a 7digit 0 left padded binary code
    msgList.append('{0:07b}'.format(ord(c)))

prev = None
count = 0  # sets how many iterations of same character
for c in "".join(msgList):
    if c != prev:  # determines the next message
        print(("0" * count) + (" " if count else "") + ("00 " if c == "0" else "0 "), end="")
        count = 1
    else:
        count += 1
    prev = c  # updates previous that contains the last of msgList that is either 0 or 1
print("0" * count, end="")

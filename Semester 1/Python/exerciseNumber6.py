"""
This program calculates the average of all the inputs.
"""

vInput = 0
vAcc = 0
iteration = 1

while True:
    vInput = input("Enter your value (0-100), any letter to finalize: ")
    if isinstance(vInput, int):
        if 0 <= vInput <= 100:
            vAcc += vInput
            iteration += 1
            print(vAcc / iteration)
    if isinstance(vInput, str):
        break
print(vAcc / iteration)

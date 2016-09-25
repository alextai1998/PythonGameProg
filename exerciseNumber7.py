"""
This program calculates the average of all the inputs.
"""

vInput = 0
vAcc = 0
iter = 0

while type(vInput) == int:
    vInput = int(input("Enter your value (0-100), any letter to finalize: "))
    if 0 <= vInput <= 100:
        vAcc += vInput
        iter += 1
    for i in range(1, iter+1):
        if i == iter:
            print(vAcc / i)

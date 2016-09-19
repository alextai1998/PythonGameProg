"""
Draw the flow diagram and write a program that counts the occurrences of getting a 6 on a dice out of 1000 rolls.
Calculate the probability of the event “obtaining a 6 in a dice roll” from the experiment. Is it what you expected?.
You can generate random numbers in Python to simulate the dice rolling.
"""


import random

num = 0
for i in range(1000):
    j = random.randint(1,6)
    print(i+1, j)
    if (j == 6):
        num = num + 1
prob = (num/10000)*100
eprob = (1/6)*100

print("There are " + str(num) + " 6 in total.")
print("The probability of getting a 6 out of 1000 rolls is " + str(prob) + "%.")
print("The expected probability of getting a 6 out of 1000 rolls is " + str(eprob) + "%.")

#compare the experimental value and the expected value
if 13.66 <= prob <= 19.66:
    print("Yes. This is the value I am expecting.")
else:
    print("No. This is not the value I am expecting.")
diff = abs(prob - eprob)
print("The difference of the experimental value and the expected value is: " + str(diff) + "%.")

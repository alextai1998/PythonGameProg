"""
This program prints all the numbers from 0 to 6 except 3 and 6.
"""

for i in range(7):
    if i == 0:
        print(i)
    if i % 3 != 0:
        print(i)
        continue  # Skips over non-prime numbers

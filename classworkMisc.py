"""
hello2 = [x**2 for x in range(11) if x % 2 != 0]
print(hello2)
"""

"""
def split_string(a):
    return a.split()  # Splitting the string Value

sentence = "the quick brown fox jumps over the lazy dog"
alist = split_string(sentence)
blist = [x for x in alist if x == "the"]
print(len(blist))
"""

"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [x for x in a if x % 2 == 0]
print(b)
"""

"""
import alexLib as al

al.findNextWord("i", al.readTxt("lyrics.txt"))
"""

"""
import numpy as np
import matplotlib.pyplot as plt

t = [.5*x-10 for x in range(200)]
points = [(x, y) for x in t for y in t if np.sqrt(x**2+y**2) < 10]
for x, y in points:
    plt.scatter(x, y, marker="x", c="turquoise")

plt.show()
"""

"""
import os

systemFiles = [filename for filename in os.listdir("/Users/alextai/Desktop") if filename.startswith("~")]
print(systemFiles)
"""

"""
mapping = {1: 22.5, 8: 13.4, 10: 12.1}
hello = [v for k, v in mapping.items()]
acc = 0
for v in hello:
    acc += v
print(acc)
print(len(mapping))

print(acc / (len(mapping)))
"""

"""
b = {"video": 0, "music": 23}
k = list(b.keys())

print(k[0])
"""

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

import alexLib as al

al.findNextWord("i", al.readTxt("lyrics.txt"))

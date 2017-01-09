eng2spa = {"uno": "one", "dos": "two", "tres": "three", "cuatro": "four", "cinco": "five", "seis": "six",
           "siete": "seven", "ocho": "eight", "nueve": "nine", "diez": "ten"}


"""
eng2spa.__delitem__("one")  # Removes the value stored in the key "one"
eng2spa.clear()  # Empties the dictionary
eng2spa.copy()
eng2spa.get("dos") # Similar to calling the value, but allows you to set default


for v in eng2spa.items():
    print(v)  # Prints keys and values as pairs

for v in eng2spa.keys():
    print(v)  # Prints keys

for v in eng2spa.value():
    print(v)  # Prints values
"""


# del, clear, copy, fromkeys, get, items, keys, values

hello = {}

seq = ("a", "b")

dict = hello.fromkeys(seq,)  # Param: accepts a set of keys; used to rewrite multiple values

print(dict)

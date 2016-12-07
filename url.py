import urllib.request
import alexLib as al

req = urllib.request.Request("https://archive.org/stream/TheChroniclesOfNarnia/The%20Chronicles%20of%20Narnia_djvu.txt")

response = urllib.request.urlopen(req)
the_page = response.read().decode("utf-8")

punctuation = "+_)(*&^%$#@!~|}{\"[]\;\',./:?><`-="

glossary = the_page.lower().split()

for w in glossary:
    if "<pre>" in w:
        start = glossary.index(w)
    if "</pre>" in w:
        finish = glossary.index(w)

narnia = glossary[start:finish]

for index, word in enumerate(narnia):
    for char in narnia[index]:
        if char in punctuation:
            narnia[index] = word.replace(char, "")


iterations = {}
filteredNarnia = []

for x in narnia[1:100]:
    if len(x) == 5:
        filteredNarnia.append(x)

for x in filteredNarnia[1:100]:
    if x in iterations.keys():
        iterations[x] += 1
    else:
        iterations[x] = 1

al.printMenu(iterations, 22, 16, "Words")


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
punctLessNarnia = []

for index, word in enumerate(narnia):
    for char in word:
        if char in punctuation:
            word = word.replace(char, "")
    punctLessNarnia.append(word)


wordBank = {}
filteredNarnia = []

for x in punctLessNarnia:
    if len(x) == 5:
        filteredNarnia.append(x)

for x in filteredNarnia:
    if x in wordBank.keys():
        wordBank[x] += 1
    else:
        wordBank[x] = 1

wblist = [(k, v) for k, v in wordBank.items()]

# sortList = al.preBubble(wblist)
# print(sortList)
#
# al.printMenu(sortList, 22, 16, "Words")


al.preBubble(wblist)
al.insertionSort(wblist)

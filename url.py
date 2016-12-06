import urllib.request
import alexLib as al

req = urllib.request.Request("https://archive.org/stream/TheChroniclesOfNarnia/The%20Chronicles%20of%20Narnia_djvu.txt")

response = urllib.request.urlopen(req)
the_page = response.read().decode("utf-8")

glossary = the_page.lower().split()

for w in glossary:
    if "<pre>" in w:
        start = glossary.index(w)
    if "</pre>" in w:
        finish = glossary.index(w)

narnia = glossary[start:finish]

iterations = {}

for x in narnia[1:100]:
    if "x" not in iterations.keys():
        iterations[x] = narnia.count(x)

al.printMenu(iterations, 22, 16, "Words")

import urllib.request

req = urllib.request.Request("https://archive.org/stream/TheChroniclesOfNarnia/The%20Chronicles%20of%20Narnia_djvu.txt")

response = urllib.request.urlopen(req)
the_page = response.read().decode("utf-8")

glossary = the_page.split()

for w in glossary:
    if "<pre>" in w:
        start = glossary.index(w)
        print(start)
    if "</pre>" in w:
        finish = glossary.index(w)
        print(finish)

narnia = glossary[start:finish]

print(narnia[1:100])

# mystring = "This sentence is a simple sentence."
# result = mystring.split()
# print(result)
# print("The total number of words is: " + str(len(result)))
# print("The word 'sentence' occurs: " + str(result.count("sentence")))

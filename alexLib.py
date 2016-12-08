"""
This program serves as a library for all of the functions Alex wrote in class.
"""


def combine(a, b):
    # A function that combines two lists by alternating taking elements
    # It will also validate that the inputs have the same length before attempting to join them.#
    clist = []
    if len(alist) == len(blist):
        for i in range(0, len(a)):
            clist.append(a[i])
            clist.append(b[i])
    else:
        print("Error: arguments need to be in the same length!")
    return clist


def multiply(a):
    # A function that multiplies all the numbers in a list
    # The function also skips non-numeric values.
    # conditions: 'a' should be a list
    product = 1
    for value in a:
        try:
            product *= int(value)
        except ValueError:
            continue
    return product


def odd_positions(a):
    # A function that returns a list of all the elements on odd positions in a list
    # conditions: 'a' should be a list
    mlist = [a[i] for i in range(1, len(a), 2)]
    return mlist


def split_string(a):
    # A function that takes a string and creates a list with single words as elements
    # conditions: 'a' should be a string
    return a.split()


def print_frame(a):
    # A function that takes a list of strings and prints them, one per line, in a rectangular frame
    # conditions:'a' should be a list
    l_element = max(a, key=len)  # Finds the longest element
    x = len(l_element)  # Finds the length of the longest element
    max_stars = x + 7  # Determines the number of stars in the first/last row

    print("*" * max_stars)
    for each in a:
        num_space = max_stars - (len(each) + 3)  # Determines the number of spaces needed to align the last asterisk
        print("* " + each + " " * num_space + "*")
    print("*" * max_stars)


def count(a):
    # A function that counts how many times a word appears in a text
    # Returns a list with WORD in even positions, and OCCURRENCES in odd positions.
    # conditions: 'a' should be a string
    a = a.lower()
    list_a = a.split()
    list_b = []
    list_c = []

    counter = []

    for j in list_a:
        if j in list_b:
            counter[list_b.index(j)] += 1
        else:
            list_b.append(j)
            counter.append(1)

    for i in range(len(list_b)):
        list_c.append(list_b[i])
        list_c.append(counter[i])

    return list_c


def readTxt(fileName):
    """
    Reads and return a text in a file
    :param filepath: address to the input file
    :return: list
    """
    f = open(fileName, "r")
    returnText = f.read().lower()
    f.close()
    return returnText.split()


def findNextWord(key, text):
    """
    Find the next word of a given key word
    :param key: word of interest
    :param text: the text to study [type: list]
    :return: a list with the following words
    """
    nextWordlist = []
    frequencylist = []

    for idx, word in enumerate(text):
        if word == key:
            nxtwrd = text[idx+1]
            if nxtwrd in nextWordlist:
                frequencylist[nextWordlist.index(nxtwrd)] += 1
            else:
                nextWordlist.append(nxtwrd)
                frequencylist.append(1)

    return nextWordlist, frequencylist


def probOcurrence(count):
   """
   Calculates the accumulated probability of an event
   :param count: a list with event's count
   :return: a list with probabilities
   """
   nEvents = sum(count)
   prob = [1.0*x/nEvents for x in count]
   density = []
   total = 0

   for p in prob:
       total += p
       density.append(total)

   return density


def randomWord(words, density):
   """
   Calculates the accumulated probability of an event
   :param words, density: words list returned, density returned from prev function
   :return: a list with probabilities
   """
   import random as rn
   n = rn.random()
   idx = 0
   while n > density[idx]:
       idx += 1

   return words[idx]


def printMenu(items, lwidth, rwidth, title):
    """
    Prints a dictionary's keys and values in a menu format
    :param items: dictionary
    :param lwidth: int
    :param rwidth: int
    :param title: string
    :return: None
    """
    x = title

    print(x.center(lwidth+rwidth, "-"))

    for element in items:
        print(element[0].ljust(lwidth, ".") + str(element[1]).rjust(rwidth, "."))


def bubbleSort(items):
    """
    Simple sorting algorithm
    :param items: list
    :return: two lists
    """
    index = list(range(len(items)))
    for i in range(len(items)):
        for j in range(len(items)-i-1):
            if items[j] < items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                index[j], index[j+1] = index[j+1], index[j]
    return items, index


def preBubble(wordBankList):
    """
    Return the sorted bank of words
    :param wordBankList: list of unsorted tuples
    :return: list of tuples
    """
    items = [element[1] for element in wordBankList]
    items_sort, index = bubbleSort(items)
    sortWordBank = [wordBankList[i] for i in index]
    return sortWordBank


def insertionSort(items):
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
    return items

items = [5, 9, 7, 2]

print(insertionSort(items))

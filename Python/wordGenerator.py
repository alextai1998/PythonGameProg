import alexLib as al

key = (input("Please enter a word: "))
num = (int(input("Please enter the number of words you want: ")))

sampleText = "helloLyrics.txt"
text = al.readTxt(sampleText)
output = []

for i in range(num):
    nextWordList, frequency = al.findNextWord(key, text)
    density = al.probOcurrence(frequency)
    prob = al.probOcurrence(density)
    aword = al.randomWord(nextWordList, prob)
    output.append(aword)

print(output)

import nltk
from nltk.corpus import stopwords

cachedStopWords = stopwords.words("english")

def removeStopWords(text):
        return ' '.join([word for word in text.split() if word not in cachedStopWords])

count = 0

with open("ShuffledOP.txt") as inputFile:
	for line in inputFile:
		cardData = line.rstrip().lstrip().split("\t")
		with open(cardData[0] + ".txt", "a") as outputFile:
			print "Placed: ", cardData[0]
			count += 1
			print count
			outputFile.write(removeStopWords(cardData[1]) + "\n")

print count
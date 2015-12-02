import nltk
from nltk.corpus import stopwords

cachedStopWords = stopwords.words("english")

def removeBadWords(text):
	return ' '.join([word for word in text.split() if (word not in cachedStopWords) and (word.isalpha()) and (len(word) > 1)])

count = 0
with open("ShuffledOP.txt", "r") as inputFile:
	with open("NewShuffledFile.txt", "w") as outputFile:
		for line in inputFile:
			line = line.rstrip().lstrip().decode('utf-8')
			new_line = line.split("\t")
			opLine = new_line[0] + "\t" + removeBadWords(new_line[1].lower()) + "\n"
			outputFile.write(opLine.encode('utf-8'))
			count += 1
print count



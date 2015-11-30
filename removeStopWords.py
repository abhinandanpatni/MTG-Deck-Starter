import nltk
from nltk.corpus import stopwords

cachedStopWords = stopwords.words("english")

def removeStopWords(text):
        return ' '.join([word for word in text.split() if word not in cachedStopWords])

with open('output.txt', 'r') as textToModify:
	with open('stopWordsRemoved.txt', 'w') as stopRemoved:
		for line in textToModify:
			line = line.lstrip().rstrip()
			lineText = line.split('text:')[1]
			lineText = removeStopWords(lineText)
			stopRemoved.write(line+'\t'+'StopWordsRemoved:'+lineText+'\n')



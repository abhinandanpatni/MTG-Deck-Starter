from sklearn.feature_extraction.text import CountVectorizer
import nltk
from nltk.corpus import stopwords

cachedStopWords = stopwords.words("english")

count = 0
colorList = ["White", "Green", "Blue", "Black", "Red"]

corpus = list()

for index, color in enumerate(colorList):
	string = ""
	with open(color + ".txt", "r") as inputFile:
		for line in inputFile:
			string += line.lower().decode('utf-8')
		string.replace("\n", " ")
		corpus.append(string)


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print vectorizer.vocabulary_.get('destroy')
print X.shape

with open("NewShuffledFile.txt", "r") as inputFile:
	with open("svm_light_file.final", "w") as outputFile:
		for line in inputFile:
			line = line.rstrip().lstrip().decode('utf-8')
			new_line = line.replace("\t", " ").split(' ')
			op_line = ""
			op_line += str(colorList.index(new_line[0])+1) + " "
			featsList = list()
			for each in new_line[1:]:
				featsList.append(vectorizer.vocabulary_.get(each.lower()))
			featsList = sorted(set(featsList))
			featsList = ' '.join(str(x)+":"+str(float(1)) for x in featsList)

			op_line += featsList
			
			outputFile.write(op_line.rstrip() + "\n")
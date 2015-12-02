from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

colorList = ["White", "Green", "Blue", "Black", "Red"]
corpus = list()

for index, color in enumerate(colorList):
	string = ""
	with open("../" + color + ".txt", "r") as inputFile:
		for line in inputFile:
			string += line
		string.replace("\n", " ")
		corpus.append(string)


vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
print X.shape

transformer = TfidfTransformer()
tfidf_transformer = transformer.fit_transform(X)


print tfidf_transformer.shape

clf = MultinomialNB().fit(tfidf_transformer, corpus)

toPredict = ["Return creatures from graveyard", "Deal damage to opponent", "Gain life"]

new_counts = vectorizer.transform(toPredict)
new_tfidf = transformer.transform(new_counts)

predicted = clf.predict(new_tfidf)

for ability, color in zip(toPredict, predicted):
	print('%r => %s' %(ability, colorList[corpus.index(color)]))

# analyze = vectorizer.build_analyser()
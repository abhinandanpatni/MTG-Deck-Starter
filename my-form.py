from flask import Flask
from flask import request
from flask import render_template
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)

@app.route('/')
def my_form():
	return render_template("MTG_Strategizer.html")

@app.route('/', methods=['POST'])
def my_form_post():

	text = request.form['text']
	text = text.split(",")

	colorList = ["White", "Green", "Blue", "Black", "Red"]
	corpus = list()

	for index, color in enumerate(colorList):
		string = ""
		with open(color + ".txt", "r") as inputFile:
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

	toPredict = text

	new_counts = vectorizer.transform(toPredict)
	new_tfidf = transformer.transform(new_counts)

	predicted = clf.predict(new_tfidf)

	processed_text = ""
	for ability, color in zip(toPredict, predicted):
		processed_text += ability + " => " + colorList[corpus.index(color)] + "</br>"

	return processed_text

if __name__ == '__main__':
	app.debug = True
	app.run()

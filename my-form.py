from flask import Flask
from flask import request
from flask import render_template
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

app = Flask(__name__)

def makeResponse(toPredict, predicted):
	allLines = list()
	with open("templates/MTG_Strategizer.html") as outputFile:
		allLines = outputFile.readlines()
	pageBeginning = allLines[0:22]
	pageEnd = allLines[23:]
	# returnStr = ''
	table = "<br/><h1>Your Results Are:</h1><br/><table align=\"center\" text-align=\"center\" width=\"75%\" class=\"table table-striped\" >\n"
	for (query,result) in zip(toPredict, predicted):
		table += "<tr>\n<td align=\"center\" ><h2>"+query+"</h2></td><td><img src=\"/static/"+result.lower()+".png\" width=\"100px\" height=\"100px\" /></td></tr>"
		# returnStr += "\n<p>"+query+" "+result+"</p>\n"
		# returnStr += "\n<p>Result"+predicted[0]+"</p>"
	table += "\n</table>\n"
	return ' '.join(pageBeginning)+table+' '.join(pageEnd)

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
	predictedColors = list()
	for ability, color in zip(toPredict, predicted):
		processed_text += ability + " => " + colorList[corpus.index(color)] + "</br>"
		predictedColors.append(colorList[corpus.index(color)])

	responseHTML = makeResponse(toPredict, predictedColors)

	return responseHTML
	#return render_template("MTG_Strategizer.html")

if __name__ == '__main__':
	app.debug = True
	app.run()

from nltk import NaiveBayesClassifier
from nltk.corpus import stopwords

stopset = list(set(stopwords.words('english')))

def word_feats(words):
    return dict([(word, True) for word in words.split() if word not in stopset])

training = []
with open('../Training.txt', 'r') as trainFile:
	for line in trainFile:
		line = line.decode('utf-8')
		line = line.rstrip().lstrip().split('\t')
		training.append((word_feats(line[1]), line[0]))

testing = []
with open('../Testing.txt', 'r') as testFile:
	for line in testFile:
		line = line.decode('utf-8')
		line = line.rstrip().lstrip().split('\t')
		testing.append((word_feats(line[1]), line[0]))

classifier = NaiveBayesClassifier.train(training)

correct = 0
allLines = 0

for line in testing:
	if classifier.classify(line[0]) == line[1]:
		correct += 1
	allLines += 1

print "Accuracy: ", float(correct)/allLines
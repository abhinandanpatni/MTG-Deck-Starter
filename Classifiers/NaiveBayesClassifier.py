from textblob.classifiers import NaiveBayesClassifier
import nltk

training = []
with open('../Training.txt', 'r') as trainFile:
	for line in trainFile:
		line = line.decode('utf-8')
		line = line.rstrip().lstrip().split('\t')
		training.append((line[1], line[0]))

testing = []
with open('../Testing.txt', 'r') as testFile:
	for line in testFile:
		line = line.decode('utf-8')
		line = line.rstrip().lstrip().split('\t')
		testing.append((line[1], line[0]))

classifier = NaiveBayesClassifier(training)

for line in testing:
	print classifier.classify(line[0]), line[1]

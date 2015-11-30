import string
from string import punctuation

with open('output.txt', 'r') as oldOP:
	with open('OutputStage1.txt', 'w') as  newOP:
		exclude = set(string.punctuation)

		for line in oldOP:
			line = line.replace('colors:[', '')
			line = line.replace(']', '')
			line = line.replace('text:', '')
			line = line.replace('\'', '')
			line = ''.join(ch for ch in line if ch not in exclude)
			colors = line.split('\t')[0]
			rules = line.split('\t')[1]
			if len(colors.split(' ')) > 1:
				for color in colors.split(' '):
					lineN = color + '\t' + rules
					newOP.write(lineN)
			else:
				newOP.write(line)

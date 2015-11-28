import json
import os

outputFile = "output.txt"
errorFile = "error.json"
path = "DataFiles/"

files = 0
colorless = 0

for filename in os.listdir(path):
	if filename.endswith(".json"):
		with open(path+"/"+filename, "r") as ipFile:
			files += 1
			data = json.load(ipFile)

		with open(outputFile, "a") as opFile:
			for i in range(len(data["cards"])):
				x = data["cards"][i]
				if "colors" in x and "text" in x:
					x["colors"] = x["colors"].encode("utf-8") if type(x["colors"]) is not list else [y.encode("utf-8") for y in x["colors"]]
					x["text"] = x["text"].encode("utf-8")
					opFile.write( "colors:" + str(x["colors"]) + "\t" + "text:" + str(x["text"]).replace("\n", " ") +"\n" )
					# print i
				elif "colors" not in x:
					colorless += 1
				i += 1

print colorless, files

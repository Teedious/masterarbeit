import pandas as pd
import os
import math

files = list(filter(lambda name: name.endswith(".csv"),os.listdir("performance/measurements/main")))
print(files)

for file in files:
	print(file)
	df = pd.read_csv("performance/measurements/main/"+file)
	for name, values in df.iteritems():
		df[name] = values.mean()
		df.rename(columns = {name:'avg '+name}, inplace = True)
	df = df.drop(list(range(1,len(df))))
	df.to_csv("performance/measurements/main/avg/main-avg-"+file, index=False)

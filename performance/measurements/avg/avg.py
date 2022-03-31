import pandas as pd
import os
import math

files = list(filter(lambda name: name.endswith(".csv"),os.listdir("performance/measurements")))
print(files)

def my_fun(x):
	a = x.iloc[1] - x.iloc[0]
	if math.isnan(a):
		a = x.iloc[0]
	return int(a)

for file in files:
	print(file)
	df = pd.read_csv("performance/measurements/"+file)
	for name, values in df.iteritems():
		df[name] = values.mean()
		df.rename(columns = {name:'avg '+name}, inplace = True)
	df = df.drop(list(range(1,len(df))))
	df.to_csv("performance/measurements/avg/avg-"+file, index=False)

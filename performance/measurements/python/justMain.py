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
	i = 0
	j = 0
	for index, row in df.iterrows():
		key= df.columns[0]
		val = row[key]
		if 25 <= val < 26:
			i = index
		if 54 <= val < 55:
			j = index+1

	df = df.drop(list(range(j,len(df))))
	df = df.drop(list(range(0,i)))

	df.to_csv("performance/measurements/main/main-"+file, index=False)

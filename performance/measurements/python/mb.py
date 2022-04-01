import pandas as pd
import os
import math

files = list(filter(lambda name: name.endswith("mem.csv"),os.listdir("performance/measurements")))
print(files)

def my_fun(x):
	return '%8.3f' % (round(x / 1000000,3))

for file in files:
	print(file)
	df = pd.read_csv("performance/measurements/"+file)
	for name, values in df.iteritems():
		if name == 'Uptime (ms)':
			continue
		df[name] = values.apply(my_fun)
	df.columns = df.columns.str.replace('bytes', 'MB')
	print(df)
	df.to_csv("performance/measurements/new-"+file, index=False)

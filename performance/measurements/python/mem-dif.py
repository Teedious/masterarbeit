from unittest import skip
import pandas as pd
import os
import math
import numpy as np

files = list(filter(lambda name: name.endswith("mem.csv"),os.listdir("performance/measurements")))
print(files)

def my_fun(x):
  a = x.iloc[1] - x.iloc[0]
  if a <= 0:
    return np.nan
  return a

for file in files:
  print(file)
  df = pd.read_csv("performance/measurements/"+file)
  for name, _ in df.iteritems():
    print(name)
    if name == 'Uptime (ms)':
      continue
    df[name] = df[name].rolling(window=2).apply(my_fun)
    df.rename(columns = {name:'dif pos '+name}, inplace = True)
  print(df)
  df.to_csv("performance/measurements/mem-dif/dif-pos-"+file, index=False)
  
  for name, _ in df.iteritems():
    print(name)
    if name == 'Uptime (ms)':
      continue
    df[name] = df[name].mean(skipna=True)
    df.rename(columns = {name:'avg '+name}, inplace = True)
  df = df.drop(list(range(1,len(df))))
  print(df)
  df.to_csv("performance/measurements/mem-dif/avg-dif-pos-"+file, index=False)


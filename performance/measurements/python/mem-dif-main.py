from unittest import skip
import pandas as pd
import os
import math
import numpy as np

the_dir = "performance/measurements/main"
files = list(filter(lambda name: name.endswith("mem.csv"),os.listdir(the_dir)))
print(files)

def my_fun(x):
  a = x.iloc[1] - x.iloc[0]
  if a <= 0:
    return np.nan
  return a

for file in files:
  print(file)
  df = pd.read_csv(the_dir+"/"+file)
  for name, _ in df.iteritems():
    print(name)
    if name == 'Uptime (ms)':
      continue
    df[name] = df[name].rolling(window=2).apply(my_fun)
    df.rename(columns = {name:'dif pos '+name}, inplace = True)
  print(df)
  df.to_csv(the_dir+"/mem-dif/dif-pos-"+file, index=False)
  
  for name, _ in df.iteritems():
    print(name)
    if name == 'Uptime (ms)':
      continue
    df[name] = df[name].mean(skipna=True)
    df.rename(columns = {name:'avg '+name}, inplace = True)
  df = df.drop(list(range(1,len(df))))
  df = df.round(3)
  print(df)
  df.to_csv(the_dir+"/mem-dif/avg-dif-pos-"+file, index=False)


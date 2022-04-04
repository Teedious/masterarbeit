from unittest import skip
import pandas as pd
import os
import math
import numpy as np

files = list(filter(lambda name: name.endswith(".csv"),os.listdir("performance/measurements")))
print(files)

def my_fun(x):
  return x / 1000.0

for file in files:
  print(file)
  df = pd.read_csv("performance/measurements/"+file)
  if 'gpu' in file:
    continue

  df[df.columns[0]] = df[df.columns[0]].apply(my_fun)
  df.columns = df.columns.str.replace('time (ms)', 'time (s)', regex=False)
  print(df)
  df.to_csv("performance/measurements/"+file, index=False)


import pandas as pd
import os
import math

files = list(filter(lambda name: name.endswith(".csv"),os.listdir(".")))
print(files)

def my_fun(x):
  a = x.iloc[1] - x.iloc[0]
  if math.isnan(a):
    a = x.iloc[0]
  return int(a)

for file in files:
  print(file)
  df = pd.read_csv(file)
  df["a"] = df['fps'].rolling(window=2).apply(my_fun)
  df.rename(columns = {'fps':'total frames', 'a':'fps'}, inplace = True)
  df['fps'][0] = df['total frames'][0]
  df['fps'] = df['fps'].apply(int)
  df.to_csv('new'+file, index=False)

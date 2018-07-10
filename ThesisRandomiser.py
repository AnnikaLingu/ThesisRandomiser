from random import shuffle
import pandas as pd

infile = "List_ALL_180710.csv"

df=pd.read_csv(infile, sep=',',header=0)
df.values


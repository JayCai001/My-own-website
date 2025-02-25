import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataframe = pd.read_csv("python/data.csv")

def handleRate(value):
  value = str(value).split('/')
  value = value[0]
  return float(value)

dataframe['rate'] = dataframe['rate'].apply(handleRate)

print(dataframe['rate'].head())

sns.countplot(x = dataframe['listed_in(type)'])
plt.xlabel("Type of restaurant")
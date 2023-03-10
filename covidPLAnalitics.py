import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

covid_file = '/content/bigData.csv' 
df_gc = pd.read_csv(covid_file) # reading file
print(df_gc)

df_gc.columns # showing columns

len(df_gc) # lenght of data frame

df_gc.describe()

count_category = df_gc['hospi'].value_counts()
print(count_category) # unique values

df_gc['hospi'].value_counts(ascending = True) # unique values (ascending)

plt.plot(df_gc['hospi'], 'g--')
plt.show # amount of hospitalized people

plt.plot(df_gc['łóż'], 'r--')
plt.show # amount of beds for hospitalized people

plt.plot(df_gc['zmian'], 'p--')
plt.show # changes from day to day

plt.plot(df_gc['respL'], 'y--')
plt.show # amount of respirators

plt.plot(df_gc['respSC'], 'g--')
plt.show # amount of respirators with hospitalized people with critical condition

plt.plot(df_gc['zmian.1'], 'g--')
plt.show # changes from day to day

# days where amount of hospitalized where above 1000
hospi_Df = df_gc[(df_gc.hospi >= 1000)]
print(hospi_Df)

# mean from days where amount of hospitalized where above 1000
hospi_mean = df_gc[["łóż","%zaj"]].mean(axis=1)
plt.scatter(hospi_mean, df_gc["zmian"])
plt.show()
# %matplotlib inline

# days where amount of respiartos was occupied with hospitalized people with critical condition
resp_Df = df_gc[(df_gc.respSC) <= 100]
print(resp_Df)

# mean from days where amount of respiartos was occupied with hospitalized people with critical condition
resp_mean = df_gc[["respSC", "respL"]].mean(axis=1)
plt.scatter(resp_mean, df_gc["zmian.1"])
plt.show()
# %matplotlib inline

df_gc.corr(method='pearson')

df_gc.corr(method='kendall')

df_gc.corr(method='spearman')

hospi_corr = hospi_Df.corr()
sns.heatmap(hospi_corr)

resp_corr = resp_Df.corr()
sns.heatmap(resp_corr)


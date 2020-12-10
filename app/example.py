import pandas as pd

pd.set_option('display.max_columns', None)

data = {'name': ['Anne', 'John', 'Beth'], 'age': [23, 18, 86]}
df = pd.DataFrame(data, columns=['name','age'])

print(df.info())

df.to_csv('output/example.csv', sep=';', index=False)
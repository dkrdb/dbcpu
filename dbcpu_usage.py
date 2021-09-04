import pandas as pd

file_name = 'C:\DBA\Python\estudos\/arquivos\/binary.csv'

df = pd.read_csv(file_name)

print(df)

file2 = 'C:\DBA\Python\estudos\/arquivos\salarios.csv'

df2 = pd.read_csv(file2)

df2.head()
print(df2)



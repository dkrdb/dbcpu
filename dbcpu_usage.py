import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

read_excel = 'C:\DBA\Python\estudos\/arquivos\/cpu_usage.xlsx'

df = pd.read_excel(read_excel)

dataframe = df.plot(kind='line')

plt.show()


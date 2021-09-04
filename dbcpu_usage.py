import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file1 = 'C:\DBA\Python\estudos\/arquivos\/cpu_usage.xlsx'

df = pd.read_excel(excel_file1, sheet_name='cpu',usecols='A:E')

pivot = df.groupby(["DB_NAME","INSTANCE_NUMBER","SNAP_TIME"]).mean()

#print(pivot)

plot_cpu_usage = pivot.plot(kind='line')

plt.show()


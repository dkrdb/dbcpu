import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file1 = 'C:\DBA\Python\estudos\/arquivos\/cpu_usage.xlsx'

df = pd.read_excel(excel_file1, sheet_name='cpu_all',usecols='A:D')

pivot = df.groupby(["DB_NAME","INSTANCE_NUMBER","SNAP_TIME"]).mean()

print(pivot)

from matplotlib import rcParams

rcParams['figure.figsize'] = 10,6

plot_cpu_usage = pivot.plot(kind='line')

plt.title("CPU USAGE")

plt.show()


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

excel_file1 = 'C:\DBA\Python\estudos\/arquivos\/cpu_usage.xlsx'

df = pd.read_excel(excel_file1, sheet_name='cpu_all',usecols='A:D')

db093 = df.loc[(df["DB_NAME"] == "db09") & (df["INSTANCE_NUMBER"] == 3)]
db094 = df.loc[(df["DB_NAME"] == "db09") & (df["INSTANCE_NUMBER"] == 4)]
ctv2 = df.loc[(df["DB_NAME"] == "ctv") & (df["INSTANCE_NUMBER"] == 2)]
ctv3 = df.loc[(df["DB_NAME"] == "ctv") & (df["INSTANCE_NUMBER"] == 3)]
isp7 = df.loc[(df["DB_NAME"] == "isp") & (df["INSTANCE_NUMBER"] == 7)]
isp8 = df.loc[(df["DB_NAME"] == "isp") & (df["INSTANCE_NUMBER"] == 8)]

print(db093)
print(db094)

plt.plot(db093.SNAP_TIME, db093.USR_CPU)
plt.plot(db094.SNAP_TIME, db094.USR_CPU)
plt.plot(ctv2.SNAP_TIME, ctv2.USR_CPU)
plt.plot(ctv3.SNAP_TIME, ctv3.USR_CPU)
plt.plot(isp7.SNAP_TIME, isp7.USR_CPU)
plt.plot(isp8.SNAP_TIME, isp8.USR_CPU)

from matplotlib import rcParams
rcParams['figure.figsize'] = 10,6

plt.title("CPU USAGE")
plt.legend(['db093','db094','ctv2','ctv3','isp7','isp8'], bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)
plt.xlabel("Media do consumo de CPU por Hora")
plt.ylabel("% de uso de CPU")
plt.xticks(rotation=60)
plt.get_current_fig_manager().window.state('zoomed')
plt.show()

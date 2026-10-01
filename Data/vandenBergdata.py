# %%
import csv
import numpy as np
from  pathlib import Path
import matplotlib.pyplot as plt

script_dir = Path(__file__).parent.absolute()
file_path = script_dir / 'vandenBerg_table2.csv'

with open(file_path, newline='') as vb_data:
        globclusters = csv.DictReader(vb_data)

        ##ngc_vb = []
        ##Name_vb = []
        FeH_vb = []
        Age_vb = []
        Age_err_vb = []
        ##Method_vb = []
        ##Figs_vb = []
        ##Range_vb = []
        ##HBtype_vb = []
        ##R_G_vb = []
        ##M_V_vb = []
        ##v_e0_vb = []
        ##log_sigma_0_vb = []

        for row in globclusters:
                ##ngc_vb.append(row['#NGC'])
                ##Name_vb.append(row['Name'])
                FeH_vb.append(float(row['FeH']))
                Age_vb.append(float(row['Age']))
                Age_err_vb.append(float(row['Age_err']))
                ##Method_vb.append(row['Method'])
                ##Figs_vb.append(row['Figs'])
                ##Range_vb.append(row['Range'])
                ##HBtype_vb.append(float(row['HBtype']))
                ##R_G_vb.append(float(row['R_G']))
                ##M_V_vb.append(float(row['M_V']))
                ##v_e0_vb.append(float(row['v_e0']))
                ##log_sigma_0_vb.append(float(row['log_sigma_0']))

## Seperate interactive cell for plotting to avoid reloading data when plotting multiple times
##allows us to better track plots from different progrrams and data sets within vs code itself. 
# %%
plt.figure()
plt.title("VB Age Vs [Fe/H]")
plt.scatter(Age_vb, FeH_vb, color='red', label='Data')
plt.errorbar(Age_vb, FeH_vb, xerr=Age_err_vb, fmt='o', color='red', markersize=6, capsize=4, label='Data with error bars')
plt.xlabel("Age (Gyr)")
plt.ylabel("[Fe/H]")
plt.legend()
plt.grid(True)
plt.show()
# %%

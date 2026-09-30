# %%
import csv
import numpy as np
from  pathlib import Path
import matplotlib.pyplot as plt

script_dir = Path(__file__).parent.absolute()
file_path = script_dir / 'Krause21.csv'

with open(file_path, newline='') as Kra_data:
        globclusters = csv.DictReader(Kra_data)

        ##Class_Kra = []
        ##Object_Kra = []
        ##AltName_Kra = []
        ##Mstar_Kra = []
        ##rh_Kra = []
        ##C5_Kra = []
        Age_Kra = []
        FeH_Kra = []

        for row in globclusters:
                ##Class_Kra.append(row['Class'])
                ##Object_Kra.append(row['Object'])
                ##AltName_Kra.append(row['AltName'])
                ##Mstar_Kra.append(float(row['Mstar']))
                ##rh_Kra.append(float(row['rh']))
                ##C5_Kra.append(float(row['C5']))
                Age_Kra.append(float(row['Age']))
                FeH_Kra.append(float(row['FeH']))


## Seperate interactive cell for plotting to avoid reloading data when plotting multiple times
##allows us to better track plots from different progrrams and data sets within vs code itself. 
# %%
plt.figure()
plt.title("Krause Age Vs [Fe/H]")
plt.scatter(Age_Kra, FeH_Kra, color='red', label='Data')
plt.xlabel("Age (Gyr)")
plt.ylabel("[Fe/H]")
plt.legend()
plt.grid(True)
plt.show()

# %%

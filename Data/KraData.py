# %%
import csv
import numpy as np
from  pathlib import Path
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit

script_dir = Path(__file__).parent.absolute()
file_path = script_dir / 'Krause21.csv'

with open(file_path, newline='') as Kra_data:
        globclusters = csv.DictReader(Kra_data)

        Class_Kra = []
        Object_Kra = []
        AltName_Kra = []
        Mstar_Kra = []
        rh_Kra = []
        C5_Kra = []
        Age_Kra = []
        FeH_Kra = []

        for row in globclusters:
                Class_Kra.append(row['Class'])
                Object_Kra.append(row['Object'])
                AltName_Kra.append(row['AltName'])
                Mstar_Kra.append(float(row['Mstar']))
                rh_Kra.append(float(row['rh']))
                C5_Kra.append(float(row['C5']))
                Age_Kra.append(float(row['Age']))
                FeH_Kra.append(float(row['FeH']))


## Linear regression analysis
result = stats.linregress(FeH_Kra, Age_Kra)

r_squared = result.rvalue ** 2

def linear_func(x, m, c):
    return m * x + c

popt, pcov = curve_fit(linear_func, FeH_Kra, Age_Kra)

slope, intercept = popt
slope_err, intercept_err = np.sqrt(np.diag(pcov))

print(f"Slope: {slope:.4f} ± {slope_err:.4f}")

fit = slope * np.array(FeH_Kra) + intercept
up_fit = (slope + slope_err) * np.array(FeH_Kra) + intercept
low_fit = (slope - slope_err) * np.array(FeH_Kra) + intercept



## Seperate interactive cell for plotting to avoid reloading data when plotting multiple times
##allows us to better track plots from different progrrams and data sets within vs code itself. 
# %%
plt.figure()
plt.title("Krause Age Vs [Fe/H]")
plt.scatter(Age_Kra, FeH_Kra, c=Mstar_Kra, label='Data')
plt.colorbar(orientation = "vertical", label = "M_star")
plt.xlabel("Age (Gyr)")
plt.ylabel("[Fe/H]")
plt.legend()
plt.grid(True)
plt.show()

# %%


plt.figure()
plt.title("Krause Age Vs [Fe/H]")
plt.scatter(FeH_Kra, Age_Kra, c=Mstar_Kra, label='Data')
plt.colorbar(orientation = "vertical", label = "M_star")
plt.plot(FeH_Kra, fit, color='red', label=f'Linear Fit = {slope:.2f} * [Fe/H] + {intercept:.2f}')
plt.scatter([], [], color="w", alpha=0, label="R² = {:.3f}".format(r_squared))  # Invisible point for R² in legend
plt.text(-0.97, 9.2, 'Cluster Name', fontsize=8, color='red')
##plt.errorbar(Age_Kra, FeH_Kra, xerr=Age_err_Kra, fmt='o', color='red', markersize=6, capsize=4, label='Data with error bars')
plt.xlabel("[Fe/H]")
plt.ylabel("Age (Gyr)")
plt.legend()
plt.grid(True)
plt.show()
#right arm (in situ) has very stable mass spread, while the left  "arm" has a greater spread in mass
# and as the metallicity increases the mass generally increases as well (again only for the left arm)
# %%


# %%

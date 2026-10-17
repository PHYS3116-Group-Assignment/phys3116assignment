# %%
import csv
import numpy as np
from  pathlib import Path
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit

script_dir = Path(__file__).parent.absolute()
file_path = script_dir / 'vandenBerg_table2.csv'

with open(file_path, newline='') as vb_data:
        globclusters = csv.DictReader(vb_data)

        ngc_vb = []
        Name_vb = []
        FeH_vb = []
        Age_vb = []
        Age_err_vb = []
        Method_vb = []
        Figs_vb = []
        Range_vb = []
        HBtype_vb = []
        R_G_vb = []
        M_V_vb = []
        v_e0_vb = []
        log_sigma_0_vb = []

        for row in globclusters:
                ngc_vb.append(row['#NGC'])
                Name_vb.append(row['Name'])
                FeH_vb.append(float(row['FeH']))
                Age_vb.append(float(row['Age']))
                Age_err_vb.append(float(row['Age_err']))
                Method_vb.append(row['Method'])
                Figs_vb.append(row['Figs'])
                Range_vb.append(row['Range'])
                HBtype_vb.append(float(row['HBtype']))
                R_G_vb.append(float(row['R_G']))
                M_V_vb.append(float(row['M_V']))
                v_e0_vb.append(float(row['v_e0']))
                log_sigma_0_vb.append(float(row['log_sigma_0']))


m_b = []
for num0 in range(len(M_V_vb)):
       mb_calc = R_G_vb[num0]-M_V_vb[num0]
       m_b.append(mb_calc)
       
print(m_b)

## Linear regression analysis
result = stats.linregress(FeH_vb, Age_vb)

r_squared = result.rvalue ** 2

def linear_func(x, m, c):
    return m * x + c

popt, pcov = curve_fit(linear_func, FeH_vb, Age_vb)

slope, intercept = popt
slope_err, intercept_err = np.sqrt(np.diag(pcov))

print(f"Slope: {slope:.4f} ± {slope_err:.4f}")

fit = slope * np.array(FeH_vb) + intercept
up_fit = (slope + slope_err) * np.array(FeH_vb) + intercept
low_fit = (slope - slope_err) * np.array(FeH_vb) + intercept


# Determine outliers based on residuals




# Plot data and line


## Seperate interactive cell for plotting to avoid reloading data when plotting multiple times
##allows us to better track plots from different progrrams and data sets within vs code itself. 
# %%
plt.figure()
plt.title("VB Age Vs [Fe/H]")
plt.scatter(Age_vb, FeH_vb, color='red', label='Data')
# plt.errorbar(Age_vb, FeH_vb, xerr=Age_err_vb, fmt='o', color='red', markersize=6, capsize=4, label='Data with error bars')

plt.xlabel("Age (Gyr)")
plt.ylabel("[Fe/H]")
plt.legend()
plt.grid(True)
plt.show()
#might be worth using this to just qualitatively describe trends and whatnot
# as done in Forbes et al
# %%

#putting age on x axis to match bifurcated amr of milky way (Leaman et al) paper (which appears to reflect/pull influence relatively well from paper in assignment brief vandenberg)
plt.figure()
plt.title("VB Age Vs [Fe/H]")
plt.scatter(FeH_vb, Age_vb, color='red', label='Data')
plt.plot(FeH_vb, fit, color='blue', label=f'Linear Fit = {slope:.2f} * [Fe/H] + {intercept:.2f}')
plt.scatter([], [], color="w", alpha=0, label="R² = {:.3f}".format(r_squared))  # Invisible point for R² in legend
plt.text(-0.97, 9.2, 'Cluster Name', fontsize=8, color='blue')
##plt.errorbar(Age_vb, FeH_vb, xerr=Age_err_vb, fmt='o', color='red', markersize=6, capsize=4, label='Data with error bars')
plt.xlabel("[Fe/H]")
plt.ylabel("Age (Gyr)")
plt.legend()
plt.grid(True)
plt.show()
# very similar shape/relation as well as axes to Leaman et al Fig 2
# %%

plt.figure()
plt.scatter(m_b, M_V_vb, color='red', label='Data')

##plt.errorbar(Age_vb, FeH_vb, xerr=Age_err_vb, fmt='o', color='red', markersize=6, capsize=4, label='Data with error bars')

plt.legend()
plt.grid(True)
plt.show()


# %%

#-1.9238x^2-8.3607+3.097 (LMC) (fe/h is x axis)
#-0.0024x^3+0.0537x^2-0.408x-0.19 (SMC)

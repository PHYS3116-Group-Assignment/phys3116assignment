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
        mass_vb = []
        log_mass_vb = []
        solar_mass = 2E30

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


for num0 in range(len(Name_vb)):
       mass_star = M_V_vb[num0]*(-1.6)
       mass_vb.append(mass_star)
       log_mass = np.log10(mass_vb[num0])/(solar_mass)
       log_mass_vb.append(log_mass)


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

# %%

x = np.linspace(-2.5, max(FeH_vb), 500)

#-1.9238x^2-8.3607+3.097 (LMC) (fe/h is x axis)
#-0.0024x^3+0.0537x^2-0.408x-0.19 (SMC)
smc_fit = 12.974*x**3 + 49.59*x**2 + 48.896*x + 16.025
lmc_fit = -1.9238*x**2 - 8.3607*x + 3.0937

plt.figure()
plt.title("VB Age Vs [Fe/H]")
plt.scatter(FeH_vb, Age_vb, c=mass_vb)
plt.colorbar(orientation = "vertical", label="Mass")
# plt.plot(x, smc_fit, linestyle='dashed', color = 'red', label='SMC')
# plt.plot(x, lmc_fit, linestyle = 'dashed', color = 'green', label='LMC')
plt.xlabel("[Fe/H]")
plt.xlim(-2.6,0)
plt.ylim(8,15)
plt.ylabel("Age (Gyr)")
plt.legend()
plt.grid(True)
plt.show()

#%%

plt.figure()
plt.title("VB Age Vs [Fe/H]")
plt.scatter(FeH_vb, Age_vb, c=mass_vb, label='Data')
plt.colorbar(orientation = "vertical", label="Mass (M☉)")
plt.plot(FeH_vb, fit, color='red', label=f'Linear Fit = {slope:.2f} * [Fe/H] + {intercept:.2f}')
plt.scatter([], [], color="w", alpha=0, label="R² = {:.3f}".format(r_squared))  # Invisible point for R² in legend
plt.text(-0.97, 9.2, 'Cluster Name', fontsize=8, color='red')
##plt.errorbar(Age_vb, FeH_vb, xerr=Age_err_vb, fmt='o', color='red', markersize=6, capsize=4, label='Data with error bars')
plt.xlabel("[Fe/H]")
plt.ylabel("Age (Gyr)")
#plt.legend()
plt.grid(True)
plt.show()
# very similar shape/relation as well as axes to Leaman et al Fig 2

#bifurcation to the left of around 12.25 Gyr indicates accretion

#%%
plt.figure()
plt.title("Galactic Radius vs Age")
plt.scatter(R_G_vb, Age_vb, c = FeH_vb, cmap = "magma", label='Data')
plt.colorbar(orientation = "horizontal", label = "Fe/H")
plt.xlabel("[Radius kpc")
plt.ylabel("Age (Gyr)")
plt.legend()
plt.grid(True)
plt.show()
#colourmapping metallicity to age/radius graph indicates that the GCs that make up the bifurcated
#arm of the Age/FeH plot are typically closer to the centre of the galaxy ie in the halo
# indicating that there is a correlation between the halo and accreted GCs

#%%
plt.figure()
plt.title("Galactice Radius vs Magnitude")
plt.scatter(R_G_vb, M_V_vb,  label='Data')
plt.xlabel("Radius kpc")
plt.ylabel("Magnitude")
plt.legend()
plt.grid(True)
plt.show()

#GCs closer to halo, previously correlated to accreted GCs, are *somewhat* clustered around a magnitude
# of around <-7, so in halo = brighter? magnitude also correlates to mass so heavier
# brighter indicates younger?
# what is correlation between luminosity and metallicity
# correlate mass to velocity; its mass and proximity to nucleus gives it a specific
#velocity, which can be used to identify stuff in HP_all

#%%
plt.figure()
plt.title("Escape velocity vs log(mass)")
plt.scatter(v_e0_vb,((mass_vb)),cmap = "magma", label='Data')
plt.xlabel("Escape Velocity")
plt.ylabel("Mass (calculated via magnitude)")
plt.legend()
plt.grid(True)
plt.show()

#%%

plt.figure()
plt.title("Escape velocity vs log(mass)")
plt.scatter(v_e0_vb,((mass_vb)), c = FeH_vb, cmap = "magma", label='Data')
plt.colorbar(orientation = "vertical", label = "Fe/H")
plt.xlabel("Escape Velocity")
plt.ylabel("Mass (calculated via magnitude)")
plt.legend()
plt.grid(True)
plt.show()

#correlation between mass and metallicity (which is to say bodies in globular cluster arm had a range of masses from around 6-12), proposed in Krause data, doesnt reaaaally follow here,
# there seems to be kind of a cap in mass increase for the most part at around 4.5-5 for whatever reason
# that said looking at the previous chart, the higher metallicity bodies are the ones that are closest to the halo
# mass here would more be used to link to the escape velocity, with the 

# %%
plt.figure()
plt.title("Escape velocity vs Radius")
plt.scatter(R_G_vb,((v_e0_vb)), c = HBtype_vb, cmap = "magma", label='Data')
plt.colorbar(orientation = "vertical")
plt.xlabel("Radius")
plt.ylabel("Velocity")
plt.legend()
plt.grid(True)
plt.show()
# %%

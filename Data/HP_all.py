#%%
import csv
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from scipy import stats
from scipy.optimize import curve_fit

script_dir = Path(__file__).parent.absolute()
file_path = script_dir / 'HarrisPartI.csv'

with open(file_path, newline='') as HPi_data:
        globclusters = csv.DictReader(HPi_data)


        id_HPi = []
        name_HPi = []
        ra_HPi = []
        ra_h_HPi = []
        ra_min_HPi = []
        ra_sec_HPi = []
        ra_deg_HPi = []
        decl_HPi = []
        decl_deg_HPi = []
        decl_min_HPi = []
        decl_sec_HPi = []
        decl_dec_deg_HPi = []
        long_HPi = []
        lat_HPi = []
        r_sun_HPi = []
        r_gc_HPi = []
        x_HPi = []
        y_HPi = []
        z_HPi = []

        for row in globclusters:
                id_HPi.append(row['ID'])
                name_HPi.append(row['Name'])
                ra_HPi.append((row['RA']))
                decl_HPi.append(row['DEC'])
                long_HPi.append(float(row['L']))
                lat_HPi.append(float(row['B']))
                r_sun_HPi.append(float(row['R_Sun']))
                r_gc_HPi.append(float(row['R_gc']))
                x_HPi.append(float(row['X']))
                y_HPi.append(float(row['Y']))
                z_HPi.append(float(row['Z']))

        for value in ra_HPi:
                ra_h_HPi.append(float((value[0]+(value[1]))))
                ra_min_HPi.append(float((value[3]+(value[4]))))
                ra_sec_HPi.append(float((value[6]+(value[7]))))

        for value2 in decl_HPi:
                if value2[0] == '+':
                    decl_deg_HPi.append(float(value2[1]+value2[2]))
                elif value2[0] == '-':
                    decl_deg_HPi.append(-1*float(value2[1]+value2[2]))
                decl_min_HPi.append(float(value2[4]+value2[5]))
                decl_sec_HPi.append(float(value2[7]+value2[8]))

script_dir = Path(__file__).parent.absolute()
file_path = script_dir / 'HarrisPartIII.csv'

with open(file_path, newline='') as HPiii_data:
    globclusters= csv.DictReader(HPiii_data)

    id_HPiii = []
    category = []
    v_r_HPiii = []
    v_r_err_HPiii = []
    v_LSR_HPiii = []
    sig_v_HPiii = []
    sig_v_err_HPiii = []
    c_HPiii = []
    r_c_HPiii = []
    r_h_HPiii = []
    mu_V_HPiii = []
    rho_0_HPiii = []
    lg_tc_HPiii = []
    lg_th_HPiii = []

    def to_float(value):
        value = value.strip()  # Remove leading/trailing whitespace
        return np.nan if value in ('NA', '') else float(value)

    for row in globclusters:
        id_HPiii.append(row['ID'])
        v_r_HPiii.append(to_float(row['v_r']))
        v_r_err_HPiii.append(to_float(row['v_r_e']))
        v_LSR_HPiii.append(to_float(row['v_LSR']))
        sig_v_HPiii.append(to_float(row['sig_v']))
        sig_v_err_HPiii.append(to_float(row['sig_v_e']))
        c_HPiii.append(to_float(row['c']))
        r_c_HPiii.append(to_float(row['r_c']))
        r_h_HPiii.append(to_float(row['r_h']))
        mu_V_HPiii.append(to_float(row['mu_V']))
        rho_0_HPiii.append(to_float(row['rho_0']))
        lg_tc_HPiii.append(to_float(row['lg_tc']))
        lg_th_HPiii.append(to_float(row['lg_th']))


for num1 in range(len(ra_HPi)):
      ra_deg = ra_h_HPi[num1] + ra_min_HPi[num1]/60 + ra_sec_HPi[num1]/3600
      ra_deg_HPi.append(ra_deg)
      decl_deg = decl_deg_HPi[num1] + decl_min_HPi[num1]/60 + decl_sec_HPi[num1]/3600
      decl_dec_deg_HPi.append(decl_deg)

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


# for num0 in range(len(id_HPiii)):
#       if v_r_HPiii[num0] == 0 and v_LSR_HPiii[num0] == 0 and sig_v_HPiii[num0] == 0:
#                         category.append("Undefined")
#       else:
#             category.append("GC")

# print(category)
# print(id_HPi)
# print(type(v_LSR_HPiii[16]))


#%%

from astropy import units as u
import astropy.coordinates as coord

icrs1 = []
vgsr = []

for num2 in range(len(id_HPiii)):
      icrs = coord.SkyCoord(
      ra= ra_deg_HPi[num2] * u.deg,
      dec=decl_dec_deg_HPi[num2] * u.deg,
      radial_velocity=v_r_HPiii[num2] * u.km / u.s,
      frame="icrs",)
      icrs1.append(icrs)
      v_sun = coord.Galactocentric().galcen_v_sun.to_cartesian()
      gal = icrs1[num2].transform_to(coord.Galactic)
      cart_data = gal.data.to_cartesian()
      unit_vector = cart_data / cart_data.norm()
      v_proj = v_sun.dot(unit_vector)
      rv_gsr0 = (icrs.radial_velocity + v_proj)
      rv_gsr = rv_gsr0.value
      vgsr.append(rv_gsr)

print(id_HPi[1], (vgsr[1]))

#%%
plt.figure()
plt.title("Radius against Galactocentric velocity")
plt.scatter(x=r_gc_HPi, y=vgsr, c='red', label='Data', s = 5)
##plt.errorbar(Age_vb, FeH_vb, xerr=Age_err_vb, fmt='o', color='red', markersize=6, capsize=4, label='Data with error bars')
plt.xlabel("R (kpc)")
plt.ylabel("Galactocentric Velocity")
plt.legend()
plt.grid(True)
plt.show()

#%%
#cross reference with position in galaxy?

#%%

#3d plot of postion of globular clusters in galactic coordinates
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_HPi, y_HPi, z_HPi, c='red', cmap='viridis')
ax.set_box_aspect((1,1,1), zoom=0.82)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()

#%%

x = np.array(long_HPi)
y = np.array(v_LSR_HPiii)

mask = np.isfinite(x) & np.isfinite(y)

x_fit = x[mask]
y_fit = y[mask]

## sin regression analysis
result = stats.linregress(x_fit, y_fit)

r_squared = result.rvalue ** 2

def sin_func(l, A, C):
    return A*np.sin(np.radians(l)) + C 

popt, pcov = curve_fit(sin_func, x_fit, y_fit)

amplitude, offset = popt
amplitude_err, offset_err = np.sqrt(np.diag(pcov))

print(f"Amplitude: {amplitude:.4f} ± {amplitude_err:.4f}")
print(f"Offset: {offset:.4f} ± {offset_err:.4f}")


l = np.linspace(0, 360, 100)  # Range of Galactic longitudes for plotting the sine curve

#loong vs vgsr plot
plt.figure()
plt.title("Galactic Longitude vs Velocity")
plt.scatter(x=x_fit, y=y_fit, c='red', label='Data', s = 5)
plt.plot(l, sin_func(l, *popt), color='blue', label=f'Sine Fit: {amplitude:.2f} * sin(l) + {offset:.2f}')
# plt.colorbar(orientation = "vertical")
##plt.errorbar(Age_vb, FeH_vb, xerr=Age_err_vb, fmt='o', color='red', markersize=6, capsize=4, label='Data with error bars')
plt.xlabel("Galactic Longitude")
plt.ylabel("Velocity (km/s)")
plt.legend()
plt.grid(True)
plt.show()


#REDUNDANT
#converting heliocentric velocity to galactocentric
# import numpy as np
# import astropy as ast
# import astropy.coordinates as coord
# from astropy import units as u
# from astropy.coordinates import SkyCoord

# c_1 = []
# gc_1 = []

# for num2 in range(len(v_r_HPiii)):
#       c1 = coord.SkyCoord(
#         ra= ra_deg_HPi[num2] * u.degree,
#         dec= decl_dec_deg_HPi[num2] * u.degree,
#         distance=(r_gc_HPi[num2] * u.mas).to(u.pc, u.parallax()),
# #       x=x_HPi[num2], y=y_HPi[num2], z=z_HPi[num2], unit='kpc', representation_type='cartesian',
# #       radial_velocity= v_r_HPiii[num2] * (u.km / u.s),
#         frame="icrs",)
      
#       c_1.append(c1)

# for num3 in c_1:
#       gc1 = num3.transform_to(coord.Galactocentric)
#       gc_1.append(gc1)

# print(gc_1[0].v_x)



#%%
# Age-metallicity relation coloured by |z|
# Function to sort names in a case-insensitive manner
def name_key(name):
    return "".join(str(name).split()).upper() # Split the name into a list of strings and convert to uppercase

# Match Harris_all names with Z data in VandenBerg data
z_lookup = {
      name_key(name): z 
      for name, z in zip(id_HPi, z_HPi)
}

plot_feh_AMZ =[]
plot_age_AMZ =[]
plot_age_err_AMZ =[]
plot_z_AMZ =[]
unmatched_names_AMZ = []

for name, feh_AMZ, age_AMZ, age_err_AMZ in zip(
      ngc_vb, FeH_vb, Age_vb, Age_err_vb):
        key = name_key(name)

        if key.isdigit():
                key = f"NGC{key}"

        if key not in z_lookup:
            unmatched_names_AMZ.append(name)
            continue

        z_AMZ = z_lookup[key]

        if not np.all(np.isfinite([feh_AMZ, age_AMZ, age_err_AMZ, z_AMZ])):
            unmatched_names_AMZ.append(name)
            continue

        plot_feh_AMZ.append(feh_AMZ)
        plot_age_AMZ.append(age_AMZ)
        plot_age_err_AMZ.append(
              age_err_AMZ if np.isfinite(age_err_AMZ) and age_err_AMZ > 0 else np.nan
        )
        plot_z_AMZ.append(abs(z_AMZ))

print("Unmatched names in Age-Metallicity-Z relation:", unmatched_names_AMZ)
print("Clusters plotted:", len(plot_feh_AMZ))

# Metallicity vs |Z| plot, coloured by age
plt.figure()
plt.title("Metallicity and Height Above the Galactic Plane")
plt.scatter(
    x=plot_feh_AMZ,
    y=plot_z_AMZ,
    c=plot_age_AMZ,
    cmap="coolwarm",
    label="Data",
    s=25
)
plt.colorbar(
    orientation="vertical",
    label="Age (Gyr)"
)
plt.xlabel("[Fe/H] (dex)")
plt.ylabel("|Z| (kpc)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
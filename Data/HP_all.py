#%%
import csv
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt


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



for num3 in range(len(icrs1)):
      v_sun = coord.Galactocentric().galcen_v_sun.to_cartesian()
      gal = icrs1[num3].transform_to(coord.Galactic)
      cart_data = gal.data.to_cartesian()
#       unit_vector = cart_data[num3] / cart_data.norm()
#       v_proj = v_sun.dot(unit_vector[num3])



print(vgsr)












#%%




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
# plt.figure()
# plt.title("VB Age Vs [Fe/H]")
# plt.scatter(r_gc_HPi, , color='red', label='Data')
# ##plt.errorbar(Age_vb, FeH_vb, xerr=Age_err_vb, fmt='o', color='red', markersize=6, capsize=4, label='Data with error bars')
# # plt.xlabel("Age (Gyr)")
# # plt.ylabel("[Fe/H]")
# plt.legend()
# plt.grid(True)
# plt.show()

#%%

#HarrisPartIII

import csv
import numpy as np
from  pathlib import Path

script_dir = Path(__file__).parent.absolute()
file_path = script_dir / 'HarrisPartIII.csv'

with open(file_path, newline='') as vb_data:
        globclusters = csv.DictReader(vb_data)

        id_HPiii = []
        v_r_HPiii = []
        v_r_e_HPiii = []
        v_LSR_HPiii = []
        sig_v_HPiii = []
        sig_v_e_HPiii = []
        c_HPiii = []
        r_c_HPiii = []
        r_h_HPiii = []
        mu_v_HPiii = []
        rho_0_HPiii = []
        lg_tc_HPiii = []
        lg_th_HPiii = []

        for row in globclusters:
            for value in row:
                if value == 'NA':
                    id_HPiii.append(float(0))
                    v_r_HPiii.append(float(0))
                    v_r_e_HPiii.append(float(0))
                    v_LSR_HPiii.append(float(0))
                    sig_v_HPiii.append(float(0))
                    sig_v_e_HPiii.append(float(0))
                    c_HPiii.append(float(0))
                    r_c_HPiii.append(float(0))
                    r_h_HPiii.append(float(0))
                    mu_v_HPiii.append(float(0))
                    rho_0_HPiii.append(float(0))
                    lg_tc_HPiii.append(float(0))
                    lg_th_HPiii.append(float(0))
                else:      
                    id_HPiii.append(row['ID'])
                    v_r_HPiii.append(float(row['v_r']))
                    v_r_e_HPiii.append(float((row['v_r_e'])))
                    v_LSR_HPiii.append(float(row['v_LSR']))
                    sig_v_HPiii.append(float(row['sig_v']))
                    sig_v_e_HPiii.append(float(row['sig_v_e']))
                    c_HPiii.append(float(row['c']))
                    r_c_HPiii.append(float(row['r_c']))
                    r_h_HPiii.append(float(row['r_h']))
                    mu_v_HPiii.append(float(row['mu_V']))
                    rho_0_HPiii.append(float(row['rho_0']))
                    lg_tc_HPiii.append(float(row['lg_tc']))
                    lg_th_HPiii.append(float(row['lg_th']))

# %%

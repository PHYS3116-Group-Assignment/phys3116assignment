import csv
import numpy as np
from  pathlib import Path
import matplotlib.pyplot as plt

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


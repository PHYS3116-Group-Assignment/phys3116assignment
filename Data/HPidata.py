import csv
import numpy as np

with open('Data/HarrisPartI.csv', newline='') as HPi_data:
        globclusters = csv.DictReader(HPi_data)


        id_HPi = []
        name_HPi = []
        ra_HPi = []
        ra_h_HPi = []
        ra_min_HPi = []
        ra_sec_HPi = []
        decl_HPi = []
        decl_deg_HPi = []
        decl_min_HPi = []
        decl_sec_HPi = []
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



                        


                        
                

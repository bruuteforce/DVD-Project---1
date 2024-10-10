import shutil
import os
import itertools
from ODO_MOS import parse_file_gates
from ODO_MOS import parse_file
import pandas as pd

def copy_and_edit_file(src_path, dest_path, old_string1, new_string1, old_string2="####", new_string2="####",old_string3="####", new_string3="####",old_string4="####", new_string4="####",old_string5="####", new_string5="####",old_string6="####", new_string6="####",old_string7="####", new_string7="####",old_string8="####", new_string8="####",old_string9="####", new_string9="####",old_string10="####", new_string10="####",old_string11="####", new_string11="####",old_string12="####", new_string12="####"):
    # Copy the file
    shutil.copy(src_path, dest_path)
    
    # Read the content of the copied file
    with open(dest_path, 'r') as file:
        file_data = file.read()
    
    # Replace the target string
    file_data = file_data.replace(old_string1, new_string1)
    if new_string2 != "####" :
        file_data = file_data.replace(old_string2, new_string2)
    if new_string3 != "####" :
        file_data = file_data.replace(old_string3, new_string3)
    if new_string4 != "####" :
        file_data = file_data.replace(old_string4, new_string4)
    if new_string5 != "####" :
        file_data = file_data.replace(old_string5, new_string5)
    if new_string6 != "####" :
        file_data = file_data.replace(old_string6, new_string6)
    if new_string7 != "####" :
        file_data = file_data.replace(old_string7, new_string7)
    if new_string8 != "####" :
        file_data = file_data.replace(old_string8, new_string8)
    if new_string9 != "####" :
        file_data = file_data.replace(old_string9, new_string9)
    if new_string10 != "####" :
        file_data = file_data.replace(old_string10, new_string10)
    if new_string11 != "####" :
        file_data = file_data.replace(old_string11, new_string11)
    if new_string12 != "####" :
        file_data = file_data.replace(old_string12, new_string12)
    # Write the modified content back to the file
    with open(dest_path, 'w') as file:
        file.write(file_data)

def get_vdd(value):
    return 1.1 if value == 1 else value 


if not os.path.exists('CLA_files\\temp'):
    os.mkdir('CLA_files\\temp')
    os.mkdir('CLA_files\\temp\\outputs')

    source_file = 'CLA_files\\cla.net'
    
    avg_err=0;cnt=0
    variables = ['p3_', 'p2_', 'p1_', 'p0_', 'g3_', 'g2_', 'g1_', 'g0_', 'cin']
    combinations = list(itertools.product([0, 1], repeat=len(variables)))
    CLA_input_comb_csv = pd.DataFrame()
    for combination in combinations:
        combo_dict = dict(zip(variables, combination))
        print(combo_dict['p3_'], combo_dict['p2_'], combo_dict['p1_'], combo_dict['p0_'], combo_dict['g3_'], combo_dict['g2_'], combo_dict['g1_'], combo_dict['g0_'], combo_dict['cin'])

        destination_file = f"CLA_files\\temp\\cla_{combo_dict['p3_']}{combo_dict['p2_']}{combo_dict['p1_']}{combo_dict['p0_']}{combo_dict['g3_']}{combo_dict['g2_']}{combo_dict['g1_']}{combo_dict['g0_']}{combo_dict['cin']}.net"
        string_to_replace2 = 'GatesAndInputs.txt'
        new_string2 = f"CLA_files\\temp\\outputs\\GatesAndInputs_{combo_dict['p3_']}{combo_dict['p2_']}{combo_dict['p1_']}{combo_dict['p0_']}{combo_dict['g3_']}{combo_dict['g2_']}{combo_dict['g1_']}{combo_dict['g0_']}{combo_dict['cin']}.txt"
        string_to_replace3 = 'CLA.txt'
        new_string3 = f"CLA_files\\temp\\outputs\\CLA_{combo_dict['p3_']}{combo_dict['p2_']}{combo_dict['p1_']}{combo_dict['p0_']}{combo_dict['g3_']}{combo_dict['g2_']}{combo_dict['g1_']}{combo_dict['g0_']}{combo_dict['cin']}.txt"
        copy_and_edit_file(source_file, destination_file, string_to_replace2, new_string2,"Vin_p3_ p3_ 0 1.1",f"Vin_p3_ p3_ 0 {get_vdd(combo_dict['p3_'])}","Vin_p2_ p2_ 0 1.1",f"Vin_p2_ p2_ 0 {get_vdd(combo_dict['p2_'])}","Vin_p1_ p1_ 0 1.1",f"Vin_p1_ p1_ 0 {get_vdd(combo_dict['p1_'])}","Vin_p0_ p0_ 0 1.1",f"Vin_p0_ p0_ 0 {get_vdd(combo_dict['p0_'])}","Vin_g3_ g3_ 0 1.1",f"Vin_g3_ g3_ 0 {get_vdd(combo_dict['g3_'])}","Vin_g2_ g2_ 0 1.1",f"Vin_g2_ g2_ 0 {get_vdd(combo_dict['g2_'])}","Vin_g1_ g1_ 0 1.1",f"Vin_g1_ g1_ 0 {get_vdd(combo_dict['g1_'])}","Vin_g0_ g0_ 0 1.1",f"Vin_g0_ g0_ 0 {get_vdd(combo_dict['g0_'])}","Vin_cn cin 0 1.1",f"Vin_cn cin 0 {get_vdd(combo_dict['cin'])}",".INCLUDE \"./",".INCLUDE \"../",string_to_replace3,new_string3)
        os.system(f"ngspice_con -b {destination_file}")
        estimation=parse_file_gates(new_string2)
        parse_file(new_string3,"v(p_)",["p_","g_","cnz","cny","cnx","leakage_current"])
        print(f"estimation:{estimation}")
        cla_csv = f"CLA_files\\temp\\outputs\\CLA_{combo_dict['p3_']}{combo_dict['p2_']}{combo_dict['p1_']}{combo_dict['p0_']}{combo_dict['g3_']}{combo_dict['g2_']}{combo_dict['g1_']}{combo_dict['g0_']}{combo_dict['cin']}.csv"
        df=pd.read_csv(cla_csv)
        print(f"simulation:{df['leakage_current'].values[0]}")

        row = {
                "p3_":get_vdd(combo_dict['p3_']),
                "p2_":get_vdd(combo_dict['p2_']),
                "p1_":get_vdd(combo_dict['p1_']),
                "p0_":get_vdd(combo_dict['p0_']),
                "g3_":get_vdd(combo_dict['g3_']),
                "g2_":get_vdd(combo_dict['g2_']),
                "g1_":get_vdd(combo_dict['g1_']),
                "g0_":get_vdd(combo_dict['g0_']),
                "cin":get_vdd(combo_dict['cin']),
                "p_":df['p_'].values[0],
                "g_":df['g_'].values[0],
                "cnz":df['cnz'].values[0],
                "cny":df['cny'].values[0],
                "cnx":df['cnx'].values[0],
                "simulated_leakage":df['leakage_current'].values[0],
                "estimated_leakage":estimation,
                f"% Err":100*abs(df['leakage_current'].values[0]-estimation)/df['leakage_current'].values[0]
            }
        CLA_input_comb_csv = pd.concat([CLA_input_comb_csv, pd.DataFrame([row])], ignore_index=True)
        avg_err+=100*abs(df['leakage_current'].values[0]-estimation)/df['leakage_current'].values[0]
        cnt+=1

    avg_err=avg_err/cnt
    CLA_input_comb_csv.to_csv("CLA_ALL_INPUT_COMB.csv",index=False)
    print(f"average error %:{avg_err}")
    with open('AVERAGE_ERROR_%.txt', 'w') as file_avg:
        file_avg.write(f"{avg_err}")


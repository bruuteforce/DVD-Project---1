import pandas as pd
import os
from ODO_MOS import parse_file_gates

os.system(f"ngspice_con -b CLA_files\cla.net")
parse_file_gates("GatesAndInputs.txt")

df_cla_gates=pd.read_csv("Gates+Leakages.csv")
estimation=0
for index, row in df_cla_gates.iterrows():
    estimation+=abs(row['estimated_leakage'])
    #estimation+=abs(row['simulated_leakage'])

print(estimation)
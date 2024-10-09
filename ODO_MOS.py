import pandas as pd
import os
import re

def change_extension(file_path, new_extension):
    # Split the file path into the base name and the current extension
    base_name, _ = os.path.splitext(file_path)
    # Create the new file path with the new extension
    new_file_path = base_name + '.' + new_extension
    return new_file_path

lookup_table={}
# columns=['vdrain','vgate','vsource','vbody','idrain','igate','isource','ibody']
def parse_file(filename,delimiter,columns):
    try:
        with open(filename, 'r') as file:
            temp=""
            global lookup_table
            j=0
            file_path = change_extension(filename,'text')
            #dont open file if no text output needed
            filew=None #open(file_path, 'a')
            ##filew.write('vdrain       vgate      vsource          vbody        idrain        igate        isource     ibody')
            #print('vdrain       vgate      vsource          vbody        idrain        igate        isource     ibody')
            for item in columns:
                #print(f"{item:<13}", end=" ")
                filew and filew.write(f"{item:<13} ")

            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace
                if '=' in line:
                    variable, value = line.split('=')
                    variable = variable.strip()
                    value = value.strip()
                    ##print(f"{variable} {value}")
                    
                    if(variable == delimiter):
                        ##print(temp)
                        filew and filew.write(temp+'\n')
                        values_list = temp.split()
                        #print(values_list)
                        if(len(values_list)==len(columns)):
                            #print(values_list)
                            lookup_table[j] = {columns[i]: values_list[i] for i in range(len(columns))}
                            j+=1
                        temp=''

                    temp=f"{temp} {value}"
            values_list = temp.split()
            filew and filew.write(temp+'\n')
            if(len(values_list)==len(columns)):
                #print(values_list)
                lookup_table[j] = {columns[i]: values_list[i] for i in range(len(columns))}
                j+=1

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    
    df = pd.DataFrame.from_dict(lookup_table,orient='index',columns=columns)
    #df.columns=columns
    # Print the DataFrame
    #print(df)
    #print(lookup_table)
    
    # Export DataFrame to Excel
    #df.to_excel(change_extension(filename,'xlsx'), index=False)
    df.to_csv(change_extension(filename,'csv'), index=False)


#df_Nand_csv = pd.read_csv("CMOS_GATE_files\\temp\outputs\\Nand.csv")
df_Nand_csv = pd.read_csv("Nand_altered.csv")
#df_Inverter_csv = pd.read_csv("CMOS_GATE_files\\temp\outputs\Inverter.csv")
df_Inverter_csv = pd.read_csv("Inverter_altered.csv")

def __round(value):
    return round(value*40)/40

def parse_file_gates(filename):
    try:
        check=0
        df = pd.DataFrame()
        prev=None; prev_val=0
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if '=' in line:
                    variable, value = line.split('=')
                    variable = variable.strip()
                    value = value.strip()
                
                    #print(f"{variable}:{value}")
                    
                    parts = variable.split('.')
                    substring = parts[-2]
                    
                    if "inv" in substring:
                        #print(f"Inverter:{float(value)},{value}")
                        simul_leakage=df_Inverter_csv[df_Inverter_csv['v(nodea)']==__round(float(value))]['current_total'].values[0]
                        estim_leakage=df_Inverter_csv[df_Inverter_csv['v(nodea)']==__round(float(value))]['estimated_leakage'].values[0]
                        row = {"GATE":"INVERTER","simulated_leakage":simul_leakage,"estimated_leakage":estim_leakage,"INPUT1":value}
                        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)

                    if "nand" in substring:
                        #print ("Nand")
                        curr = '.'.join(parts[:-1])
                        if (check == 1):
                            if (prev != curr):
                                print (f"recheck the file! {prev}!={curr}")
                                exit(0)
                            else:
                                if "mnb" in parts[-1]:
                                    check = 0
                                    simul_leakage=df_Nand_csv[(df_Nand_csv['v(nodea)']==__round(float(prev_val))) & (df_Nand_csv['v(nodeb)']==__round(float(value)))]['current_total'].values[0]
                                    estim_leakage=df_Nand_csv[(df_Nand_csv['v(nodea)']==__round(float(prev_val))) & (df_Nand_csv['v(nodeb)']==__round(float(value)))]['estimated_leakage'].values[0]
                                    row = {"GATE":"NAND","simulated_leakage":simul_leakage,"estimated_leakage":estim_leakage,"INPUT1":prev_val,"INPUT2":value}
                                    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)

                        elif (check == 0):
                            if "mna" in parts[-1]:
                                check = 1
                                prev=curr
                                prev_val=value
        
        match = re.search(r'_(.*?)\.', filename)
        filename_gate_leakages=""
        if match:
            filename_gate_leakages=filename.replace("GatesAndInputs","Gates+Leakages")
        else:
            filename_gate_leakages=f"Gates+Leakages.csv"
            
        df.to_csv(filename_gate_leakages,index=False)
        
        estimation=0
        for index, row in df.iterrows():
            estimation+=abs(row['estimated_leakage'])
            #estimation+=abs(row['simulated_leakage'])

        return estimation
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

import pandas as pd
import os

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
                print(f"{item:<13}", end=" ")
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
    print(df)
    print(lookup_table)
    
    # Export DataFrame to Excel
    #df.to_excel(change_extension(filename,'xlsx'), index=False)
    df.to_csv(change_extension(filename,'csv'), index=False)



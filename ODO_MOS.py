import pandas as pd
lookup_table={}
columns=['abs(v(alim))','vdrain','vgate','vsource','vbody','idrain','igate','isource','ibody']
def parse_file(filename):
    try:
        with open(filename, 'r') as file:
            temp=""
            global lookup_table
            j=0
            print('abs(v(alim))     vdrain       vgate      vsource          vbody        idrain        igate        isource     ibody')
            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace
                if '=' in line:
                    variable, value = line.split('=')
                    variable = variable.strip()
                    value = value.strip()
                    ##print(f"{variable} {value}")
                    
                    if(variable == "abs(v(alim))"):
                        ##print(temp)
                        values_list = temp.split()
                        #print(values_list)
                        if(len(values_list)==len(columns)):
                            #print(values_list)
                            lookup_table[j] = {columns[i]: values_list[i] for i in range(len(columns))}
                            j+=1
                        temp=''

                    temp=f"{temp} {value}"
        
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Example usage:
parse_file('test.txt')
df = pd.DataFrame.from_dict(lookup_table,orient='index',columns=columns)
#df.columns=columns
# Print the DataFrame
print(df)
print(lookup_table)
# Export DataFrame to Excel
df.to_excel('products.xlsx', index=False)

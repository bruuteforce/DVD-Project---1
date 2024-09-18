import pandas as pd

def __round(value):
    return round(value*40)/40

Vdd=1.1

# Open the file in write mode to clear its contents
with open('Estimations.txt', 'w') as file:
    pass  # 'pass' does nothing, but opening in 'w' mode clears the file


n_on_1 = pd.read_csv("DVD_MOS_files\\temp\outputs\\NMOS_ON1.csv")
n_off_1 = pd.read_csv("DVD_MOS_files\\temp\outputs\\NMOS_OFF1.csv")
p_on_1 = pd.read_csv("DVD_MOS_files\\temp\outputs\PMOS_ON1.csv")
p_off_1 = pd.read_csv("DVD_MOS_files\\temp\outputs\PMOS_OFF1.csv")

def fetch_currents_nmos(drain,gate,source,body):
    if gate>Vdd/2.0 :
        actv_df=n_on_1
        # print("ON")
    else :
        # print("OFF")
        actv_df=n_off_1
    # print(drain,gate,source,body)
    match=actv_df.loc[(actv_df['vdrain']==drain) & (actv_df['vsource']==source) & (actv_df['vgate']==gate) & (actv_df['vbody']==body)]
    # print(actv_df.loc[(actv_df['vdrain']==drain) & (actv_df['vsource']==source) & (actv_df['vgate']==gate) & (actv_df['vbody']==body)])
    return match

def fetch_currents_pmos(drain,gate,source,body):
    if gate<Vdd/2.0 :
        actv_df=p_on_1
        # print("ON")
    else :
        # print("OFF")
        actv_df=p_off_1
    # print(drain,gate,source,body)
    match=actv_df.loc[(actv_df['vdrain']==drain) & (actv_df['vsource']==source) & (actv_df['vgate']==gate) & (actv_df['vbody']==body)]
    # print(actv_df.loc[(actv_df['vdrain']==drain) & (actv_df['vsource']==source) & (actv_df['vgate']==gate) & (actv_df['vbody']==body)])
    return match

df_n = pd.read_csv("STACKED_MOS_files\\temp\outputs\AandBn.csv")

# for value in df.iloc[:, 0]:
#     print(value)
#     print(round(value * 20) / 20)
#     vds1=round(value * 20) / 20 #Source for TOP NMOS; drain for BOTTOM NMOS


for index, row in df_n.iterrows():
    print(f"Index: {index}")
    print(f"vsd1: {__round(row['v(sd1)'])}, vgen: {__round(row['vgen'])},va: {__round(row['va'])},vb: {__round(row['vb'])}")
    # M1
    drain = __round(row['v(sd1)'])
    gate = __round(row['va'])
    source = 0
    body = 0
    VI_data_1=fetch_currents_nmos(drain,gate,source,body)
    # M2
    drain = __round(row['vgen'])
    gate = __round(row['vb'])
    source = __round(row['v(sd1)'])
    body = 0
    VI_data_2=fetch_currents_nmos(drain,gate,source,body)

    print(VI_data_1)
    print(VI_data_2)
    match (VI_data_1['vgate'].values[0], VI_data_2['vgate'].values[0]):
        case (0, 0):
            leakage_current=VI_data_2['idrain'].values[0]
        case (0, 1.1):
            leakage_current=VI_data_1['idrain'].values[0]+VI_data_2['igate'].values[0]
        case (1.1, 0):
            leakage_current=VI_data_1['igate'].values[0]+VI_data_2['idrain'].values[0]
        case (1.1,1.1):
            leakage_current=VI_data_1['igate'].values[0]+VI_data_2['igate'].values[0]
        case _:
            print("Invalid combination")
    print(leakage_current)
    with open('Estimations.txt', 'a') as f:
        f.write(f"NMOS stack:\nvsd1: {__round(row['v(sd1)'])}, vgen: {__round(row['vgen'])},va: {__round(row['va'])},vb: {__round(row['vb'])}\n")
        f.write('M1(Bottom):\n')
        f.write(VI_data_1.to_string(index=False)+'\n')
        f.write('M2(Top):\n')
        f.write(VI_data_2.to_string(index=False)+'\n')
        f.write(f'Estimated Leakage Current:{leakage_current}\n\n')

df_p = pd.read_csv("STACKED_MOS_files\\temp\outputs\AandBp.csv")


for index, row in df_p.iterrows():
    print(f"Index: {index}")
    print(f"vsd1: {__round(row['v(sd1)'])}, vgen: {__round(row['vgen'])},va: {__round(row['va'])},vb: {__round(row['vb'])}")
    # M1
    drain = 0
    gate = __round(row['va'])
    source = __round(row['v(sd1)'])
    body = Vdd
    VI_data_1=fetch_currents_pmos(drain,gate,source,body)
    # M2
    drain = __round(row['v(sd1)'])
    gate = __round(row['vb'])
    source = __round(row['vgen'])
    body = Vdd
    VI_data_2=fetch_currents_pmos(drain,gate,source,body)

    print(VI_data_1)
    print(VI_data_2)
    match (VI_data_1['vgate'].values[0], VI_data_2['vgate'].values[0]):
        case (1.1, 1.1):
            leakage_current=VI_data_1['idrain'].values[0]
        case (1.1, 0):
            leakage_current=VI_data_1['idrain'].values[0]+VI_data_2['igate'].values[0]
        case (0, 1.1):
            leakage_current=VI_data_1['igate'].values[0]+VI_data_2['idrain'].values[0]
        case (0,0):
            leakage_current=VI_data_1['igate'].values[0]+VI_data_2['igate'].values[0]
        case _:
            print("Invalid combination")
    print(leakage_current)
    
    with open('Estimations.txt', 'a') as f:
        f.write(f"PMOS stack:\nvsd1: {__round(row['v(sd1)'])}, vgen: {__round(row['vgen'])},va: {__round(row['va'])},vb: {__round(row['vb'])}\n")
        f.write('M1(Bottom):\n')
        f.write(VI_data_1.to_string(index=False)+'\n')
        f.write('M2(Top):\n')
        f.write(VI_data_2.to_string(index=False)+'\n')
        f.write(f'Estimated Leakage Current:{leakage_current}\n\n')
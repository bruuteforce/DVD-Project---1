import pandas as pd

def round0_05(value):
    return round(value*20)/20

Vdd=1.1

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
    print(f"vsd1: {round0_05(row['v(sd1)'])}, vgen: {round0_05(row['vgen'])},va: {round0_05(row['va'])},vb: {round0_05(row['vb'])}")
    # M1
    drain = round0_05(row['v(sd1)'])
    gate = round0_05(row['va'])
    source = 0
    body = 0
    VI_data_1=fetch_currents_nmos(drain,gate,source,body)
    # M2
    drain = round0_05(row['vgen'])
    gate = round0_05(row['vb'])
    source = round0_05(row['v(sd1)'])
    body = 0
    VI_data_2=fetch_currents_nmos(drain,gate,source,body)

    print(VI_data_1)
    print(VI_data_2)

df_p = pd.read_csv("STACKED_MOS_files\\temp\outputs\AandBp.csv")


for index, row in df_p.iterrows():
    print(f"Index: {index}")
    print(f"vsd1: {round0_05(row['v(sd1)'])}, vgen: {round0_05(row['vgen'])},va: {round0_05(row['va'])},vb: {round0_05(row['vb'])}")
    # M1
    drain = 0
    gate = round0_05(row['va'])
    source = round0_05(row['v(sd1)'])
    body = 1.1
    VI_data_1=fetch_currents_pmos(drain,gate,source,body)
    # M2
    drain = round0_05(row['v(sd1)'])
    gate = round0_05(row['vb'])
    source = round0_05(row['vgen'])
    body = 1.1
    VI_data_2=fetch_currents_pmos(drain,gate,source,body)

    # print(VI_data_1)
    # print(VI_data_2)
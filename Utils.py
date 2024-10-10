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

n_on_2 = pd.read_csv("DVD_MOS_files\\temp\outputs\\NMOS_ON2.csv")
n_off_2 = pd.read_csv("DVD_MOS_files\\temp\outputs\\NMOS_OFF2.csv")
p_on_2 = pd.read_csv("DVD_MOS_files\\temp\outputs\PMOS_ON2.csv")
p_off_2 = pd.read_csv("DVD_MOS_files\\temp\outputs\PMOS_OFF2.csv")

n_on_4 = pd.read_csv("DVD_MOS_files\\temp\outputs\\NMOS_ON4.csv")
n_off_4 = pd.read_csv("DVD_MOS_files\\temp\outputs\\NMOS_OFF4.csv")
p_on_4 = pd.read_csv("DVD_MOS_files\\temp\outputs\PMOS_ON4.csv")
p_off_4 = pd.read_csv("DVD_MOS_files\\temp\outputs\PMOS_OFF4.csv")

def update_estims(MOS_TYP,row,VI_data_1,VI_data_2,leakage_current):
    with open('Estimations.txt', 'a') as f:
        f.write(f"{MOS_TYP} stack:\nvsd1: {__round(row['v(sd1)'])}, vgen: {__round(row['vgen'])},va: {__round(row['va'])},vb: {__round(row['vb'])}\n")
        f.write('M1(Bottom):\n')
        f.write(VI_data_1.to_string(index=False)+'\n')
        f.write('M2(Top):\n')
        f.write(VI_data_2.to_string(index=False)+'\n')
        f.write(f'Estimated Leakage Current:{leakage_current}\n')
        f.write(f"Simulated Leakage Current:{row['current']}\n")
        f.write(f"{100*abs((abs(leakage_current)-abs(row['current']))/row['current'])}\n\n")

def update_estims1(MOS_TYP,row,VI_data_P1,VI_data_P2,VI_data_N1,VI_data_N2,leakage_current):
    with open('Estimations.txt', 'a') as f:
        if MOS_TYP=="NAND":
           f.write(f"{MOS_TYP}:\nva: {__round(row['v(nodea)'])},vb: {__round(row['v(nodeb)'])}\n")
        else:
            f.write(f"{MOS_TYP}:\nva: {__round(row['v(nodea)'])}\n")
        f.write('P1(a):\n')
        f.write(VI_data_P1.to_string(index=False)+'\n')
        (MOS_TYP!="INVERTER") and f.write('P2(b):\n')
        (MOS_TYP!="INVERTER") and f.write(VI_data_P2.to_string(index=False)+'\n')
        f.write('N1(a):\n')
        f.write(VI_data_N1.to_string(index=False)+'\n')
        (MOS_TYP!="INVERTER") and f.write('N2(b):\n')
        (MOS_TYP!="INVERTER") and f.write(VI_data_N2.to_string(index=False)+'\n')
        f.write(f'Estimated Leakage Current:{leakage_current}\n')
        f.write(f"Simulated Leakage Current:{row['current_total']}\n")
        f.write(f"{100*abs((abs(leakage_current)-abs(row['current_total']))/row['current_total'])}\n\n")

def fetch_currents_nmos(drain,gate,source,body,scaling=1):
    if gate>Vdd/2.0 :
        match(scaling):
            case(1):
                actv_df=n_on_1
            case(2):
                actv_df=n_on_2
            case(4):
                actv_df=n_on_4
            case _:
                print("update logic")
        # print("ON")
    else :
        # print("OFF")
         match(scaling):
            case(1):
                actv_df=n_off_1
            case(2):
                actv_df=n_off_2
            case(4):
                actv_df=n_off_4
            case _:
                print("update logic")
    # print(drain,gate,source,body)
    match=actv_df.loc[(actv_df['vdrain']==drain) & (actv_df['vsource']==source) & (actv_df['vgate']==gate) & (actv_df['vbody']==body)]
    # print(actv_df.loc[(actv_df['vdrain']==drain) & (actv_df['vsource']==source) & (actv_df['vgate']==gate) & (actv_df['vbody']==body)])
    return match

def fetch_currents_pmos(drain,gate,source,body,scaling=1):
    if gate<Vdd/2.0 :
        match(scaling):
            case(1):
                actv_df=p_on_1
            case(2):
                actv_df=p_on_2
            case(4):
                actv_df=p_on_4
            case _:
                print("update logic")
        # print("ON")
    else :
        # print("OFF")
        match(scaling):
            case(1):
                actv_df=p_off_1
            case(2):
                actv_df=p_off_2
            case(4):
                actv_df=p_off_4
            case _:
                print("update logic")
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
    match (VI_data_1['vgate'].values[0], VI_data_2['vgate'].values[0],row['vgen']):
        case (0, 0, 1.1):
            leakage_current=VI_data_2['idrain'].values[0]
            update_estims("NMOS",row,VI_data_1,VI_data_2,leakage_current)
        case (0, 1.1, 1.1):
            leakage_current=VI_data_1['idrain'].values[0]+VI_data_2['igate'].values[0]
            update_estims("NMOS",row,VI_data_1,VI_data_2,leakage_current)
        case (1.1, 0, 1.1):
            leakage_current=VI_data_1['igate'].values[0]+VI_data_2['idrain'].values[0]
            update_estims("NMOS",row,VI_data_1,VI_data_2,leakage_current)
        case (1.1, 1.1, 0):
            leakage_current=VI_data_1['igate'].values[0]+VI_data_2['igate'].values[0]
            update_estims("NMOS",row,VI_data_1,VI_data_2,leakage_current)
        case _:
            print("Invalid combination")

df_p = pd.read_csv("STACKED_MOS_files\\temp\outputs\AandBp.csv")


for index, row in df_p.iterrows():
    print(f"Index: {index}")
    print(f"vsd1: {__round(row['v(sd1)'])}, vgen: {__round(row['vgen'])},va: {__round(row['va'])},vb: {__round(row['vb'])}")
    # M1
    drain = __round(row['vgnd'])
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
    match (VI_data_1['vgate'].values[0], VI_data_2['vgate'].values[0],row['vgnd']):
        case (1.1, 1.1, 0):
            leakage_current=VI_data_1['idrain'].values[0]
            update_estims("PMOS",row,VI_data_1,VI_data_2,leakage_current)
        case (1.1, 0, 0):
            leakage_current=VI_data_1['idrain'].values[0]+VI_data_2['igate'].values[0]
            update_estims("PMOS",row,VI_data_1,VI_data_2,leakage_current)
        case (0, 1.1, 0):
            leakage_current=VI_data_1['igate'].values[0]+VI_data_2['idrain'].values[0]
            update_estims("PMOS",row,VI_data_1,VI_data_2,leakage_current)
        case (0 , 0, 1.1):
            leakage_current=VI_data_1['igate'].values[0]+VI_data_2['igate'].values[0]
            update_estims("PMOS",row,VI_data_1,VI_data_2,leakage_current)
        case _:
            print("Invalid combination")

df_Inv = pd.read_csv("CMOS_GATE_files\\temp\outputs\Inverter.csv")
df_Inv_altr=pd.DataFrame()
for index, row in df_Inv.iterrows():
    #v(node1),v(nodea),v(nodez),current_vdd,current_total
    #PMOS
    drain = __round(row['v(nodez)'])
    gate = __round(row['v(nodea)'])
    source = __round(row['v(node1)'])
    body = __round(row['v(node1)'])
    VI_data_P=fetch_currents_pmos(drain,gate,source,body,2)
    #NMOS
    drain = __round(row['v(nodez)'])
    gate = __round(row['v(nodea)'])
    source = 0
    body = 0
    VI_data_N=fetch_currents_nmos(drain,gate,source,body,1)
    print(f"\nInverter:(va:{__round(row['v(nodea)'])})\n{VI_data_P}\n{VI_data_N}\ncurrent_vdd:{row['current_vdd']}\ncurrent_total:{row['current_total']}")

    row_df = row.to_frame().T 
    match (__round(row['v(nodea)'])):
        case (0):
            leakage_current=VI_data_N['isource'].values[0]+VI_data_N['igate'].values[0]+VI_data_P['igate'].values[0]
            update_estims1("INVERTER",row,VI_data_P,None,VI_data_N,None,leakage_current)
            row_df['estimated_leakage'] = leakage_current
        case (1.1):
            leakage_current=VI_data_P['isource'].values[0]+VI_data_N['igate'].values[0]+VI_data_P['igate'].values[0]
            update_estims1("INVERTER",row,VI_data_P,None,VI_data_N,None,leakage_current)
            row_df['estimated_leakage'] = leakage_current

    df_Inv_altr = pd.concat([df_Inv_altr, row_df], ignore_index=True)

df_Inv_altr.to_csv("Inverter_altered.csv", index=False)


df_Nand = pd.read_csv("CMOS_GATE_files\\temp\outputs\\Nand.csv")
df_Nand_altr=pd.DataFrame()
for index, row in df_Nand.iterrows():
    #v(node1),v(nodea),v(nodeb),v(nodez),current_vdd,current_total
    #PMOS1
    drain = __round(row['v(nodez)'])
    gate = __round(row['v(nodea)'])
    source = __round(row['v(node1)'])
    body = __round(row['v(node1)'])
    VI_data_PA=fetch_currents_pmos(drain,gate,source,body,2)
    #PMOS2
    drain = __round(row['v(nodez)'])
    gate = __round(row['v(nodeb)'])
    source = __round(row['v(node1)'])
    body = __round(row['v(node1)'])
    VI_data_PB=fetch_currents_pmos(drain,gate,source,body,2)
    #NMOS1 (BOTTOM)
    drain = __round(row['v(sd2)'])
    gate = __round(row['v(nodea)'])
    source = 0
    body = 0
    VI_data_NA=fetch_currents_nmos(drain,gate,source,body,2)
    #NMOS2 (TOP)
    drain = __round(row['v(nodez)'])
    gate = __round(row['v(nodeb)'])
    source = __round(row['v(sd2)'])
    body = 0
    VI_data_NB=fetch_currents_nmos(drain,gate,source,body,2)
    print(f"\nNand:(va:{__round(row['v(nodea)'])},vb:{__round(row['v(nodeb)'])})\n{VI_data_PA}\n{VI_data_PB}\n{VI_data_NA}\n{VI_data_NB}\ncurrent_vdd:{row['current_vdd']}\ncurrent_total:{row['current_total']}")
    
    row_df = row.to_frame().T 

    match (__round(row['v(nodea)']), __round(row['v(nodeb)'])):
        case (0,0):
            leakage_current=VI_data_PA['igate'].values[0]+VI_data_PB['igate'].values[0]+VI_data_NB['igate'].values[0]+VI_data_NA['isource'].values[0]+VI_data_NA['ibody'].values[0]
            #lk=VI_data_PA['igate'].values[0]+VI_data_PB['igate'].values[0]-VI_data_NB['idrain'].values[0]
            update_estims1("NAND",row,VI_data_PA,VI_data_PB,VI_data_NA,VI_data_NB,leakage_current)
            #update_estims1("NAND",row,VI_data_PA,VI_data_PB,VI_data_NA,VI_data_NB,lk)
            row_df['estimated_leakage'] = leakage_current
        case (0,1.1):
            #leakage_current=VI_data_PA['igate'].values[0]+VI_data_PA['ibody'].values[0]+VI_data_NA['isource'].values[0]+VI_data_NA['igate'].values[0]
            leakage_current=VI_data_PA['isource'].values[0]+VI_data_PA['idrain'].values[0]+VI_data_NA['idrain'].values[0]
            #lk=VI_data_PA['igate'].values[0]-VI_data_NA['idrain'].values[0]
            #lk=VI_data_PA['igate'].values[0]+VI_data_PB['idrain'].values[0]-VI_data_NB['igate'].values[0]-VI_data_NA['idrain'].values[0]
            update_estims1("NAND",row,VI_data_PA,VI_data_PB,VI_data_NA,VI_data_NB,leakage_current)
            #update_estims1("NAND",row,VI_data_PA,VI_data_PB,VI_data_NA,VI_data_NB,lk)
            row_df['estimated_leakage'] = leakage_current
        case (1.1, 0):
            leakage_current=VI_data_PB['igate'].values[0]-VI_data_NA['igate'].values[0]+VI_data_NB['igate'].values[0]+VI_data_NB['isource'].values[0]
            #lk=VI_data_PA['idrain'].values[0]+VI_data_PB['igate'].values[0]-VI_data_NB['idrain'].values[0]-VI_data_NA['igate'].values[0]
            update_estims1("NAND",row,VI_data_PA,VI_data_PB,VI_data_NA,VI_data_NB,leakage_current)
            #update_estims1("NAND",row,VI_data_PA,VI_data_PB,VI_data_NA,VI_data_NB,lk)
            row_df['estimated_leakage'] = leakage_current
        case (1.1, 1.1):
            leakage_current=VI_data_PA['igate'].values[0]+VI_data_PB['igate'].values[0]+VI_data_NA['igate'].values[0]+VI_data_NB['igate'].values[0]+VI_data_PA['isource'].values[0]+VI_data_PB['isource'].values[0]
            #lk=VI_data_PA['idrain'].values[0]+VI_data_PB['idrain'].values[0]-VI_data_NB['igate'].values[0]-VI_data_NA['igate'].values[0]
            update_estims1("NAND",row,VI_data_PA,VI_data_PB,VI_data_NA,VI_data_NB,leakage_current)
            #update_estims1("NAND",row,VI_data_PA,VI_data_PB,VI_data_NA,VI_data_NB,lk)
            row_df['estimated_leakage'] = leakage_current
        case _:
            print("Invalid combination")
            
    df_Nand_altr = pd.concat([df_Nand_altr, row_df], ignore_index=True)

df_Nand_altr.to_csv("Nand_altered.csv", index=False)

df_Nor = pd.read_csv("CMOS_GATE_files\\temp\outputs\\Nor.csv")
for index, row in df_Nor.iterrows():
    #v(node1),v(nodea),v(nodeb),v(nodez),v(node2),current_vdd,current_total
    #PMOS1
    drain = __round(row['v(node2)'])
    gate = __round(row['v(nodea)'])
    source = __round(row['v(node1)'])
    body = __round(row['v(node1)'])
    VI_data_P1=fetch_currents_pmos(drain,gate,source,body,4)
    #PMOS2
    drain = __round(row['v(nodez)'])
    gate = __round(row['v(nodeb)'])
    source = __round(row['v(node2)'])
    body = __round(row['v(node1)'])
    VI_data_P2=fetch_currents_pmos(drain,gate,source,body,4)
    #NMOS1
    drain = __round(row['v(nodez)'])
    gate = __round(row['v(nodea)'])
    source = 0
    body = 0
    VI_data_N1=fetch_currents_nmos(drain,gate,source,body,1)
    #NMOS2
    drain = __round(row['v(nodez)'])
    gate = __round(row['v(nodeb)'])
    source = 0
    body = 0
    VI_data_N2=fetch_currents_nmos(drain,gate,source,body,1)
    print(f"\nNor:(va:{__round(row['v(nodea)'])},vb:{__round(row['v(nodeb)'])})\n{VI_data_P1}\n{VI_data_P2}\n{VI_data_N1}\n{VI_data_N2}\ncurrent_vdd:{row['current_vdd']}\ncurrent_total:{row['current_total']}")

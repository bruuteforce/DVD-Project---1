import pandas as pd


filename = 'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\temp\outputs\\NMOS_OFF1.csv'
df = pd.read_csv(filename)
row=df.loc[(df['vdrain'] == 0) & (df['vsource'] == 0.05),'idrain'].values[0]
print(row)

Generator.py:
->Generates the single MOS data for NMOS,PMOS with varying Widths,Vd,Vs \
    Outputs stored at DVD_MOS_files\temp \n
->Generates the Stacked MOS data for NMOS and PMOS with varying Va,Vb \
    Outputs stored at STACKED_MOS_files\temp \n

Utils.py:
Finds the single MOS data corresponding to the obtained Stacked MOS data(Intermediate node voltages) and estimates the leakage current \
    Output stored in Estimations.txt file

Setup:\
install pandas and openpyxl pip packages:\
pip install openpyxl \n
pip install pandas

Add your ngspice bin folder in environment Path variable:\
Open "Edit the system environment variables" --> "Environment variables" \
In "System Variables" double click on "Path" and add the ngspice bin folder Path in the list of Paths 

![alt text](image.png)
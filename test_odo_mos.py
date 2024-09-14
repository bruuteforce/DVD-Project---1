from ODO_MOS import parse_file
import sys
import os

# Print the name of the script
print("Script name:", sys.argv[0])

# Print the arguments
for i in range(1, len(sys.argv)):
    print(f"Argument {i}:", sys.argv[i])

##For Signle MOS
# os.system('ngspice_con -b DVD_MOS_files\\NMOS_off.ckt')
# Example usage:
# columns=['vdrain','vgate','vsource','vbody','idrain','igate','isource','ibody']
# parse_file(sys.argv[1],"v(drain)",columns)

##For Stacked MOS
os.system('ngspice_con -b "E:\DVD\\tutorial\\ngspice-43_64\\Spice64\\bin\AandBn_HP.net"')
# Example usage:
columns=['v(sd1)','power?','vgen','va','vb']
parse_file(sys.argv[1],"v(sd1)",columns)
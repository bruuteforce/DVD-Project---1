from ODO_MOS import parse_file
import sys
import os

# Print the name of the script
print("Script name:", sys.argv[0])

# Print the arguments
for i in range(1, len(sys.argv)):
    print(f"Argument {i}:", sys.argv[i])

os.system('ngspice_con -b DVD_MOS_files\\NMOS_off.ckt')
# Example usage:
parse_file(sys.argv[1])
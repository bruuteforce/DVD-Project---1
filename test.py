import shutil
import os
from ODO_MOS import parse_file

def copy_and_edit_file(src_path, dest_path, old_string1, new_string1, old_string2, new_string2):
    # Copy the file
    shutil.copy(src_path, dest_path)
    
    # Read the content of the copied file
    with open(dest_path, 'r') as file:
        file_data = file.read()
    
    # Replace the target string
    file_data = file_data.replace(old_string1, new_string1)
    file_data = file_data.replace(old_string2, new_string2)

    # Write the modified content back to the file
    with open(dest_path, 'w') as file:
        file.write(file_data)

# Example usage
if not os.path.exists('E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\temp'):
    os.mkdir('E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\temp')
    os.mkdir('E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\temp\\outputs')

##maybe do a for loop

columns=['vdrain','vgate','vsource','vbody','idrain','igate','isource','ibody']
##NMOS OFF
source_file = 'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\NMOS_off.ckt'
for i in [1, 2, 3, 4, 6, 8]:
    destination_file = f'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\temp\\NMOS_off{i}.ckt'
    string_to_replace1 = '.PARAM Wmin=45n'
    new_string1 = f'.PARAM Wmin=45n*{i}'
    string_to_replace2 = 'NMOS_off.txt'
    new_string2 = f'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\temp\\outputs\\NMOS_OFF{i}.txt'
    copy_and_edit_file(source_file, destination_file, string_to_replace1, new_string1, string_to_replace2, new_string2)
    os.system(f'ngspice_con -b DVD_MOS_files\\temp\\NMOS_off{i}.ckt')
    parse_file(f'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\temp\\outputs\\NMOS_OFF{i}.txt',"v(drain)",columns)
    ##print("File copied and string replaced successfully.")

##NMOS ON
source_file = 'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\NMOS_on.ckt'
for i in [1, 2, 3, 4, 6, 8]:
    destination_file = f'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\temp\\NMOS_on{i}.ckt'
    string_to_replace1 = '.PARAM Wmin=45n'
    new_string1 = f'.PARAM Wmin=45n*{i}'
    string_to_replace2 = 'NMOS_on.txt'
    new_string2 = f'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\temp\\outputs\\NMOS_ON{i}.txt'
    copy_and_edit_file(source_file, destination_file, string_to_replace1, new_string1, string_to_replace2, new_string2)
    os.system(f'ngspice_con -b DVD_MOS_files\\temp\\NMOS_on{i}.ckt')
    parse_file(f'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\temp\\outputs\\NMOS_ON{i}.txt',"v(drain)",columns)

#PMOS OFF
source_file = 'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\PMOS_off.ckt'
for i in [1, 2, 3, 4, 6, 8]:
    destination_file = f'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\temp\\PMOS_off{i}.ckt'
    string_to_replace1 = '.PARAM Wmin=45n'
    new_string1 = f'.PARAM Wmin=45n*{i}'
    string_to_replace2 = 'PMOS_off.txt'
    new_string2 = f'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\temp\\outputs\\PMOS_OFF{i}.txt'
    copy_and_edit_file(source_file, destination_file, string_to_replace1, new_string1, string_to_replace2, new_string2)
    os.system(f'ngspice_con -b DVD_MOS_files\\temp\\PMOS_off{i}.ckt')
    parse_file(f'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\temp\\outputs\\PMOS_OFF{i}.txt',"v(drain)",columns)

source_file = 'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\PMOS_on.ckt'
for i in [1, 2, 3, 4, 6, 8]:
    destination_file = f'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\temp\\PMOS_on{i}.ckt'
    string_to_replace1 = '.PARAM Wmin=45n'
    new_string1 = f'.PARAM Wmin=45n*{i}'
    string_to_replace2 = 'PMOS_on.txt'
    new_string2 = f'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\temp\\outputs\\PMOS_ON{i}.txt'
    copy_and_edit_file(source_file, destination_file, string_to_replace1, new_string1, string_to_replace2, new_string2)
    os.system(f'ngspice_con -b DVD_MOS_files\\temp\\PMOS_on{i}.ckt')
    parse_file(f'E:\DVD\project_1\DVD-Project---1\DVD_MOS_files\\temp\\outputs\\PMOS_ON{i}.txt',"v(drain)",columns)
    
import shutil
import os
from ODO_MOS import parse_file

def copy_and_edit_file(src_path, dest_path, old_string1, new_string1, old_string2="####", new_string2="####"):
    # Copy the file
    shutil.copy(src_path, dest_path)
    
    # Read the content of the copied file
    with open(dest_path, 'r') as file:
        file_data = file.read()
    
    # Replace the target string
    file_data = file_data.replace(old_string1, new_string1)
    if new_string2 != "####" :
        file_data = file_data.replace(old_string2, new_string2)

    # Write the modified content back to the file
    with open(dest_path, 'w') as file:
        file.write(file_data)

# Example usage
if not os.path.exists('DVD_MOS_files\\temp'):
    os.mkdir('DVD_MOS_files\\temp')
    os.mkdir('DVD_MOS_files\\temp\\outputs')

    ##maybe do a for loop

    columns=['vdrain','vgate','vsource','vbody','idrain','igate','isource','ibody']
    ##NMOS OFF
    source_file = 'DVD_MOS_files\\NMOS_off.ckt'
    for i in [1, 2, 3, 4, 6, 8]:
        destination_file = f'DVD_MOS_files\\temp\\NMOS_off{i}.ckt'
        string_to_replace1 = '.PARAM Wmin=45n'
        new_string1 = f'.PARAM Wmin=45n*{i}'
        string_to_replace2 = 'NMOS_off.txt'
        new_string2 = f'DVD_MOS_files\\temp\\outputs\\NMOS_OFF{i}.txt'
        copy_and_edit_file(source_file, destination_file, string_to_replace1, new_string1, string_to_replace2, new_string2)
        os.system(f'ngspice_con -b DVD_MOS_files\\temp\\NMOS_off{i}.ckt')
        parse_file(f'DVD_MOS_files\\temp\\outputs\\NMOS_OFF{i}.txt',"v(drain)",columns)
        ##print("File copied and string replaced successfully.")

    ##NMOS ON
    source_file = 'DVD_MOS_files\\NMOS_on.ckt'
    for i in [1, 2, 3, 4, 6, 8]:
        destination_file = f'DVD_MOS_files\\temp\\NMOS_on{i}.ckt'
        string_to_replace1 = '.PARAM Wmin=45n'
        new_string1 = f'.PARAM Wmin=45n*{i}'
        string_to_replace2 = 'NMOS_on.txt'
        new_string2 = f'DVD_MOS_files\\temp\\outputs\\NMOS_ON{i}.txt'
        copy_and_edit_file(source_file, destination_file, string_to_replace1, new_string1, string_to_replace2, new_string2)
        os.system(f'ngspice_con -b DVD_MOS_files\\temp\\NMOS_on{i}.ckt')
        parse_file(f'DVD_MOS_files\\temp\\outputs\\NMOS_ON{i}.txt',"v(drain)",columns)

    #PMOS OFF
    source_file = 'DVD_MOS_files\\PMOS_off.ckt'
    for i in [1, 2, 3, 4, 6, 8]:
        destination_file = f'DVD_MOS_files\\temp\\PMOS_off{i}.ckt'
        string_to_replace1 = '.PARAM Wmin=45n'
        new_string1 = f'.PARAM Wmin=45n*{i}'
        string_to_replace2 = 'PMOS_off.txt'
        new_string2 = f'DVD_MOS_files\\temp\\outputs\\PMOS_OFF{i}.txt'
        copy_and_edit_file(source_file, destination_file, string_to_replace1, new_string1, string_to_replace2, new_string2)
        os.system(f'ngspice_con -b DVD_MOS_files\\temp\\PMOS_off{i}.ckt')
        parse_file(f'DVD_MOS_files\\temp\\outputs\\PMOS_OFF{i}.txt',"v(drain)",columns)

    source_file = 'DVD_MOS_files\\PMOS_on.ckt'
    for i in [1, 2, 3, 4, 6, 8]:
        destination_file = f'DVD_MOS_files\\temp\\PMOS_on{i}.ckt'
        string_to_replace1 = '.PARAM Wmin=45n'
        new_string1 = f'.PARAM Wmin=45n*{i}'
        string_to_replace2 = 'PMOS_on.txt'
        new_string2 = f'DVD_MOS_files\\temp\\outputs\\PMOS_ON{i}.txt'
        copy_and_edit_file(source_file, destination_file, string_to_replace1, new_string1, string_to_replace2, new_string2)
        os.system(f'ngspice_con -b DVD_MOS_files\\temp\\PMOS_on{i}.ckt')
        parse_file(f'DVD_MOS_files\\temp\\outputs\\PMOS_ON{i}.txt',"v(drain)",columns)
        

if not os.path.exists('STACKED_MOS_files\\temp'):
    os.mkdir('STACKED_MOS_files\\temp')
    os.mkdir('STACKED_MOS_files\\temp\\outputs')

    columns=['v(sd1)','current','vgen','va','vb']
    source_file = 'STACKED_MOS_files\AandBn.ckt'
    destination_file = f'STACKED_MOS_files\\temp\\AandBn.ckt'
    # string_to_replace1 = '.PARAM Wmin=45n'
    # new_string1 = f'.PARAM Wmin=45n*{i}'
    string_to_replace2 = 'AandBn.txt'
    new_string2 = f'STACKED_MOS_files\\temp\\outputs\\AandBn.txt'
    copy_and_edit_file(source_file, destination_file, string_to_replace2, new_string2)
    os.system(f'ngspice_con -b STACKED_MOS_files\\temp\\AandBn.ckt')
    parse_file(f'STACKED_MOS_files\\temp\\outputs\\AandBn.txt',"v(sd1)",columns)

    columns=['v(sd1)','current','vgen','vgnd','va','vb']
    source_file = 'STACKED_MOS_files\AandBp.ckt'
    destination_file = f'STACKED_MOS_files\\temp\\AandBp.ckt'
    # string_to_replace1 = '.PARAM Wmin=45n'
    # new_string1 = f'.PARAM Wmin=45n*{i}'
    string_to_replace2 = 'AandBp.txt'
    new_string2 = f'STACKED_MOS_files\\temp\\outputs\\AandBp.txt'
    copy_and_edit_file(source_file, destination_file, string_to_replace2, new_string2)
    os.system(f'ngspice_con -b STACKED_MOS_files\\temp\\AandBp.ckt')
    parse_file(f'STACKED_MOS_files\\temp\\outputs\\AandBp.txt',"v(sd1)",columns)


if not os.path.exists('CMOS_GATE_files\\temp'):
    os.mkdir('CMOS_GATE_files\\temp')
    os.mkdir('CMOS_GATE_files\\temp\\outputs')
#inverter
    columns=['v(node1)','v(nodea)','v(nodez)','current_vdd','current_total']
    source_file = 'CMOS_GATE_files\inverter.net'
    destination_file = f'CMOS_GATE_files\\temp\\Inverter.net'
    # string_to_replace1 = '.PARAM Wmin=45n'
    # new_string1 = f'.PARAM Wmin=45n*{i}'
    string_to_replace2 = 'Inverter.txt'
    new_string2 = f'CMOS_GATE_files\\temp\\outputs\\Inverter.txt'
    copy_and_edit_file(source_file, destination_file, string_to_replace2, new_string2)
    os.system(f'ngspice_con -b CMOS_GATE_files\\temp\\Inverter.net')
    parse_file(f'CMOS_GATE_files\\temp\\outputs\\Inverter.txt',"v(node1)",columns)
#nand
    columns=['v(node1)','v(nodea)','v(nodeb)','v(nodez)','v(sd2)','current_vdd','current_total']
    source_file = 'CMOS_GATE_files\\nand.net'
    destination_file = f'CMOS_GATE_files\\temp\\Nand.net'
    # string_to_replace1 = '.PARAM Wmin=45n'
    # new_string1 = f'.PARAM Wmin=45n*{i}'
    string_to_replace2 = 'Nand.txt'
    new_string2 = f'CMOS_GATE_files\\temp\\outputs\\Nand.txt'
    copy_and_edit_file(source_file, destination_file, string_to_replace2, new_string2)
    os.system(f'ngspice_con -b CMOS_GATE_files\\temp\\Nand.net')
    parse_file(f'CMOS_GATE_files\\temp\\outputs\\Nand.txt',"v(node1)",columns)
#nor
    columns=['v(node1)','v(nodea)','v(nodeb)','v(nodez)','v(node2)','current_vdd','current_total']
    source_file = 'CMOS_GATE_files\\nor.net'
    destination_file = f'CMOS_GATE_files\\temp\\Nor.net'
    # string_to_replace1 = '.PARAM Wmin=45n'
    # new_string1 = f'.PARAM Wmin=45n*{i}'
    string_to_replace2 = 'Nor.txt'
    new_string2 = f'CMOS_GATE_files\\temp\\outputs\\Nor.txt'
    copy_and_edit_file(source_file, destination_file, string_to_replace2, new_string2)
    os.system(f'ngspice_con -b CMOS_GATE_files\\temp\\Nor.net')
    parse_file(f'CMOS_GATE_files\\temp\\outputs\\Nor.txt',"v(node1)",columns)
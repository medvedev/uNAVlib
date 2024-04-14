filename_inav = "msp_codes_from_inav.txt"
filename_bf = "msp_codes_from_bf.txt"

with open(filename_inav, 'r') as f:
    data_inav = f.readlines()

with open(filename_bf, 'r') as f:
    data_bf = f.readlines()

codes = {}
for l in data_inav:
    if '#define MSP' in l:
        if l[0] != '/':
            code_str, code_value = l.split()[1:3]
            codes[code_str] = eval(code_value)

for l in data_bf:
    if '#define MSP' in l:
        if l[0] != '/':
            code_str, code_value = l.split()[1:3]
            code_value = eval(code_value)
            if code_str in codes:
                if codes[code_str] != code_value:
                    print(f"{code_str} BF={code_value} but INAV={codes[code_str]}")
                    continue
            codes[code_str] = code_value

with open('../enums/msp_codes.py','w') as f:
    f.write("MSPCodes = {\n")
    for code in codes:
        f.write(f"\'{code}\': {codes[code]},\n")

    f.write('}\n')
    f.write("# The idea is to automate, so only the dictionary above needs to be updated\n")
    f.write("MSPCodes2Str = {v: i for i,v in MSPCodes.items()}\n")
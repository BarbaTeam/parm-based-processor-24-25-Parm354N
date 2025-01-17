def file_convert(file_path): 
    with open(file_path, 'r') as file: 
        lines =  file.readlines()
    n = len(lines)
    str = ""
    for lineIndex in range(n): 
        if (lines[lineIndex][0] != '@' and len(lines[lineIndex][:-1]) > 0): 
            str += (assemble_instruction(lines[lineIndex][:-1]) + " ")
    return str


#PROBLEM SOME OF THE INSTRUCTIONS HAVE SAME NAME DIFFERET OPCODE: NEED TO USE ARUGMENTS
def write_string_to_txt_file(string, file_name):
    with open(file_name, 'w') as file:
        file.write(string)

def assemble_instruction(instruction):
    # Define the instruction set and their binary opcodes
    instruction_set = {
        "lsls": ["00000", "0100000010"],
        "lsrs": ["00001", "0100000011"],
        "asrs": ["00010", "0100000100"],
        "adds": "0001100",
        "subs": "0001101",
        "movs": "00100",
        "ands": "0100000000",
        "eors": "0100000001",
        "adcs": "0100000101",
        "sbcs": "0100000110",
        "rors": "0100000111",
        "tst":  "0100001000",
        "rsbs": "0100001001",
        "cmp":  "0100001010",
        "cmn":  "0100001011",
        "orrs": "0100001100",
        "muls": "0100001101",
        "bics": "0100001110",
        "mvns": "0100001111",
        "str": "10010",
        "ldr": "10011",
        "add": "101100000",
        "sub": "101100001",
        "b": "11011110",
        "beq": "11010000",
        "bne": "11010001",
        "bcs": "11010010",
        "bcc": "11010011",
        "bmi": "11010100",
        "bpl": "11010101",
        "bvs": "11010110",
        "bvc": "11010111",
        "bhi": "11011000",
        "bls": "11011001",
        "bge": "11011010",
        "blt": "11011011",
        "bgt": "11011100",
        "ble": "11011101",
        "bal": "1110"
    }

    # Function to convert register and immediate values to binary
    def to_binary(value, bits):
        return format(int(value), f'0{bits}b')

    # Split the instruction into parts
    parts = instruction.split()
    if (len(parts) < 1): 
        print("yo im right here man")
    instr = parts[0]
    operands = []
    for i in range(1, len(parts)): 
        operands.append(parts[i].split(',')[0])

    # Initialize the binary code
    binary_code = ''
    if instr == 'movs':
        rd = int(operands[0][1:])
        imm8 = int(operands[1][1:])
        binary_code = f"{instruction_set[instr]}{to_binary(rd, 3)}{to_binary(imm8, 8)}"


    elif instr in ["lsls", "lsrs", "asrs"]: 
        rd = int(operands[0][1:])
        rm = int(operands[1][1:])
        if (len(operands) == 3): 
            imm5 = int(operands[2][1:])
            binary_code = f"{instruction_set[instr][0]}{to_binary(imm5, 5)}{to_binary(rm, 3)}{to_binary(rd, 3)}"
        elif (len(operands) == 2): 
            binary_code = f"{instruction_set[instr][1]}{to_binary(rm, 3)}{to_binary(rd, 3)}"


    elif instr in ['ands', 'eors', 'adcs', 'sbcs', 'rors', 'tst', 'rsbs', 'cmp', 'cmn', 'orrs', 'muls', 'bics', 'mvns']:
        rd = int(operands[0][1:])
        rm = int(operands[1][1:])
        binary_code = f"{instruction_set[instr]}{to_binary(rm, 3)}{to_binary(rd, 3)}"
    elif instr in ['adds', 'subs']:
        rd = int(operands[0][1:])
        rn = int(operands[1][1:])
        rm = int(operands[2][1:])
        binary_code = f"{instruction_set[instr]}{to_binary(rm, 3)}{to_binary(rn, 3)}{to_binary(rd, 3)}"
    elif instr in ['str', 'ldr']:
        rt = int(operands[0][1:])
        imm8 = int(operands[1][4:-1])
        binary_code = f"{instruction_set[instr]}{to_binary(rt, 3)}{to_binary(imm8, 8)}"
    elif instr in ['add_sp', 'sub_sp']:
        imm7 = int(operands[1][1:])
        binary_code = f"{instruction_set[instr]}{to_binary(imm7, 7)}"
    elif instr in ['b', 'beq', 'bne', 'bcs', 'bcc', 'bmi', 'bpl', 'bvs', 'bvc', 'bhi', 'bls', 'bge', 'blt', 'bgt', 'ble', 'bal']:
        imm8 = int(operands[0][1:])
        binary_code = f"{instruction_set[instr]}{to_binary(imm8, 8)}"
    else:
        raise ValueError("Instruction not supported")

    # Convert binary to hexadecimal
    hex_code = f"{int(binary_code, 2):04x}"
    return hex_code



def fullConvert(inputPathString, outPathString): 
    write_string_to_txt_file(file_convert(inputPathString), outPathString)

#fullConvert("C:\\Users\\Lohann\\Desktop\\parmTest.s", "C:\\Users\\Lohann\\Desktop\\testResultHexa.txt")



#fullConvert("C:\\Users\\Lohann\\Desktop\\parm\\13-16_instructions.s", "C:\\Users\\Lohann\\Desktop\\parm\\testRes13-16.txt")



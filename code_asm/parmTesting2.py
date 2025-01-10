def file_convert(file_path): 
    with open(file_path, 'r') as file: 
        lines =  file.readlines()
    n = len(lines)
    str = ""
    for lineIndex in range(n): 
        if (lines[lineIndex][0] != '@' and len(lines[lineIndex][:-1]) > 0): 
            str += (assemble_instruction(lines[lineIndex][:-1]) + " ")
    return str

def write_string_to_txt_file(string, file_name):
    with open(file_name, 'w') as file:
        file.write(string)

def assemble_instruction(instruction):
    # Define the instruction set and their binary opcodes
    instruction_set = {
        'movs': '00100',
        'ands': '0100000000',
        'eors': '0100000001',
        'lsls': '0100000010',
        'lsrs': '0100000011',
        # Add more instructions as needed
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
    elif instr in ['ands', 'eors', 'lsls', 'lsrs']:
        rd = int(operands[0][1:])
        rm = int(operands[1][1:])
        binary_code = f"{instruction_set[instr]}{to_binary(rm, 3)}{to_binary(rd, 3)}"
    else:
        raise ValueError("Instruction not supported")

    # Convert binary to hexadecimal
    hex_code = f"{int(binary_code, 2):04x}"
    return hex_code


def fullConvert(inputPathString, outPathString): 
    write_string_to_txt_file(file_convert(inputPathString), outPathString)

fullConvert("C:\\Users\\Lohann\\Desktop\\parmTest.s", "C:\\Users\\Lohann\\Desktop\\testResultHexa.txt")
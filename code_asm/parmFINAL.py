def file_convert(file_path): 
    with open(file_path, 'r') as file: 
        lines =  file.readlines()
    n = len(lines)
    str = ""
    labelsDict = parsLabels(lines, n)
    for lineIndex in range(n): 
        if (lines[lineIndex][0] != '@' and len(lines[lineIndex][:-1]) > 0): 
            str += (assemble_instruction(lines[lineIndex][:-1], labelsDict) + " ")
    return str


def write_string_to_txt_file(string, file_name):
    with open(file_name, 'w') as file:
        file.write(string)

def isLabel(line): 
    if len(line) == 0: 
        return False
    if len(line) == 1: 
        return line[-1] == ':'
    else: 
        return line[-1] == ':' or line[-2] == ':' or line[0] == '.'
        
def parsLabels(lineTable, length):
    labelDict = {}
    for lineIndex in range(length): 
        if isLabel(lineTable[lineIndex]): 
            labelDict[lineTable[lineIndex][:-2]] = lineIndex + 1
    return labelDict 

def convertLabelsToValue(labelDict, string): 
    if string in labelDict: 
        return labelDict[string]
    else: 
        return string

def assemble_instruction(instruction, labelsDict):
    # Define the instruction set and their binary opcodes
    instruction_set = {
        "lsls": ["00000", "0100000010"],
        "lsrs": ["00001", "0100000011"],
        "asrs": ["00010", "0100000100"],
        "adds": ["0001100", "0001110"],
        "subs": ["0001101", "0001111"],
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
        "b": "11100",
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
        "bal": "11100",
        "bnv": "11101"
    }

    # Function to convert register and immediate values to binary
    def to_binary(value, bits):
        return format(int(value), f'0{bits}b')

    # Split the instruction into parts
    parts = instruction.split()
    if (len(parts) < 1): 
        print("yo im right here man")
    instr = str.lower(parts[0])
    operands = []
    for i in range(1, len(parts)): 
        operands.append(convertLabelsToValue(labelsDict, parts[i].split(',')[0]))

    # Initialize the binary code
    binary_code = ''
    if instr == 'movs':
        rd = intOrString(operands[0])
        imm8 = intOrString(operands[1])
        binary_code = f"{instruction_set[instr]}{to_binary(rd, 3)}{to_binary(imm8, 8)}"


    elif instr in ["lsls", "lsrs", "asrs"]: 
        rd = intOrString(operands[0])
        rm = intOrString(operands[1])
        if (len(operands) == 3): 
            imm5 = intOrString(operands[2])
            binary_code = f"{instruction_set[instr][0]}{to_binary(imm5, 5)}{to_binary(rm, 3)}{to_binary(rd, 3)}"
        elif (len(operands) == 2): 
            binary_code = f"{instruction_set[instr][1]}{to_binary(rm, 3)}{to_binary(rd, 3)}"


    elif instr in ['ands', 'eors', 'adcs', 'sbcs', 'rors', 'tst', 'rsbs', 'cmp', 'cmn', 'orrs', 'muls', 'bics', 'mvns']:
        rd = intOrString(operands[0])
        rm = intOrString(operands[1])
        binary_code = f"{instruction_set[instr]}{to_binary(rm, 3)}{to_binary(rd, 3)}"
    elif instr in ['adds', 'subs']:
        rd, rn, rm = 0,0,0
        if (len(operands) == 2): 
            #yaboifucked
            rd = intOrString(operands[0])
            immX = intOrString(operands[1])
            binary_code = f"{instruction_set[instr][0]}{to_binary(immX, 3)}{to_binary(rd, 3)}{to_binary(rd, 3)}"

        else: 
            if operands[2][0] == '#': 
                rd = intOrString(operands[0])
                rn = intOrString(operands[1])
                imm3 = intOrString(operands[2])
                binary_code = f"{instruction_set[instr][1]}{to_binary(imm3, 3)}{to_binary(rn, 3)}{to_binary(rd, 3)}"
            else: 
                rd = intOrString(operands[0])
                rn = intOrString(operands[1])
                rm = intOrString(operands[2])
                binary_code = f"{instruction_set[instr][0]}{to_binary(rm, 3)}{to_binary(rn, 3)}{to_binary(rd, 3)}"
    elif instr in ['str', 'ldr']:
        rt = intOrString(operands[0])
        #imm8 = intOrString(operands[1], 4, -1)
        imm8 = 0
        binary_code = f"{instruction_set[instr]}{to_binary(rt, 3)}{to_binary(imm8, 8)}"
    elif instr in ['add_sp', 'sub_sp']:
        imm7 = intOrString(operands[1])
        binary_code = f"{instruction_set[instr]}{to_binary(imm7, 7)}"
    elif instr in ['beq', 'bne', 'bcs', 'bcc', 'bmi', 'bpl', 'bvs', 'bvc', 'bhi', 'bls', 'bge', 'blt', 'bgt', 'ble']:
        imm8 = intOrString(operands[0], 1)
        binary_code = f"{instruction_set[instr]}{to_binary(imm8, 8)}"
    elif instr in ['b', 'bal', 'bnv']: 
        imm11 = intOrString(operands[0], 1)
        binary_code = f"{instruction_set[instr]}{to_binary(imm11, 11)}"
    else:
        return ""
        raise ValueError("Instruction not supported")

    # Convert binary to hexadecimal
    hex_code = f"{int(binary_code, 2):04x}"
    return hex_code

def intOrString(operand, stringStart = 1, stringEnd = "NULL"): 
    if isinstance(operand, str): 
        if stringEnd == "NULL": 
            return int(operand[stringStart: ])
        else: 
            return int(operand[stringStart: stringEnd])

    elif isinstance(operand, int): 
        return operand
    else: 
        return "what on earth"

def fullConvert(inputPathString, outPathString): 
    write_string_to_txt_file(file_convert(inputPathString), outPathString)

#fullConvert("C:\\Users\\Lohann\\Desktop\\parmTest.s", "C:\\Users\\Lohann\\Desktop\\testResultHexa.txt")



fullConvert("C:\\Users\\Lohann\\Desktop\\parm\\test_integration\\branch.s", "C:\\Users\\Lohann\\Desktop\\parm\\test_integration\\branch.txt")



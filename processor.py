import sys
from codecs import decode
from traceback import print_tb, format_exception
"""
#############___Implemented___################
#    00 - End OF File                        #
#    01 - End Of Instruction                 #
#    02 - push                               #
#    03 - pop                                #
#    04 - print                              #
#    05 - add                                #
#    06 - substract                          #
#    07 - multipy                            #
#    08 - divide                             #
#    09 - shuffle                            #
#    10 - GOTO                               #
#    11 - IFEQUAL                            #
#    12 - modulus                            #
#    13 - INCrement                          #
#    14 - DECrement                          #
#    15 - Exponent                           #
#    16 - Store                              #
#    17 - Retrive                            #
#    18 - DELete                             #
#    19 - IFGREAT                            #
#    20 - IFNULL                             #
#    21 - IFPLUS                             #
#    22 - IFMINUS                            #
#    23 - IFUNEQUAL                          #
#    24 - IFEQUAL                            #
#    25 - IFSMALL                            #
#    26 - GOTO_L                             #
#    27 - IFGREAT(0)                         #
#    28 - IFNULL(0)                          #
#    29 - IFPLUS(0)                          #
#    30 - IFMINUS(0)                         #
#    31 - IFUNEQUAL(0)                       #
#    32 - IFEQUAL(0)                         #
#    33 - IFSMALL(0)                         #
#    34 - SADD                               #
#    35 - SCONV                              #
#    36 - POP_TOP                            #
#    37 - GOTO_CONDITIONALLY                 #
#    38 - GOTO_CONDITIONALLY_L               #
#    39 - LITERAL_PRINT                      #
#    40 - NOT                                #
#    41 - OR                                 #
#    42 - AND                                #
#    43 - REGISTER                           #
#    44 - UNREGISTER                         #
#    45 - GETREGISTER                        #
#    46 - FLOATCONV                          #
#    47 - INTCONV                            #
#    48 - DUPLICATE                          #
#    49 - ARCREATE                           #
#    50 - ARCREATE(1)                        #
#    51 - MEMDUMP                            #
#    52 - ARDISASSEMBLE                      #
#    53 - ARGET                              #
#    54 - ARSET                              #
#    55 - ARLEN                              #
#    56 - ARAPPEND(0)                        #
#    57 - ARAPPEND(1)                        #
#    58 - ARPOP(0)                           #
#    59 - ARLEN(0)                           #
#    60 - ARSET_TOP                          #
#    61 - ARINSERT_TOP                       #
#    62 - ARINSERT                           #
#    63 - INPUT                              #
#    64 - PUSH_NULL                          #
#    65 - SHUFFLE(1)                         #
#    66 - ARPOP(0)                           #
#    67 - ARPOP_TOP(1)                       #
#    68 - ARPOP_TOP(0)                       #
#    69 - PUSH_TRUE                          #
#    70 - PUSH_FALSE                         #
#    71 - XOR                                #
#    72 - ASSERT                             #
#    73 - NEGATE                             #
#    74 - IFSAME                             #
#    75 - IFSAME(0)                          #
#############___Unimplemented___##############
#                                            #
#                                            #
#                                            #
##############################################
"""
class main(object):
    def __init__(self, argv):
        self.memory = []
        self.storage = {}
        self.register = {}
        self.main(argv)

    def main(self, argv):
        bcode = self.load_program(argv[1])
        self.line_no = 0
        while(self.line_no<len(bcode)):
            instruction = self.load_instruction(bcode[self.line_no])
            try:
                self.execute_instruction(instruction)
            except Exception as error:
                print(''.join(format_exception(etype=type(error), value=error, tb=error.__traceback__)))
                sys.exit(65)
            self.line_no+=1

    def load_program(self, file):
        file = open(file)
        code = file.read()
        code = code.replace("\n", " ")
        code = code.split("01")
        file.close()
        for i, x in enumerate(code):
            while code[i].startswith(" "):
                code[i] = code[i][1:]
            while code[i].endswith(" "):
                code[i] = code[i][:-1]
        return code

    def load_instruction(self, instruction):
        instruction = instruction.split(" ")
        return instruction

    def execute_instruction(self, instruction):
        pointer = 0
        while (pointer<len(instruction)):
            if instruction[pointer] == '02':
                self.PUSH(instruction[pointer+1])
            elif instruction[pointer] == '03':
                try:
                    index_to_pop = instruction[pointer+1]
                except:
                    index_to_pop = hex(len(self.memory)-1)
                self.POP(index_to_pop)
            elif instruction[pointer] == '04':
                self.PRINT()
            elif instruction[pointer] == '05':
                self.ADD()
            elif instruction[pointer] == '06':
                self.SUB()
            elif instruction[pointer] == '07':
                self.MUL()
            elif instruction[pointer] == '08':
                self.DIV()
            elif instruction[pointer] == '09':
                self.SHUFFLE(instruction[pointer+1])
            elif instruction[pointer] == '10':
                self.GOTO()
            elif instruction[pointer] == '11':
                self.IFEQUAL()
            elif instruction[pointer] == '12':
                self.MODULUS()
            elif instruction[pointer] == '13':
                self.INC()
            elif instruction[pointer] == '14':
                self.DEC()
            elif instruction[pointer] == '15':
                self.EXPO()
            elif instruction[pointer] == '16':
                self.STORE(instruction[pointer+1])
            elif instruction[pointer] == '17':
                self.RETRIVE(instruction[pointer+1])
            elif instruction[pointer] == '18':
                self.DEL(instruction[pointer+1])
            elif instruction[pointer] == '19':
                self.IFGREAT()
            elif instruction[pointer] == '20':
                self.IFNULL()
            elif instruction[pointer] == '21':
                self.IFPLUS()
            elif instruction[pointer] == '22':
                self.IFMINUS()
            elif instruction[pointer] == '23':
                self.IFUNEQUAL()
            elif instruction[pointer] == '24':
                self.IFEQUAL()
            elif instruction[pointer] == '25':
                self.IFSMALL()
            elif instruction[pointer] == '26':
                self.GOTO_L()
            elif instruction[pointer] == '27':
                self.IFGREAT(call=0)
            elif instruction[pointer] == '28':
                self.IFNULL(call=0)
            elif instruction[pointer] == '29':
                self.IFPLUS(call=0)
            elif instruction[pointer] == '30':
                self.IFMINUS(call=0)
            elif instruction[pointer] == '31':
                self.IFUNEQUAL(call=0)
            elif instruction[pointer] == '32':
                self.IFEQUAL(call=0)
            elif instruction[pointer] == '33':
                self.IFSMALL(call=0)
            elif instruction[pointer] == '34':
                self.SADD()
            elif instruction[pointer] == '35':
                self.SCONV()
            elif instruction[pointer] == '36':
                self.POP_TOP(instruction[pointer+1])
            elif instruction[pointer] == '37':
                self.GOTO(condition=1)
            elif instruction[pointer] == '38':
                self.GOTO_L(condition=1)
            elif instruction[pointer] == '39':
                self.LITERAL_PRINT()
            elif instruction[pointer] == '40':
                self.NOT()
            elif instruction[pointer] == '41':
                self.OR()
            elif instruction[pointer] == '42':
                self.AND()
            elif instruction[pointer] == '43':
                self.REGISTER(instruction[pointer+1])
            elif instruction[pointer] == '44':
                self.UNREGISTER(instruction[pointer+1])
            elif instruction[pointer] == '45':
                self.GETREGISTER(instruction[pointer+1])
            elif instruction[pointer] == '46':
                self.FLOATCONV()
            elif instruction[pointer] == '47':
                self.INTCONV()
            elif instruction[pointer] == '48':
                self.DUPLICATE()
            elif instruction[pointer] == '49':
                self.ARCREATE()
            elif instruction[pointer] == '50':
                self.ARCREATE(mode=1)
            elif instruction[pointer] == '51':
                self.MEMDUMP()
            elif instruction[pointer] == '52':
                self.ARDISASSEMBLE()
            elif instruction[pointer] == '53':
                self.ARGET(instruction[pointer+1])
            elif instruction[pointer] == '54':
                self.ARSET(instruction[pointer+1])
            elif instruction[pointer] == '55':
                self.ARLEN()
            elif instruction[pointer] == '56':
                self.ARAPPEND(pos=0)
            elif instruction[pointer] == '57':
                self.ARAPPEND(pos=1)
            elif instruction[pointer] == '58':
                self.ARPOP(pos=1)
            elif instruction[pointer] == '59':
                self.ARLEN(call=0)
            elif instruction[pointer] == '60':
                self.ARSET_TOP(instruction[pointer+1])
            elif instruction[pointer] == '61':
                self.ARINSERT_TOP(instruction[pointer+1])
            elif instruction[pointer] == '62':
                self.ARINSERT(instruction[pointer+1])
            elif instruction[pointer] == '63':
                self.INPUT()
            elif instruction[pointer] == '64':
                self.PUSH_NULL()
            elif instruction[pointer] == '65':
                self.SHUFFLE(instruction[pointer+1], call=1)
            elif instruction[pointer] == '66':
                self.ARPOP(pos=0)
            elif instruction[pointer] == '67':
                self.ARPOP_TOP(pos=1)
            elif instruction[pointer] == '68':
                self.ARPOP_TOP(pos=0)
            elif instruction[pointer] == '69':
                self.PUSH_TRUE()
            elif instruction[pointer] == '70':
                self.PUSH_FALSE()
            elif instruction[pointer] == '71':
                self.XOR()
            elif instruction[pointer] == '72':
                self.ASSERT()
            elif instruction[pointer] == '73':
                self.NEGATE()
            elif instruction[pointer] == '74':
                self.IFSAME()
            elif instruction[pointer] == '75':
                self.IFSAME(call=0)
            elif instruction[pointer] == '00':
                sys.exit(0)
            pointer += 1

    def get_string(self, value):
        value = value[1:]
        value = value[:-1]
        value = value[2:]
        value = bytearray.fromhex(value).decode()
        return value

    def PUSH(self, value):
        if value.startswith("{") and value.endswith("}"):
            self.memory.append(self.get_string(value))
        else:
            self.memory.append(int(value, 16))

    def PUSH_NULL(self):
        self.memory.append(None)

    def PUSH_TRUE(self):
        self.memory.append(True)

    def PUSH_FALSE(self):
        self.memory.append(False)

    def INPUT(self):
        displayed = self.memory[len(self.memory)-1]
        if displayed is None:
            displayed = ""
        given = input(str(displayed))
        self.memory.append(given)

    def DUPLICATE(self):
        mem = self.memory[len(self.memory)-1]
        self.memory.append(mem)

    def MEMDUMP(self):
        print(self.memory)

    def ARCREATE(self, mode=0):
        array_len = self.memory.pop()
        array = self.memory[array_len*-1:]
        if mode:
            self.memory = self.memory[0:len(self.memory)-array_len]
        self.memory.append(array)

    def ARGET(self, mode="0x0"):
        mode = int(mode, 16)
        list_place = self.memory.pop()
        reference = self.memory[len(self.memory)-1]
        reference = self.memory[len(self.memory) - list_place][reference] if mode else self.memory[list_place][reference]
        self.memory.append(reference)

    def ARSET(self, mode="0x0"):
        mode = int(mode, 16)
        list_place = self.memory.pop()
        value = self.memory[len(self.memory)-1]
        reference = self.memory.pop(len(self.memory)-2) if mode else self.memory[len(self.memory)-2]
        self.memory[list_place][reference] = value

    def ARINSERT(self, mode="0x0"):
        mode = int(mode, 16)
        list_place = self.memory.pop()
        value = self.memory[len(self.memory)-1]
        reference = self.memory.pop(len(self.memory)-2) if mode else self.memory[len(self.memory)-2]
        self.memory[list_place].insert(reference, value)

    def ARINSERT_TOP(self, mode="0x0"):
        mode = int(mode, 16)
        list_place = self.memory.pop()
        value = self.memory[len(self.memory)-1]
        reference = self.memory.pop(len(self.memory)-2) if mode else self.memory[len(self.memory)-2]
        self.memory[len(self.memory)-list_place].insert(reference, value)

    def ARSET_TOP(self, mode="0x0"):
        mode = int(mode, 16)
        list_place = self.memory.pop()
        value = self.memory[len(self.memory)-1]
        reference = self.memory.pop(len(self.memory)-2) if mode else self.memory[len(self.memory)-2]
        self.memory[len(self.memory)-list_place][reference] = value

    def ARLEN(self, call=1):
        list_place = self.memory.pop()
        if call:
            list_place = self.memory[len(self.memory) - list_place]
        else:
            list_place = self.memory[list_place]
        length = len(list_place)-1
        self.memory.append(length)

    def ARAPPEND(self, pos=0):
        list_place = self.memory.pop()
        list_place = self.memory[list_place] if pos else self.memory[len(self.memory) - list_place]
        list_place.append(self.memory[len(self.memory)-1])

    def ARPOP(self, pos=0):
        list_place = self.memory.pop()
        list_place = self.memory[list_place] if pos else self.memory[len(self.memory) - list_place]
        list_place.pop(self.memory[len(self.memory)-1])

    def ARPOP_TOP(self, pos=0):
        list_place = self.memory.pop()
        list_place = self.memory[list_place] if pos else self.memory[len(self.memory) - list_place]
        list_place.pop()

    def ARDISASSEMBLE(self, mode=0):
        array_len = self.memory.pop()
        for val in array_len:
            self.memory.append(val)

    def STORE(self, key):
        value = self.memory[len(self.memory)-1]
        self.memory.pop()
        key = int(key, 16)
        self.storage[key] = value

    def RETRIVE(self, key):
        key = int(key, 16)
        self.memory.append(self.storage[key])

    def DEL(self, key):
        key = int(key, 16)
        del self.storage[key]

    def POP(self, index):
        self.memory.pop(int(index, 16))

    def POP_TOP(self, index):
        index = int(index, 16)
        index = len(self.memory) - index
        self.memory.pop(index)

    def SCONV(self):
        to_append = str(self.memory[len(self.memory)-1])
        self.memory.pop()
        self.memory.append(to_append)

    def FLOATCONV(self):
        to_append = float(self.memory[len(self.memory)-1])
        self.memory.pop()
        self.memory.append(to_append)

    def INTCONV(self):
        to_append = int(self.memory[len(self.memory)-1])
        self.memory.pop()
        self.memory.append(to_append)

    def REGISTER(self, key):
        key = self.get_string(key)
        value =  self.memory.pop()
        self.register[key] = value

    def UNREGISTER(self, key):
        key = self.get_string(key)
        del self.register[key]

    def GETREGISTER(self, key):
        key = self.get_string(key)
        self.memory.append(self.register[key])

    def PRINT(self):
        sys.stdout.write(str(self.memory[len(self.memory)-1]))

    def LITERAL_PRINT(self):
        decoded = decode(self.memory[len(self.memory)-1], "unicode_escape")
        sys.stdout.write(decoded)

    def ADD(self):
        results = self.memory[len(self.memory)-1] + self.memory[len(self.memory)-2]
        self.memory.append(results)

    def SADD(self):
        self.memory[len(self.memory)-1] = str(self.memory[len(self.memory)-1])
        self.memory[len(self.memory)-2] = str(self.memory[len(self.memory)-2])
        results = self.memory[len(self.memory)-1] + self.memory[len(self.memory)-2]
        self.memory.append(results)

    def SUB(self):
        results = self.memory[len(self.memory)-1] - self.memory[len(self.memory)-2]
        self.memory.append(results)

    def MUL(self):
        results = self.memory[len(self.memory)-1] * self.memory[len(self.memory)-2]
        self.memory.append(results)

    def DIV(self):
        try:
            results = self.memory[len(self.memory)-1] / self.memory[len(self.memory)-2]
        except ZeroDivisionError:
            raise ZeroDivisionError("You are dividing by zero on instruction number " + str(self.line_no))
        self.memory.append(results)

    def NEGATE(self):
        self.memory[len(self.memory)-1] = self.memory[len(self.memory)-2] * -1

    def MODULUS(self):
        try:
            results = self.memory[len(self.memory)-1] % self.memory[len(self.memory)-2]
        except ZeroDivisionError:
            raise ZeroDivisionError("You are dividing by zero on instruction number " + str(self.line_no))
        self.memory.append(results)

    def EXPO(self):
        results = self.memory[len(self.memory)-1] ** self.memory[len(self.memory)-2]
        self.memory.append(results)

    def SHUFFLE(self, index, call=0):
        given = self.memory[int(index, 16)] if call else self.memory[len(self.memory) - int(index, 16)]
        stack_top = self.memory[len(self.memory)-1]
        if call:
            self.memory[int(index, 16)] = stack_top
        else:
            self.memory[len(self.memory) - int(index, 16)] = stack_top
        self.memory[len(self.memory)-1] = given

    def INC(self):
        self.memory[len(self.memory)-1] = self.memory[len(self.memory)-1] + 1

    def DEC(self):
        self.memory[len(self.memory)-1] = self.memory[len(self.memory)-1] - 1

    def ASSERT(self):
        assertion = self.memory.pop()
        assert assertion

    def IFEQUAL(self, call=1):
        first = self.memory.pop() if call else self.memory[len(self.memory)-1]
        second = self.memory.pop() if call else self.memory[len(self.memory)-2]
        self.memory.append(first == second)

    def IFSAME(self, call=1):
        first = self.memory.pop() if call else self.memory[len(self.memory)-1]
        second = self.memory.pop() if call else self.memory[len(self.memory)-2]
        self.memory.append(first is second)

    def IFGREAT(self, call=1):
        first = self.memory.pop() if call else self.memory[len(self.memory)-1]
        second = self.memory.pop() if call else self.memory[len(self.memory)-2]
        self.memory.append(first > second)

    def IFSMALL(self, call=1):
        first = self.memory.pop() if call else self.memory[len(self.memory)-1]
        second = self.memory.pop() if call else self.memory[len(self.memory)-2]
        self.memory.append(first < second)

    def IFNULL(self, call=1):
        mayNull = self.memory.pop() if call else self.memory[len(self.memory)-1]
        self.memory.append(bool(mayNull))

    def IFPLUS(self, call=1):
        value = self.memory.pop() if call else self.memory[len(self.memory)-1]
        self.memory.append(value > 0)

    def IFMINUS(self, call=1):
        value = self.memory.pop() if call else self.memory[len(self.memory)-1]
        self.memory.append(value < 0)

    def IFUNEQUAL(self, call=1):
        first = self.memory.pop() if call else self.memory[len(self.memory)-1]
        second = self.memory.pop() if call else self.memory[len(self.memory)-2]
        self.memory.append(first != second)

    def NOT(self):
        self.memory[len(self.memory)-1] = not(self.memory[len(self.memory)-1])

    def OR(self):
        a = self.memory.pop()
        b = self.memory.pop()
        self.memory.append(a or b)

    def XOR(self):
        a = self.memory.pop()
        b = self.memory.pop()
        self.memory.append(((a and not b) or (not a and b)))

    def AND(self):
        a = self.memory.pop()
        b = self.memory.pop()
        self.memory.append(a and b)

    def GOTO(self, condition=0):
        line_no = self.memory.pop()
        found_condition = self.memory.pop()
        if (condition == 1) and found_condition:  
            self.line_no = line_no - 1
        elif condition == 0:
            self.line_no = line_no - 1

# GOTO_L needs some rework
    def GOTO_L(self, condition=0):
        line_no = self.memory[len(self.memory)-1]
        found_condition = self.memory.pop(len(self.memory)-2)
        if (condition == 1) and found_condition:
            self.line_no = line_no - 1
        elif condition == 0:
            self.line_no = line_no - 1

    def target(*args):
        return main, None

if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise Exception("No file path provided.")
    main(sys.argv)

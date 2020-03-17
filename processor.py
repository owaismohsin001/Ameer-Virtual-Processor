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
#    58 - ARPOP(1)                           #
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
#    76 - Split                              #
#    77 - JOIN                               #
#    78 - StrINSERT                          #
#    79 - RECORD                             #
#    80 - RECAP                              #
#    81 - FRAMEDUMP                          #
#    82 - RECORDHEAP                         #
#    83 - RECAPHEAP                          #
#    84 - HEAPDUMP                           #
#    85 - PUSH_LAST                          #
#    86 - SETUP_EXCEPT                       #
#    87 - END_EXCEPT                         #
#    88 - IFEXCEPTION                        #
#    89 - LISTCONV                           #
#############___Unimplemented___##############
#                                            #
#                                            #
#                                            #
##############################################
"""
class Frame(object):
    def __init__(self):
        self.Frame = {}
        self.callStack = []
        self.last_frame =  ''

    def __setitem__(self, key, value):
        self.__set_last_frame()
        self.callStack.append(key)
        self.Frame[key] = value

    def last(self):
        return self.last_frame

    def __set_last_frame(self):
        self.last_frame =  '' if self.callStack == [] else self.callStack[-1]

    def __remove_callStack(self):
        if self.callStack != []:
            self.callStack.pop()
            self.__set_last_frame()

    def __getitem__(self, key):
        self.__remove_callStack()
        return self.Frame[key]

class Memory:
    def __init__(self):
        self.memory = []

    def __getitem__(self, key):
        return self.memory[key]

    def __setitem__(self, key, value):
        self.memory[key] = value

    def __delitem__(self, key):
        del self.memory[key]

    def __len__(self):
        return len(self.memory)

    def __iter__(self):
        return iter(self.memory)

    def __repr__(self):
        return f"{self.memory}"

    def pop(self, *args):
        return self.memory.pop(*args)

    def append(self, *args):
        self.memory.append(*args)

class main(object):
    def __init__(self, argv):
        self.memory = Memory()
        self.storage = {}
        self.register = {}
        self.memory_frame = Frame()
        self.heap_frame = Frame()
        self.exception_handler = False
        self.exceptions = []
        self.opcodes = {
            "02": lambda x: self.PUSH(*x),
            "03": lambda x: self.POP(*x),
            "04": lambda x: self.PRINT(),
            "05": lambda x: self.ADD(),
            "06": lambda x: self.SUB(),
            "07": lambda x: self.MUL(),
            "08": lambda x: self.DIV(),
            "09": lambda x: self.SHUFFLE(),
            "10": lambda x: self.GOTO(),
            "11": lambda x: self.IFEQUAL(),
            "12": lambda x: self.MODULUS(),
            "13": lambda x: self.INC(),
            "14": lambda x: self.DEC(),
            "15": lambda x: self.EXPO(),
            "16": lambda x: self.STORE(),
            "17": lambda x: self.RETRIVE(),
            "18": lambda x: self.DEL(),
            "19": lambda x: self.IFGREAT(),
            "20": lambda x: self.IFNULL(),
            "21": lambda x: self.IFPLUS(),
            "22": lambda x: self.IFMINUS(),
            "23": lambda x: self.IFUNEQUAL(),
            "24": lambda x: self.IFEQUAL(),
            "25": lambda x: self.IFSMALL(),
            "26": lambda x: self.GOTO_L(),
            "27": lambda x: self.IFGREAT(0),
            "28": lambda x: self.IFNULL(0),
            "29": lambda x: self.IFPLUS(0),
            "30": lambda x: self.IFMINUS(0),
            "31": lambda x: self.IFUNEQUAL(0),
            "32": lambda x: self.IFEQUAL(0),
            "33": lambda x: self.IFSMALL(0),
            "34": lambda x: self.SADD(),
            "35": lambda x: self.SCONV(),
            "36": lambda x: self.POP_TOP(*x),
            "37": lambda x: self.GOTO(condition=1),
            "38": lambda x: self.GOTO_L(condition=1),
            "39": lambda x: self.LITERAL_PRINT(),
            "40": lambda x: self.NOT(),
            "41": lambda x: self.OR(),
            "42": lambda x: self.AND(),
            "43": lambda x: self.REGISTER(*x),
            "44": lambda x: self.UNREGISTER(*x),
            "45": lambda x: self.GETREGISTER(*x),
            "46": lambda x: self.FLOATCONV(),
            "47": lambda x: self.INTCONV(),
            "48": lambda x: self.DUPLICATE(),
            "49": lambda x: self.ARCREATE(),
            "50": lambda x: self.ARCREATE(1),
            "51": lambda x: self.MEMDUMP(),
            "52": lambda x: self.ARDISASSEMBLE(),
            "53": lambda x: self.ARGET(*x),
            "54": lambda x: self.ARSET(*x),
            "55": lambda x: self.ARLEN(),
            "56": lambda x: self.ARAPPEND(0),
            "57": lambda x: self.ARAPPEND(1),
            "58": lambda x: self.ARPOP(1),
            "59": lambda x: self.ARLEN(0),
            "60": lambda x: self.ARSET_TOP(*x),
            "61": lambda x: self.ARINSERT_TOP(*x),
            "62": lambda x: self.ARINSERT(*x),
            "63": lambda x: self.INPUT(),
            "64": lambda x: self.PUSH_NULL(),
            "65": lambda x: self.SHUFFLE(1),
            "66": lambda x: self.ARPOP(0),
            "67": lambda x: self.ARPOP_TOP(1),
            "68": lambda x: self.ARPOP_TOP(0),
            "69": lambda x: self.PUSH_TRUE(),
            "70": lambda x: self.PUSH_FALSE(),
            "71": lambda x: self.XOR(),
            "72": lambda x: self.ASSERT(),
            "73": lambda x: self.NEGATE(),
            "74": lambda x: self.IFSAME(),
            "75": lambda x: self.IFSAME(0),
            "76": lambda x: self.Split(),
            "77": lambda x: self.JOIN(),
            "78": lambda x: self.StrINSERT(),
            "79": lambda x: self.RECORD(*x),
            "80": lambda x: self.RECAP(*x),
            "81": lambda x: self.FRAMEDUMP,
            "82": lambda x: self.RECORDHEAP(*x),
            "83": lambda x: self.RECAPHEAP(*x),
            "84": lambda x: self.HEAPDUMP(*x),
            "85": lambda x: self.PUSH_LAST(*x),
            "86": lambda x: self.SETUP_EXCEPT(),
            "87": lambda x: self.END_EXCEPT(),
            "88": lambda x: self.IFEXCEPTION(*x),
            "89": lambda x: self.LISTCONV()
        }
        self.main(argv)

    def main(self, argv):
        bcode = self.load_program(argv[1])
        self.line_no = 0
        while(self.line_no<len(bcode)):
            instruction = self.load_instruction(bcode[self.line_no])
            if instruction != [""]:
                try:
                    self.execute_instruction(instruction)
                except Exception as error:
                    if self.exception_handler:
                        self.exceptions.append(error)
                        self.exception_handler = False
                    else:
                        print(''.join(format_exception(etype=type(error), value=error, tb=error.__traceback__)), f"\nOccured at instruction number {self.line_no}")
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
        code = [i for i in instruction if i!='']
        return instruction

    def execute_instruction(self, instruction):
        pointer = 0
        while (pointer<len(instruction)):
            if instruction[pointer].startswith("{0x") or instruction[pointer].startswith("0x"):
                pointer+=1
            elif instruction[pointer] == '00':
                sys.exit(0)
            elif instruction[pointer] == '03':
                try:
                    index_to_pop = instruction[pointer+1]
                except:
                    index_to_pop = hex(len(self.memory)-1)
                    self.opcodes[instruction[pointer]]([index_to_pop])
                    pointer += 1
            elif len(instruction)-1 == pointer:
                    self.opcodes[instruction[pointer]]([])
            else:
                self.opcodes[instruction[pointer]]([instruction[pointer+1]])
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

    def SETUP_EXCEPT(self):
        self.exception_handler = True

    def END_EXCEPT(self):
        self.exception_handler = False

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

    def PUSH_LAST(self, mode=0):
        last = self.heap_frame.last() if mode else self.memory_frame.last()
        self.memory.append(last)

    def RECORD(self):
        key = self.memory.pop()
        self.memory_frame[key] = self.memory
        self.memory = []

    def RECORDHEAP(self, call=0):
        key = self.memory.pop()
        self.heap_frame[key] = self.register if call else self.storage
        if call:
            self.register = {}
        else:
            self.storage = {}

    def RECAP(self):
        key = self.memory.pop()
        self.memory = self.memory_frame[key]
        del self.memory_frame[key]

    def RECAPHEAP(self, call=0):
        key = self.memory.pop()
        if call:
            self.register = self.heap_frame[key]
        else:
            self.storage = self.heap_frame[key]
        del self.heap_frame[key]

    def FRAMEDUMP(self):
        print(self.memory_frame.Frame)

    def DUMPHEAP(self):
        print(self.heap_frame.Frame)

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

    def LISTCONV(self):
        to_append = list(self.memory[len(self.memory)-1])
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

    def SPLIT(self):
        splitter = self.memory.pop()
        self.memory[len(self.memory)-1] = self.memory[len(self.memory)-1].split(splitter)

    def JOIN(self):
        joiner = self.memory.pop()
        self.memory[len(self.memory)-1] = joiner.join(self.memory[len(self.memory)-1])

    def StrINSERT(self):
        insertion = self.memory.pop()
        self.memory[len(self.memory)-1] = self.memory[len(self.memory)-1].format(insertion)

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
        self.memory[len(self.memory)-1] = self.memory[len(self.memory)-1] * -1

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

    def IFEXCEPTION(self, given_type):
        exception = self.exceptions.pop() if self.exceptions != [] else self.exceptions
        given_type = self.get_string(given_type)
        self.memory.append(type(exception).__name__ == given_type)

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
        found_condition = self.memory.pop() if condition else True
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

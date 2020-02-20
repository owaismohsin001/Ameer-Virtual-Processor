# Ameer Virtual Processor
This is virtual machine named Ameer Virtual Processor to which languages can be compiled to, and be ran on.
## Environment
It can be ran on any python environment but for the sake of let's say performance, it should be ran with either an AOT Compiler like Nuitka or a JIT Compiler like PyPy which this virtual machine can be compiled to.
## Supported type of instructions
This VM is intended to be used for dynamic languages and so it's made dynamic in it's very nature. This currently supports variables in a heap and a string heap, arrays and strings. We hope to add built in functions in this very soon and to expand on our support of arrays and strings.
## Instruction Chart
What follows is a (hopefully) comprehensive description of each instruction that is currently avaliable in this virtual machine.

**00 - End OF File |** This instruction is used to tell the program that the file is ended before it does or for cleanliness of code. 

**01 - End Of Instruction |** This code is used to end every instruction.

**02 - push |** PUSH to the top of the stack.

**03 - pop  |** Pop either top or a certain index from the stack.

**04 - print |** Used to print the top of the sack.

**05 - add |** Add two numbers at the top of the stack.

**06 - substract |** Substract two numbers at the top of the stack.

**07 - multipy |** Multiply two numbers at the top of the stack.

**08 - divide |** Divide two numbers at the top of the stack

**09 - shuffle |** Shuffle two elements from the stack, takes an argument as to what stack number should the first stack be shuffled with.

**10 - GOTO |** Unconditional GOTO and it pops the line number of the stack.

**11 - IFEQUAL |** Add either True or False on the stack depending on if first and second values on the stack are equal and pops conditions.

**12 - modulus |** Modulus of first two values from stack and append the result onto it.

**13 - INCrement |** Increment the last number from the stack.

**14 - DECrement |** Decrement the last number from the stack.

**15 - Exponent |** Exponent of first two values from stack and append the result onto it.   

**16 - Store |** Store the first element from the stack in a heap of numbered name, numbered according to the given in the instruction.

**17 - Retrive |** Retrive and append from the storage onto the stack.

**18 - DELete |** Delete an item from storage.

**19 - IFGREAT |** Adds either True or False on the stack depending on if first is greater than the and second value on the stack and pops conditions.

**20 - IFNULL |** Adds either True or False on the stack depending on if the first value on the stack is null and pops conditions.

**21 - IFPLUS |** Adds either True or False on the stack depending on if the first value on the stack is positive and pops conditions.

**22 - IFMINUS |** Adds either True or False on the stack depending on if the first value on the stack is negative and pops conditions.

**23 - IFUNEQUAL |** Adds either True or False on the stack depending on if first is unequal to the second value on the stack and pops conditions.

**24 - IFEQUAL |** Adds either True or False on the stack depending on if first is equal to the second value on the stack and pops conditions. 

**25 - IFSMALL |** Adds either True or False on the stack depending on if first is unequal to the second value on the stack and pops conditions.

**26 - GOTO_L |** GOTO without popping line number from stack.

**27 - IFGREAT(0) |** Adds either True or False on the stack depending on if first is greater than the and second value on the stack.

**28 - IFNULL(0) |** Adds either True or False on the stack depending on if the first value on the stack is null.

**29 - IFPLUS(0) |** Adds either True or False on the stack depending on if the first value on the stack is positive.

**30 - IFMINUS(0) |** Adds either True or False on the stack depending on if the first value on the stack is negative.

**31 - IFUNEQUAL(0) |** Adds either True or False on the stack depending on if first is unequal to the second value on the stack.   

**32 - IFEQUAL(0) |** Adds either True or False on the stack depending on if first is equal to the second value on the stack.

**33 - IFSMALL(0) |** Adds either True or False on the stack depending on if first is unequal to the second value on the stack.

**34 - SADD |** Concatenates first two elements of the stack and appends them.

**35 - SCONV |** Converts the first element of the stack to a string.  

**36 - POP_TOP |** Pops the first elememnts from the stack depending on the indx you provide.    

**37 - GOTO_CONDITIONALLY |** Conditionally GOTO a line number depending on the first value on the stack and if it's True or False.

**38 - GOTO_CONDITIONALLY_L |** Conditionally GOTO a line number depending on the first value on the stack and if it's True or False and don't pop conditions off the stack.

**39 - LITERAL_PRINT |** Print stuff with literals. 

**40 - NOT |** Inverts the first condition on the stack.

**41 - OR |** OR operation on the first condition on the stack. 

**42 - AND |** AND operation on the first condition on the stack.

**43 - REGISTER |** Adds first element of the stack to this register with a string name.

**44 - UNREGISTER |** Removes the given element from the register.

**45 - GETREGISTER |** Add the given element from the register to the top of the stack.

**46 - FLOATCONV |** Converts the first element of the stack to a float. 

**47 - INTCONV |** Converts the first element of the stack to a integer.  

**48 - DUPLICATE |** Duplicate the first value of the stack.

**49 - ARCREATE |** Creates an array with the array length on the top of the stack and append it onto the stack.

**50 - ARCREATE(1) |** Creates an array with the array length on the top of the stack and append it onto the stack and removes those from the stack.

**51 - MEMDUMP |** Print entire stack.

**52 - ARDISASSEMBLE |** Disassemble the array on the top of the stack.      

**53 - ARGET |** Get list's place from the top of the stack and them gets the reference from the stack. Either from the top or bottom depending on it's mode.

**54 - ARSET |** Sets an array the same way it get's it. 

**55 - ARLEN |** Get the length of the array from the given index.

**56 - ARAPPEND(0) |** Appends the memory on a certain index from top.

**57 - ARAPPEND(1) |** Appends the memory on a certain index from bottom.   

**58 - ARPOP(1) |** Pops array on a certain list's place counted from bottom.

**59 - ARLEN(0) |** Length of an array from bottom.

**60 - ARSET_TOP |** Set an array from top index.

**61 - ARINSERT_TOP |** Insert into an array from top index.

**62 - ARINSERT |** Insert into an array from bottom index.

**63 - INPUT |** With this insruction you can input anything in a string form.

**64 - PUSH_NONE |** With this insruction you can push none on to the stack.

**65 - SHUFFLE(1) |** Shuffles the first item in the stack with another one given in the instruction itself, counted from bottom.

**66 - ARPOP(0) |** Pops array on a certain list's place counted from top.

**67 - ARPOP_TOP(1) |** Pops array's top index on a certain list's place counted from top.

**68 - ARPOP_TOP(0) |** Pops array's top index on a certain list's place counted from bottom.

**69 - PUSH_TRUE |** Pushes a true value onto the stack.

**70 - PUSH_FALSE |** Pushes a false value onto the stack.

**71 - XOR |** XOR gate that checks for first two value of the stack and pops them of it.

Hey, btw, assembly for these instructions will be created as soon as I am satisfied with instruction themselves.

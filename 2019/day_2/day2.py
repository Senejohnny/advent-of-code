""" day 2 of advent of code 2019 """
with open('input_day2.txt') as file:
    memory =[int(_) for _ in file.read().split(',')]

def alarm(_memory): # pylint: disable=
    """ returns first adress in memory with opcode 99 """
    mem = _memory.copy()
    i = 0
    while True:
        if mem[i] == 99:
            return mem[0]
        if mem[i] == 1:
            mem[mem[i + 3]] = mem[mem[i + 1]] + mem[mem[i + 2]]
        else:
            mem[mem[i + 3]] = mem[mem[i + 1]] * mem[mem[i + 2]]
        i += 4

def memory_setter(noun, verb, _memory):
    """ memory setter """
    temp_mem = _memory.copy()
    temp_mem[1], temp_mem[2] = noun, verb
    return temp_mem

def get_answer_part2(original_memory):    # pylint: disable=inconsistent-return-statements 
    """ answer to part 2 """
    for noun in range(0, 99):
        for verb in range(0, 99):
            _memory = memory_setter(noun, verb, original_memory)
            if alarm(_memory) == 19690720:
                return 100 * noun + verb

# Part 1
tem_mem = memory_setter(12, 2, memory)
print(alarm(tem_mem))
# Part 2
print(get_answer_part2(memory))

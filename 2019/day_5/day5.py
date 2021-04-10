with open('2019/day_5/input_day5.txt') as file:
    memory =[int(_) for _ in file.read().split(',')]

mode = {
        '0' : lambda x, i: x[i],  # position mode
        '1' : lambda x, i: i     # immediate mode
}

def diagnostic_code(memory, _input):
    mem = memory.copy()
    output = []
    i = 0
    while True:
        inst = str(mem[i]).zfill(5)
        A, B, C, _, opcode = inst
        if opcode == '9':
            return output
        elif opcode == '1':
            mem[mode[A](mem, i + 3)] = mem[mode[C](mem, i + 1)] + mem[mode[B](mem, i + 2)]
            i += 4
        elif opcode == '2':
            mem[mode[A](mem, i + 3)] = mem[mode[C](mem, i + 1)] * mem[mode[B](mem, i + 2)]
            i += 4
        elif opcode == '3':
            mem[mode[C](mem, i + 1)] = _input
            i += 2
        elif opcode == '4':
            output.append(mem[mode[C](mem, i + 1)])
            i += 2
        elif opcode == '5':
            if mem[mode[C](mem, i + 1)]:
                i =  mem[mode[B](mem, i + 2)]
            else:
                i += 3
        elif opcode == '6':
            if not mem[mode[C](mem, i + 1)]:
                i =  mem[mode[B](mem, i + 2)]
            else:
                i += 3
        elif opcode == '7':
            if mem[mode[C](mem, i + 1)] < mem[mode[B](mem, i + 2)]:
                mem[mode[A](mem, i + 3)] = 1
            else:
                mem[mode[A](mem, i + 3)] =  0
            i += 4
        elif opcode == '8':
            if mem[mode[C](mem, i + 1)] == mem[mode[B](mem, i + 2)]:
                mem[mode[A](mem, i + 3)] = 1
            else:
                mem[mode[A](mem, i + 3)] =  0
            i += 4
        else:
            raise IndexError(f'Index {i} unacceptable')

# Part 1
print(diagnostic_code(memory, 1))
# Part 2
print(diagnostic_code(memory, 5))
# Hi, This is a code for adventofcode website competition day 5
with open('5.txt') as f:
    List = f.readlines()
    index = int(List[0])
    print(index)
    List[0] = index + 1
    i = 1
    current_position = 0
    while 0 <= index + current_position <= len(List)-1:
        a = int(List[index + current_position])
        List[index + current_position] = a + 1
        current_position = index + current_position   # this is the current position
        index = a
        i += 1
        print(i)
    # step = 0
    # while 0 <= step <= len(List)-1:
    #     a = int(List[step])
    #     List[step] = a + 1            this was even a better solution
    #     step = step + a
    #     i += 1
    #     print(i)
    #     # print('---------------')
print('Number of steps =', i)
print("  Name of the file: ", f.name)

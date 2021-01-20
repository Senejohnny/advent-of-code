# Hi, This is a code for adventofcode website competition day 5
with open('5.txt') as f:
    List = f.readlines()
    print(len(List))
    index = int(List[0])
    print('index =', index)
    List[0] = index + 1
    i = 1
    current_position = 0
    while 0 <= index + current_position <= len(List)-1:
        a = int(List[index + current_position])
        if a >= 3:
            List[index + current_position] = a - 1
        else:
            List[index + current_position] = a + 1
        current_position = index + current_position   # this is the current position
        index = a
        i += 1
        # print(i)
print('Number of steps =', i)
print("  Name of the file: ", f.name)

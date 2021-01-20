# Hi, This is a code for adventofcode website competition day 1
with open('2.txt') as f:
    i = 0
    for line in f:
        for i in range(len(line)):
            if line.count(i) == 2:
                print("Yes")

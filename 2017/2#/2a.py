# Hi, This is a code for adventofcode website competition day 1
with open('2.txt') as f:
    i = 0
    Sum = 0
    for line in f:
        i += 1
        A = [int(s) for s in line.split() if s.isdigit()]
        Sum = Sum + max(A)-min(A)
        print('Line(%d)   ' % i, A)
print(Sum)
print("  Name of the file: ", f.name)

# Hi, This is a code for adventofcode website competition day 1
with open('2.txt') as f:
    i = 0
    Sum = 0
    for line in f:
        i += 1
        A = [int(s) for s in line.split() if s.isdigit()]
        for j in range(len(A)):
            for k in range(len(A)):
                if k != j:
                    devide = A[j] % A[k]
                    if devide == 0:
                        value = A[j] / A[k]
                        print(value)
                        Sum = Sum + value
    # print('Line(%d)  ' % i, A)
print('Final Answer is =  ', int(Sum))
print("  Name of the file: ", f.name)

with open('4.txt') as f:
    i = 0
    Sum = 0
    for line in f:
        i += 1
        A = [s for s in line.split()]
        count = 0
        print('Line(%d)  ' % i, A)
        for j in range(len(A)):
            for k in range(len(A)):
                if k != j:
                    list1 = list(A[j])
                    list2 = list(A[k])
                    if len(list1) != len(list2):
                        count += 1
                    else:
                        list1.sort()
                        list2.sort()
                        if list1 != list2:
                            count += 1
                        print(count)
        if count == len(A)*(len(A)-1):
            Sum += 1
            print('Current Sum value is = ', Sum)
print("  Name of the file: ", f.name)
print('Final Answer is =  ', int(Sum))


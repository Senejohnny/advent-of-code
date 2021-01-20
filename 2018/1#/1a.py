# Hi, This is a code for adventofcode website competition day 1
f = open("1.txt", "r")
L = f.read()
LL = L.split()
print(LL)
# Sum = 0
# for i in range(len(LL)):
#     Sum = Sum + int(LL[i])
#     print(i, Sum)

Sum = 0
Memory = [Sum]
i = 0
while 1 > 0:
    Sum = Sum + int(LL[i])
    if Sum in Memory:
        print("Yes", Sum, "found in memory")
        break
    Memory.append(Sum)
    # print(Memory)
    i += 1
    if i > len(LL)-1:
        i = 0

# Sum = 0
# Memory = [Sum]
#     for j in range(3):
#         for i in range(len(LL)):
#             Sum = Sum + int(LL[i])
#             if Sum not in Memory:
#                 Memory.append(Sum)
#                 print(Memory)
#             else:
#                 print("Yes", Sum, "found in memory")
#         #             break
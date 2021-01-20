# Hi, This is a code for adventofcode website competition day 1
f = open("1.txt", "r")
L = f.read()
print(len(L))
print(type(L))
print(L)
# Sum = 0
# for i in range(len(L)-1):
#     if L[i] == L[i+1]:
#         Sum = Sum + int(L[i])
#         print(Sum, i)
#
# if L[0] == L[-1]:
#     print(Sum + int(L[0]))

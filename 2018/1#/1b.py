# Hi, This is a code for adventofcode website competition day 1
f = open("1.txt", "r")
L = f.read()
print(len(L))
print(type(L))
print(L)
step = int(int(len(L)) / 2)
Sum = 0
for i in range(len(L)):
    if L[i] == L[(i + step) % int(len(L))]:
        Sum = Sum + int(L[i])
        print(Sum, i)

# if L[0] == L[-1]:
#     k = Sum + int(L[0])
# print(k)

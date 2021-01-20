# def spiral(N, M):
#     x, y = 0, 0
#     dx, dy = 0, -1
#
#     for dumb in range(N*M):
#         if abs(x) == abs(y) and [dx, dy] != [1, 0] or x > 0 and y == 1-x:
#             dx, dy = -dy, dx            # corner, change direction
#
#         if abs(x) > N/2 or abs(y) > M/2:    # non-square
#             dx, dy = -dy, dx                # change direction
#             x, y = -y+dx, x+dy              # jump
#
#         yield x, y
#         x, y = x+dx, y+dy

# Part 1 of the question
def Sum_Spiral(N):
    x, y = 0, 0
    dx, dy = 0, -1
    sum=1
    while sum < N:
        if abs(x) == abs(y) and [dx, dy] != [1, 0] or x > 0 and y == 1 - x:
            dx, dy = -dy, dx  # corner, change direction
        x, y = x + dx, y + dy
        sum=sum+1
    print(abs(x)+abs(y), sum)
    return x,y
N=325489
Sum_Spiral(N)

# Part 1 of the question
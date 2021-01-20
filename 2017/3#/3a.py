 # finding the step of the spiral memory
import math
# def spiral(input):
input = 325489
r = 0
while input > math.pow((2*r+1), 2):
     r += 1
print(r)

Right_Bottom = math.pow((2*r+1), 2)
Left_Bottom = Right_Bottom - 2*r
Left_Top = Left_Bottom - 2*r
Right_Top = Left_Top - 2*r

if input <= Right_Top:
     x = r
     y = r-(Right_Top-input)
     print("Coordinate:", "X=", int(x), "Y'", int(y), "Distance:", int(abs(x)+abs(y)))
elif input <= Left_Top:
     x = -(r - (Left_Top - input))
     y = r
     print("Coordinate:", "X=", int(x), "Y'", int(y), "Distance:", int(abs(x) + abs(y)))
elif input <= Left_Bottom:
     x = -r
     y = -(r - (Left_Bottom - input))
     print("Coordinate:", "X=", int(x), "Y'", int(y), "Distance:", int(abs(x) + abs(y)))
else:
     x = (r - (Right_Bottom - input))
     y = -r
     print("Coordinate:", "X=", int(x), "Y'", int(y), "Distance:", int(abs(x) + abs(y)))

# spiral(input)
 # Right_Bottom=(2*r+1)^2
# Left_Bottom = Right_Bottom - 2*r
# Left_Top = Left_Bottom - 2*r
# Right_Top = Left_Top - 2*r

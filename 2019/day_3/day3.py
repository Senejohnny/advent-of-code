import re
with open('input_day3.txt') as file:
    input = [_.split(',') for _ in file.read().splitlines()]

move = {
    'D': lambda x, y, z: [(x, y - _) for _ in range(1, z+1)],
    'U': lambda x, y, z: [(x, y + _) for _ in range(1, z+1)],
    'L': lambda x, y, z: [(x - _, y) for _ in range(1, z+1)],
    'R': lambda x, y, z: [(x + _, y) for _ in range(1, z+1)],
} 

def get_coordinates(insts:str):
    x, y = 0, 0
    coords = [(x, y)]
    for inst in insts:
        dirc, step = re.findall(r'(\w+?)(\d+)', inst)[0]
        coords.extend(move[dirc](x, y, int(step)))
        x, y = coords[-1]
    return coords

def find_cross_points(input):
    wire_1 = get_coordinates(input[0])
    wire_2 = get_coordinates(input[1])
    crosses =  set(wire_1).intersection(set(wire_2)) - {(0, 0)}
    return wire_1, wire_2, crosses

####################################
# Part 1
####################################
def min_manhatan_dist(crosses): 
    return min([abs(_[0])+abs(_[1]) for _ in crosses])

def solution_part_1(input):
    _, _, crosses = find_cross_points(input)
    return min_manhatan_dist(crosses)

####################################
# Part 2
####################################
def min_length(wire_1, wire_2, crosses):
    steps = []
    for cross in crosses:
        ind_cross_w1 = wire_1.index(cross)
        ind_cross_w2 = wire_2.index(cross)
        steps.append(len(wire_1[0:ind_cross_w1]) + len(wire_2[0:ind_cross_w2]))
    return min(steps)

def solution_part_2(input):
    wire_1, wire_2, crosses = find_cross_points(input)
    return min_length(wire_1, wire_2, crosses)

if __name__ == '__main__':
    print('Solution to part 1 is:', solution_part_1(input))
    print('Solution to part 2 is:', solution_part_2(input))
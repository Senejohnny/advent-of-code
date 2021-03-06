""" day 1 of advent of code """
import os
path = os.path.abspath('./day_1/input_day1.txt')
with open(path) as file:
    modules_masses = [x.strip() for x in file.read().splitlines()]

# Part 1
print('Part 1:', sum([(int(mass) // 3 - 2) for mass in modules_masses]))

# Part 2
def calculate_fule(mass, _sum=0):
    """ function that calculates spent fule """
    fule = mass // 3 - 2
    if fule > 0:
        _sum += fule
        return calculate_fule(fule, _sum)
    return _sum

print('Part 2:', sum([calculate_fule(int(mass)) for mass in modules_masses]))

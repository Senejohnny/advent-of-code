with open('input_day1.txt') as file:
    modules_masses = [x.strip() for x in file.read().splitlines()]

# Part 1
print('Part 1:', sum([(int(mass) // 3 - 2) for mass in modules_masses]))

# Part 2
def calculate_fule(mass, _sum=0):
    fule = mass // 3 - 2 
    if fule > 0:
        _sum += fule
        return calculate_fule(fule, _sum)
    else:
        return _sum

print('Part 2:', sum([calculate_fule(int(mass)) for mass in modules_masses]))
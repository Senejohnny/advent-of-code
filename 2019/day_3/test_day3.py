import pytest
from day3 import solution_part_1, solution_part_2

test_input_1 = ([['R8','U5', 'L5', 'D3'], ['U7','R6','D4','L4']], 6)
test_input_2 = ([['R75','D30','R83','U83','L12','D49','R71','U7','L72'] ,['U62','R66','U55','R34','D71','R55','D58','R83']], 159)
test_input_3 = ([['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']], 135)

test_input_4 = ([['R8','U5', 'L5', 'D3'], ['U7','R6','D4','L4']], 30)
test_input_5 = ([['R75','D30','R83','U83','L12','D49','R71','U7','L72'] ,['U62','R66','U55','R34','D71','R55','D58','R83']], 610)
test_input_6 = ([['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']], 410)

@pytest.mark.parametrize("test_input, expected_output", 
    [
        test_input_1,
        test_input_2,
        test_input_3,
    ]
)
def test_solution_part_1(test_input, expected_output):
    assert solution_part_1(test_input) == expected_output

@pytest.mark.parametrize("test_input, expected_output", 
    [
        test_input_4,
        test_input_5,
        test_input_6,
    ]
)
def test_solution_part_2(test_input, expected_output):
    assert solution_part_2(test_input) == expected_output
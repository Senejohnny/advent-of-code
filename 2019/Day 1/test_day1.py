import pytest
from day1 import calculate_fule

@pytest.mark.parametrize("test_input, expected_output", 
    {
        (14, 2),
        (1969, 966),
        (100756, 50346),
    }
)
def test_calculate_fule(test_input, expected_output):
    assert calculate_fule(test_input) == expected_output
import numpy as np
from collections import Counter
lower, upper = map(int, '134792-675810'.split('-'))

# Part 1
cond = {
    'non-dec': lambda x: sorted(x) == list(x),
    'rep': lambda x: 0 in np.diff([int(_) for _ in list(x)]),
    '2rep': lambda x: 2 in Counter(x).values()
}
print('Part 1:', sum([True for i in range(lower, upper) if cond['non-dec'](str(i)) if cond['rep'](str(i))]) )

# Part 2
print('Part 2:', sum([True for i in range(lower, upper) if cond['non-dec'](str(i)) if  cond['2rep'](str(i))]) )

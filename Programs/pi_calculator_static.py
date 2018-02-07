# Pi Calculator

import sys
p = 0

for i in range(1, 299999999, 4):
    p += (-1 / (i + 2)) + (1 / (i + 4))

pi = 4 * (1 + p)
print(pi)

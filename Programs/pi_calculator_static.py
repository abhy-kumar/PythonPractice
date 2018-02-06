# Pi Calculator
p = 0

for i in range(1, 99999999, 4):
    p += (-1 / (i + 2)) + (1 / (i + 4))

pi = 4 * (1 + p)
print(pi)

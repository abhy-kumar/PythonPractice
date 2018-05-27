n = input()
n = int(n)

l = ('A', 'B', 'C', 'D', 'E', 'F', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', )

def cycle(l, start_at=None):
    start_at = 0 if start_at is None else l.index(start_at)
    while True:
        yield l[start_at]
        start_at = (start_at + 1) % len(l)

for i in range(0,n):
    for j in range(0,i):
        print("*",end="")
    print("\n")
for i in range(0,n):
    for idx, elem in enumerate(l):
        thiselem = elem
        nextelem = l[(idx + 1) % len(l)]


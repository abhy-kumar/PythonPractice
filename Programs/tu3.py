n = input()
n = int(n)
d = 0
d1 = 0
a = []
arr = [int(x) for x in input().split()]

x, y = input().split()

x = int(x)
y = int(y)

a = arr.index(x)
b = arr.index(y)

for i in range(a,b):
    d = d + arr[a]

if (a >= len(arr)/2) or (b >= len(arr)/2):
    d1 = sum(arr) - d

if(d<d1):
    print(d)
else:
    print(d1)

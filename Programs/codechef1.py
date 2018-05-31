#
def find(x, l, r, mylist):
    count = 0
    for i in range(l - 1, r):
        if (x == mylist[i]):
            count = count + 1
    print(count)


n = input()
n = int(n)

mylist = []

mylist = list(map(int, input().split()))

q = input()
q = int(q)

for i in range(0, q):
    x, L, R = map(int, input().split())
    find(x, L, R, mylist)

def calc(mylist,s):
    l = 0
    r = s
    m = len(mylist) % s
    temp = []
    #for i in range(0,m+1):
    for i in range(l,r+1):
        req = sum(mylist[l:r])
        temp.append(req)
        l = l + 1
        r = r + 1
    print(max(temp))



t = int(input())

for i in range (0,t):
    n = input()
    n = int(n)
    mylist = []
    mylist = list(map(int, input().split()))
    s = input()
    s = int(s)
    calc(mylist,s)
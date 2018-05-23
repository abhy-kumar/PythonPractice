
t = int(input())

for i in range(0,t):
    d1 = 1
    count = 1
    d = int(input())
    while(d1<d):
        d1 = 1 + count * 9
        count = count + 1
    print(count)



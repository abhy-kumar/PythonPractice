def dis(l_list, index1, index2, mylist):
    m = mylist.index(index1)
    n = mylist.index(index2)
    i = 0
    j = 0
    if n > m:
        while n > m:
            i = i + mylist[m]
            m = m + 1
    elif n < m:
        while n < m:
            j = j + mylist[n]
            n = n + 1
    else:
        return (0)
    print(i)
    print(j)
    print(min(i,j))


l_mylist = input()
l_mylist = int(l_mylist)

mylist = []

mylist = list(map(int, input().split()))

i, j = input().split()
i, j = int(i), int(j)
dis(l_mylist, i, j, mylist)
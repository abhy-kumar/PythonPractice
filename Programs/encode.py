def enco(istr):
    arr = []
    arr = list(istr)
    l = len(istr)

    print(istr[0] + istr[1] + str(len(istr)) + istr[-2] + istr[-1])

n = input()
n = int(n)


for i in range(0,n):
    istr = input()
    k = int(len(istr))
    if(k>8):
        enco(istr)
    else:
        print(istr)
def collatz(x):
    if x % 2 == 0:
        print(x // 2)
    else:
        print(x * 3 + 1)


x = int(input())
collatz(x)

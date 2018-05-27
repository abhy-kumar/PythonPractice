def collatz(x):
	if x % 2 == 0:
		return x//2
	return x*3 + 1

x = int(input())
collatz(x)
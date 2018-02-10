# This program reverses a given string.

print("Enter your string.\n")
a = input()

c = list(a)
ar = []

for i in range(0,len(c)):
    ar.append(c[len(c)-i-1])

ar = ' '.join(ar)
print(ar)
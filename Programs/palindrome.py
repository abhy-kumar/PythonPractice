print("Enter your word.\n")
a = input()
a = a.lower()
flag  = 0
c = list(a)
ar = []
for i in range(0,len(c)):
    if c[i] == ' ':
        print('Enter a single word.')
        flag = 1
for i in range(0,len(c)):
    ar.append(c[len(c)-i-1])

ar = ''.join(ar)
ar = ar.lower()

if flag == 0:
    if ar == a:
        print('The word is a palindrome.')
    else:
        print('Not a palindrome.')
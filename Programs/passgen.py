import random
import pandas as pd

# Change this to the desired password length.
n = 8

pw = []

s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'xy', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
     'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# Character containing Array

for i in range(0, n):
    pw.append(s[random.randrange(len(s))])

fpw = ''.join((pw))
print(fpw)

# copy directly to clipboard if a password is generated.
df = pd.DataFrame([fpw])
df.to_clipboard(index=False, header=False)

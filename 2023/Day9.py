test = \
"""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

smoltest = "0 3 6 9 12 15"

new = smoltest.split('\n')
print(new)

for i,subs in enumerate(new):
    new[i] = subs.split(' ')
print(new)

with open("Day9input.txt") as f:
    text = f.read()
print(text)

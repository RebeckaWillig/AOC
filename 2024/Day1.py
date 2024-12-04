import re

with open("Day1input.txt") as f:
    text = f.read()

test = \
"""3   4
4   3
2   5
1   3
3   9
3   3"""

new = re.split('   |\n',text)
#print(new)

left = []
right = []

for (i,x) in enumerate(new):
    if i % 2 == 0:
        left.append(int(x))
    else:
        right.append(int(x))

left.sort()
right.sort()

result1 = 0

for i in range(len(left)):
    result1 += abs(left[i]-right[i])

print(result1)

result2 = 0

for x in left:
    result2 += right.count(x)*x

print(result2)

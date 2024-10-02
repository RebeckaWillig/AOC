with open("Day3input.txt") as f:
    text = f.read()

test = "^v^v^v^v^v"

h = 0
v = 0
list = [(0,0)]

new0 = []
new1 = []

for i,elem in enumerate(text):
    if (i % 2 == 0):
        new0.append(elem)
    else:
        new1.append(elem)

for i in new0:
    if (i == 'v'):
        v -= 1
    elif (i == '^'):
        v += 1
    elif (i == '<'):
        h -= 1
    else:
        h += 1

    if (h,v) not in list:
        list.append((h,v))

h = 0
v = 0

for i in new1:
    if (i == 'v'):
        v -= 1
    elif (i == '^'):
        v += 1
    elif (i == '<'):
        h -= 1
    else:
        h += 1

    if (h,v) not in list:
        list.append((h,v))

print(len(list))


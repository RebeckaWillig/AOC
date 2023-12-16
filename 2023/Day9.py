with open("Day9input.txt") as f:
    text = f.read()

test = \
"""0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

def find_next_sequence(s):
    next_sequence = []
    for i in range(len(s)-1):
        next_sequence.append(s[i+1]-s[i])
    return next_sequence

def add_next_value(sequences):
    l = len(sequences)
    sequences[l-1].append(0)
    for i in range(l-1):
        s1 = sequences[l-2-i]
        s2 = sequences[l-1-i]
        s1.append(s1[-1]+s2[-1])

def add_previous_value(sequences):
    for s in sequences:
        s.reverse()
    l = len(sequences)
    sequences[l-1].append(0)
    for i in range(l-1):
        s1 = sequences[l-2-i]
        s2 = sequences[l-1-i]
        s1.append(s1[-1]-s2[-1])


smoltest = "10 13 16 21 30 45"

new = text.split('\n')
#print(new)

for i,subs in enumerate(new):
    new[i] = subs.split(' ')
#print(new)

result1 = 0
result2 = 0
for history in new:
    for i,n in enumerate(history):
        history[i] = int(n)
    sequences = []
    sequences.append(history)
    while any(sequences[-1]):
        current_sequence = sequences[-1]
        next_sequence = find_next_sequence(current_sequence)
        sequences.append(next_sequence)
        #print(sequences[-1])
    #print(sequences)
    add_next_value(sequences)
    #print(sequences)
    result1 += sequences[0][-1]
    add_previous_value(sequences)
    #print(sequences)
    result2 += sequences[0][-1]
print("Part 1:",result1)
print("Part 2:",result2)









text = \
"""Time:        55     99     97     93
Distance:   401   1485   2274   1405"""

test = \
"""Time:      7  15   30
Distance:  9  40  200"""

smoltest = \
"""Time: 30
Distance: 200"""

#Part1

new1 = text.split('\n')
ts = new1[0].split()[1:len(new1[0])]
ds = new1[1].split()[1:len(new1[1])]
#print(ts,ds)
result1 = 1

for t,d in zip(ts,ds):
    t = int(t)
    d = int(d)
    i = 0
    while (i*(t-i)) <= d:
        i += 1
    ways = t-2*i+1
    #print(ways)
    result1 *= ways

print("Part 1:",result1)

#Part2

new2 = text.split('\n')
time = int(new2[0].replace(' ','').split(':')[1])
dist = int(new2[1].replace(' ','').split(':')[1])
#print(time,dist)

i = 0
while (i*(time-i)) <= dist:
    i += 1
result2 = time-2*i+1
print("Part 2:",result2)

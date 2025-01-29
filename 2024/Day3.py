import re
import fnmatch

with open("Day3input.txt") as f:
    text = f.read()

test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
new = test.split('mul')
#print(new)

filtered = fnmatch.filter(new, '(*,*)*')
print(filtered)

for instr in filtered:
    #print(instr)
    if instr[2] == ',':
        if instr[1].isnumeric:
            x = int(instr[1])
        #if instr[]



with open("Day12input.txt") as f:
    text = f.read()

test = \
"""???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""

smoltest = "???.### 1,1,3"

def part(row):
    row = row.split()
    first = row[0]
    second = row[1].split(',')
    #second = list(map(int,second))
    second = [int(c) for c in second]
    print(first)
    print(second)

def valid_row(row):
    print()    

print(smoltest)


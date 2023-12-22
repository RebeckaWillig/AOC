with open("Day10input.txt") as f:
    text = f.read()

test1 = \
"""-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""

test2 = \
"""7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

new  = text.split('\n')

class Pipe():
    def __init__(self,r=0,c=0,t=None):
        self.r = r  #row
        self.c = c  #column
        self.t = t  #type
    def print(self):
        print((self.r,self.c),self.t)

def find_start(sketch):
    for i,r in enumerate(sketch):
        j = r.find('S')
        if j != -1:
            return Pipe(i,j,'S')

def find_first(sketch,start):
    first = Pipe()
    p = sketch[start.r-1][start.c]  # north
    if p == '|' or p == '7' or p == 'F':
        first.r = start.r-1
        first.c = start.c
        first.t = p
        return first
    p = sketch[start.r][start.c+1]  # east
    if p == '-' or p == '7' or p == 'J':
        first.r = start.r
        first.c = start.c+1
        first.t = p
        return first
    p = sketch[start.r+1][start.c]  # south
    if p == '|' or p == 'L' or p == 'J':
        first.r = start.r+1
        first.c = start.c
        first.t = p
        return first
    p = sketch[start.r][start.c-1]  # west
    if p == '-' or p == 'L' or p == 'F':
        first.r = start.r
        first.c = start.c-1
        first.t = p
        return first

def find_next(sketch,current,previous):
    next = Pipe()
    if current.t == '|':
        next.c = current.c
        if current.r < previous.r:
            next.r = current.r - 1  # north
        else:
            next.r = current.r + 1  # south
    elif current.t == '-':
        next.r = current.r
        if current.c < previous.c:
            next.c = current.c - 1  # west
        else:
            next.c = current.c + 1  # east
    elif current.t == 'L':
        if current.c == previous.c:
            next.r = current.r
            next.c = current.c + 1  # east
        else:
            next.r = current.r - 1  # north
            next.c = current.c
    elif current.t == 'J':
        if current.c == previous.c:
            next.r = current.r
            next.c = current.c - 1  # west
        else:
            next.r = current.r - 1  # north
            next.c = current.c
    elif current.t == '7':
        if current.c == previous.c:
            next.r = current.r
            next.c = current.c - 1  # west
        else:
            next.r = current.r + 1  # south
            next.c = current.c
    elif current.t == 'F':
        if current.c == previous.c:
            next.r = current.r
            next.c = current.c + 1  # east
        else:
            next.r = current.r + 1  # south
            next.c = current.c
    else:
        print("Something is wrong")
    next.t = sketch[next.r][next.c]
    #next.print()
    return next

start_pipe = find_start(new)
#start_pipe.print()
pipe_list = [start_pipe]
first_pipe = find_first(new,start_pipe)
pipe_list.append(first_pipe)

while pipe_list[-1].t != 'S':
    p = find_next(new,pipe_list[-1],pipe_list[-2])
    pipe_list.append(p)
    #p.print()

result = (len(pipe_list)-1)//2
print(result)

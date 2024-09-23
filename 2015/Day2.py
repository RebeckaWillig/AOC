with open("Day2input.txt") as f:
    text = f.read()

test = "2x3x4"

new = text.split('\n')
paper = 0
ribbon = 0

for i in new:
    dim = i.split('x')

    a = int(dim[0]) * int(dim[1])
    b = int(dim[0]) * int(dim[2])
    c = int(dim[1]) * int(dim[2])

    size = 2*a + 2*b + 2*c + min([a,b,c])
    paper += size

    wrap = (int(dim[0]) + int(dim[1]) + int(dim[2]) - max([int(dim[0]),int(dim[1]),int(dim[2])]))*2
    bow = int(dim[0]) * int(dim[1]) * int(dim[2])
    ribbon += wrap + bow

print(paper)
print(ribbon)
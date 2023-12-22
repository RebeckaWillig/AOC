with open("Day11input.txt") as f:
    text = f.read()

test = \
"""...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

smoltest = """.#
.."""

def no_galaxies(row):
    for column in row:
        if column == '#':
            return False
    return True

def add_rows(image):
    new_image = []
    for row in image:
        if no_galaxies(row):
            new_image.append(row)
        new_image.append(row)
    return new_image

def transpose_image(image):
    new_image = []
    l = len(image[0])
    for _ in range(l):
        new_image.append([])
    for row in image:
        for j,c in enumerate(row):
            new_image[j].append(c)
    return new_image

def expand(image):
    image = add_rows(image)
    image = transpose_image(image)
    image = add_rows(image)
    image = transpose_image(image)
    return image

def find_galaxies(image):
    galaxies = []
    for i,row in enumerate(image):
        for j,c in enumerate(row):
            if c == '#':
                galaxies.append((i,j))
    return galaxies

def shortest_path(g1,g2):
    return abs(g1[0]-g2[0]) + abs(g1[1]-g2[1])

def shortest_path2(g1,g2,ers,ecs,size):
    if g1[0] < g2[0]:
        verdis = range(g1[0],g2[0])
    elif g1[0] > g2[0]:
        verdis = range(g2[0],g1[0])
    else:
        verdis = []
    if g1[1] < g2[1]:
        hordis = range(g1[1],g2[1])
    elif g1[1] > g2[1]:
        hordis = range(g2[1],g1[1])
    else:
        hordis = []
    distance = 0
    for i in verdis:
        if i in ers:
            distance += size
        else:
            distance += 1
    for i in hordis:
        if i in ecs:
            distance += size
        else:
            distance += 1
    return distance


def f(gs,size):
    path_lengths = 0
    l = len(gs)-1
    for i in range(l):
        for j in range(i,l):
            path_lengths += shortest_path2(gs[i],gs[j+1],empty_rows,empty_columns,size)
    return path_lengths

def galaxy_free(image):
    free_row = []
    for i,row in enumerate(image):
        if no_galaxies(row):
            free_row.append(i)
    return free_row


new = text.split('\n')
new = [list(c) for c in new]

transposed = transpose_image(new)
empty_rows = galaxy_free(new)
empty_columns = galaxy_free(transposed)
galaxies = find_galaxies(new)

result1 = f(galaxies,2)
print("Part 1:",result1)
result2 = f(galaxies,1000000)
print("Part 2:",result2)


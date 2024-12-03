import re
import numpy as np

with open("Day6input.txt") as f:
    text = f.read()

new = text.split('\n')

test = "toggle 0,0 through 9,9"

lights = np.array(1000*[1000*[0]])

def turn_on(x1,x2,y1,y2):
    for r in range (x1, x2+1):
        for c in range (y1, y2+1):
            lights[r][c] += 1

def turn_off(x1,x2,y1,y2):
    for r in range (x1, x2+1):
        for c in range (y1, y2+1):
            if lights[r][c] != 0:
                lights[r][c] -= 1

def toggle(x1,x2,y1,y2):
    for r in range (x1, x2+1):
        for c in range (y1, y2+1):
            lights[r][c] += 2


for i in new:
    instr = re.split(' |,', i)

    if len(instr) == 6:
        toggle(int(instr[1]), int(instr[4]), int(instr[2]), int(instr[5]))
    elif instr[1] == 'on':
        turn_on(int(instr[2]), int(instr[5]), int(instr[3]), int(instr[6]))
    else:
        turn_off(int(instr[2]), int(instr[5]), int(instr[3]), int(instr[6]))


print(lights.sum())


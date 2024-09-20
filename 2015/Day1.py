with open("Day1input.txt") as f:
    text = f.read()

test = "()))"

floor = 0
result = 0

for p,i in enumerate(text):
    if i == "(":
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        result = p+1
        break


print(result)


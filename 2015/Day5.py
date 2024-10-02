with open("Day5input.txt") as f:
    text = f.read()

new = text.split('\n')

test = "Heloop"
vowels = "aeiou"
bads = ["ab","cd","pq","xy"]

def has_vowels(string):
    n_vowels = 0
    for i in string:
        if i in vowels:
            n_vowels += 1
    if n_vowels >= 3:
        return True
    return False

def has_doubles(string):
    for i in range (1,len(string)):
        if string[i] == string[i-1]:
            return True
    return False

def has_no_bads(string):
    for i in bads:
        if i in string:
            return False
    return True

def has_pairs(string):
    if len(string) < 4:
        return False
    if string[:2] in string[2:]:
        return True
    return has_pairs(string[1:])

def has_repeat(string):
    if len(string) < 3:
        return False
    if string[0] == string[2]:
        return True
    return has_repeat(string[1:])

def is_nice(string):
    return (has_pairs(string) and has_repeat(string))

result = 0

for i in new:
    if is_nice(i):
        result += 1

print(result)

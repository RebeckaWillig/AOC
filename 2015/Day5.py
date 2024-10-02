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

def is_nice(string):
    return (has_vowels(string) and has_doubles(string) and has_no_bads(string))

result = 0

for i in new:
    if is_nice(i):
        result += 1

print(result)


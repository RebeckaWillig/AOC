import hashlib

input = "bgvyzdsv"

def get_md5(input_string):
    return hashlib.md5(input_string.encode()).hexdigest()

i = 0

while True:
    input_string = input + str(i)
    result = get_md5(input_string)
    if(result.startswith("00000")):
        print(i)
        print(result)
    i += 1


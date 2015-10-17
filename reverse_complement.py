import sys

def read_input():
    return sys.stdin.read().splitlines()

def complement(base):
    if base == "A":
        return "T"
    elif base == "T":
        return "A"
    elif base == "C":
        return "G"
    elif base == "G":
        return "C"

def reverse_complement(pattern):
    result = [None] * len(pattern)
    for i in range(0,len(pattern)):
        result[i] = complement(pattern[-1-i])
    return result

data = read_input()
result = reverse_complement(data[0].strip())
print(''.join(result))

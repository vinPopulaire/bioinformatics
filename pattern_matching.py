import sys

def read_input():
    return sys.stdin.read().splitlines()

def pattern_matching(pattern, genome):
    indices = []
    for i in range(0, len(genome) - len(pattern) + 1):
        if (pattern == genome[i:i+len(pattern)]):
            indices.append(str(i))
    return indices


data = read_input()
result = pattern_matching(data[0].strip(), data[1].strip())
print(" ".join(result))


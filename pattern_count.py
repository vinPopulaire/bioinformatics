import sys

def read_input():
    return sys.stdin.read().splitlines()

def pattern_count(text, pattern):
    count = 0
    for i in range(0, len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1
    return count

data = read_input()
result = pattern_count(data[0].strip(),data[1].strip())

print(result)

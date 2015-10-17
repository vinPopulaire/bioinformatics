import sys

def read_input():
    return sys.stdin.read().splitlines()

def sym_to_num(sym):
    if sym == "A":
        return 0
    elif sym == "T":
        return 1
    elif sym == "C":
        return 2
    elif sym == "G":
        return 3

def num_to_sym(num):
    if num == 0:
        return "A"
    elif num == 1:
        return "T"
    elif num == 2:
        return "C"
    elif num == 3:
        return "G"

def pattern_to_num(pattern):
    if len(pattern) == 0:
        return 0
    return 4*pattern_to_num(pattern[0:-1]) + sym_to_num(pattern[-1])

def num_to_pattern(num, k):
    if k == 1:
        return num_to_sym(num)
    prefix = num // 4
    last = num % 4
    sym = num_to_sym(last)
    pattern = num_to_pattern(prefix, k-1)

    return pattern + sym

def create_list(k):
    return [0]*(4**k)

def max_list(frequency_list):

    maximum = 0
    max_list = []

    for index, k_mer in enumerate(frequency_list):
        if (maximum < k_mer):
            maximum = k_mer
            max_list = [index]
        elif (maximum == k_mer):
            max_list.append(index)
    return max_list

def frequent_words(text, k):
    result = []

    frequency_list = create_list(k)

    for i in range(0, len(text)-k+1):
        current = text[i:i+k]
        index = pattern_to_num(current)
        frequency_list[index] += 1

    most_frequent = max_list(frequency_list)
    for k_mer in most_frequent:
        result.append(num_to_pattern(k_mer, k))
    return result

data = read_input()
result = frequent_words(data[0].strip(), int(data[1]))
print(" ".join(result))

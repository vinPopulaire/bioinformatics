import sys

def read_input():
    return sys.stdin.read().splitlines()

def sym_to_num(sym):
    if sym == "A":
        return 0
    elif sym == "C":
        return 1
    elif sym == "G":
        return 2
    elif sym == "T":
        return 3

def num_to_sym(num):
    if num == 0:
        return "A"
    elif num == 1:
        return "C"
    elif num == 2:
        return "G"
    elif num == 3:
        return "T"

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

def max_list(dictionary):

    maximum = 0
    max_list = []

    for key, k_mer in dictionary.items():
        if (maximum < k_mer):
            maximum = k_mer
            max_list = [key]
        elif (maximum == k_mer):
            max_list.append(key)
    return max_list

def frequent_words(text, k):
    result = []

    frequency_hash = {}

    for i in range(0, len(text)-k+1):
        current = text[i:i+k]
        index = pattern_to_num(current)
        if index in frequency_hash:
            frequency_hash[index] += 1
        else:
            frequency_hash.setdefault(index, 1)

    most_frequent = max_list(frequency_hash)
    for k_mer in most_frequent:
        result.append(num_to_pattern(k_mer, k))
    return result

data = read_input()
result = frequent_words(data[0].strip(), int(data[1]))
print(" ".join(result))

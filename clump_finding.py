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

def clump_finding(genome, k, L, t):
    result = []
    frequency_hash = {}
    clumps = {}
    text = genome[0:L]

    for i in range(0, len(text)-k+1):
        current = text[i:i+k]
        index = pattern_to_num(current)
        if index in frequency_hash:
            frequency_hash[index] += 1
            if frequency_hash[index] == t:
                clumps[index] = 1
        else:
            frequency_hash.setdefault(index,1)
            clumps.setdefault(index,0)

    for i in range(1, len(genome)-L+1):
        text = genome[i:i+L]

        previous_kmer = genome[i-1:i-1+k]
        previous_kmer_index = pattern_to_num(previous_kmer)
        new_kmer = genome[i+L-k:i+L]
        new_kmer_index = pattern_to_num(new_kmer)

        frequency_hash[previous_kmer_index] -= 1
        if new_kmer_index in frequency_hash:
            frequency_hash[new_kmer_index] += 1
            if frequency_hash[new_kmer_index] == t:
                clumps[new_kmer_index] = 1
        else:
            frequency_hash.setdefault(new_kmer_index,1)
            clumps.setdefault(new_kmer_index,0)

    for k_mer in clumps:
        if clumps[k_mer] == 1:
            result.append(num_to_pattern(k_mer, k))
    return result

data = read_input()
input_nums = data[1].split(' ')
result = clump_finding(data[0].strip(), int(input_nums[0]), int(input_nums[1]), int(input_nums[2]))
print(" ".join(result))

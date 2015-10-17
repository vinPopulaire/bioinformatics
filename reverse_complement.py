def read_input(filename):
    file = open(filename,'r')
    return file.readlines()

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

data = read_input("data.txt")
text = data[0].strip()

print ''.join(reverse_complement(text))

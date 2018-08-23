import math

PATTERN = [1, 10, 9, 12, 3, 4]

def thirt(n):
    seq = [int(digit) for digit in str(n)][::-1]
    total = 0
    pattern_factor = math.ceil(len(seq) / len(PATTERN))
    if pattern_factor == 1:
        full_pattern = PATTERN[:-(len(PATTERN)-len(seq))]
    else:
        full_pattern = PATTERN * math.ceil(len(seq) / len(PATTERN))
        remainder = len(full_pattern) % len(seq)
        full_pattern = full_pattern[:-remainder]
    for i, _ in enumerate(seq):
        total += seq[i] * full_pattern[i]
    if total == n:
        return total
    return thirt(total)

print(thirt(85299258))
print(thirt(321))
print(thirt(1234567))

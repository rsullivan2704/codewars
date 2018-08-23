def revrot(strng, sz):
    if sz <= 0 or sz > len(strng) or strng == '':
        return ''
    start = 0
    subcount = len(strng) / sz
    result = ''
    while subcount > 0:
        sub = strng[start:(sz + start)]
        if len(sub) < sz:
            continue
        else:
            total = 0
            digits = [int(char) for char in sub]
            for digit in digits:
                total += digit**3
            if total % 2 == 0:
                digits = digits.reverse()
            else:
                digits.append(digits[0])
                digits.remove(digits[0])
            result += ''.join([str(digit) for digit in digits])
        start += sz
        subcount -= 1
    return result

print revrot("733049910872815764", 5)

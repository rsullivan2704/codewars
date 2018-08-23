def persistence(n):
    digits = list(str(n))
    finished = False
    count = 0
    while not finished:
        count += 1
        result = 1
        for digit in digits:
            result *= int(digit)
        if result < 10:
            finished = True
        else:
            digits = list(str(result))
    return count

persistence(39)

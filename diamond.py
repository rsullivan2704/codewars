def diamond(n):
    if n % 2 == 0 or n < 0:
        return None
    diamondformat = '{0}{1}{2}'
    diamondresult = diamondformat.format('', ("*" * n), '\n')
    length = n - 2
    while length > 0:
        currentline = diamondformat.format(' ' * ((n - length) / 2), ('*' * length), '\n')
        diamondresult = diamondformat.format(currentline, diamondresult, currentline)
        length -= 2
    return diamondresult

expected =  " *\n"
expected += "***\n"
expected += " *\n"
print diamond(31)

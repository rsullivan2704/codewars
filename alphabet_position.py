import string

def alphabet_position(text):
    alpha = string.ascii_lowercase
    result = ''
    for char in text.lower():
        if char.isalpha():
            result += str(alpha.find(char) + 1) + ' '
    return result.rstrip()

alphabet_position("The sunset sets at twelve o' clock.")

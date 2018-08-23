import math

def decrypt(encrypted_text, n):
    if encrypted_text is None or encrypted_text == '':
        return encrypted_text
    text_list = list(encrypted_text)
    if n > 0:
        result = []
        # beginchars = text_list[0:(int(math.ceil(len(text_list)) / 2))]
        # endchars = text_list[int(math.floor(len(text_list) / 2)):len(text_list)]
        for index, char in enumerate(text_list):
            if index % 2 == 0:
                result.append(text_list[index + int(math.ceil(len(text_list)) / 2)])
            else:
                result.append(text_list[index - 1])
        n -= 1
        return decrypt(''.join(result), n)
    else:
        return encrypted_text

def encrypt(text, n):
    if text is None or text == '':
        return text
    text_list = list(text)
    if n > 0:
        leftovers = []
        result = []
        for index, char in enumerate(text_list):
            if (index + 1) % 2 == 0:
                result.append(char)
            else:
                leftovers.append(char)
        result.extend(leftovers)
        n -= 1
        return encrypt(''.join(result), n)
    else:
        return text

print encrypt('This is a test!', 1)
print encrypt("This is a test!", 3)
print encrypt("", 0)
print encrypt(None, 0)

print decrypt("This is a test!", 0)
print decrypt("hsi  etTi sats!", 1)

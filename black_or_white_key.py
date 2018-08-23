
SCALE = {
    1: 'white',
    2: 'black',
    3: 'white',
    4: 'white',
    5: 'black',
    6: 'white',
    7: 'black',
    8: 'white',
    9: 'white',
    10: 'black',
    11: 'white',
    12: 'black'
}

def black_or_white_key(key_press_count):
    count = key_press_count
    if count > 88:
        count %= 88
        if count == 0:
            count = 4
    if count > 12:
        count %= 12
        if count == 0:
            count = 12
    return SCALE[count]

# def black_or_white_key(key_press_count):
#     count %= 88 if count > 88 else count % 12 if count > 12 else count = 12 if count == 0
#     return SCALE[count]
    
# print('1', black_or_white_key(1))
# print('5', black_or_white_key(5))
# print('12', black_or_white_key(12))
# print('42', black_or_white_key(42))
# print('88', black_or_white_key(88))
# print('89', black_or_white_key(89))
# print('92', black_or_white_key(92))
# print('100', black_or_white_key(100))
# print('111', black_or_white_key(111))
# print('200', black_or_white_key(200))
# print('2017', black_or_white_key(2017))
print('2112', black_or_white_key(2112))
print('264', black_or_white_key(264))
print('6600', black_or_white_key(6600))

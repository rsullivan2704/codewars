import collections

def nico(key, message):
    sorted_key = sorted(key)
    numeric_key = [sorted_key.index(char) + 1 for char in key]
    message_stack = []
    stack_count = len(message) // len(numeric_key)
    pad_space_count = len(message) % len(numeric_key)
    i = 1
    start = 0
    end = len(numeric_key)
    for i in range(stack_count + 1):
        message_part = message[start:end]
        part_list = []
        for j in range(len(numeric_key)):
            num = numeric_key[j]
            if j < len(message_part):
                char = message_part[j]
            else:
                char = ' '
            part = (num, char)
            part_list.append(part)
        message_stack.append(part_list)
        start = end
        end += len(numeric_key)
        if end > len(message):
            end = len(message)
    encoded_message = ''
    for message_part in message_stack:
        sorted_part = sorted(message_part)
        encoded_message += ''.join([part[1] for part in sorted_part])
    return encoded_message


print(nico("crazy", "secretinformation"))
    
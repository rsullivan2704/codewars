def to_camel_case(text):
    text = text.replace('-', '_')
    text_list = text.split('_')
    text_list = [text_list[0]] + [strng.capitalize() for strng in text_list[1:]]
    return ''.join(text_list)

print to_camel_case("the_stealth_warrior")
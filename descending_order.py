def Descending_Order(num):
    num_string = str(num)
    num_list = sorted(num_string, reverse=True)
    sep = ''
    return int(sep.join(num_list))

Descending_Order(0)
Descending_Order(123456789)

def binary_array_to_number(arr):
    print int(''.join([str(num) for num in arr]), 2)
    return int(''.join([str(num) for num in arr]), 2)

binary_array_to_number([0,0,0,1])
binary_array_to_number([0,0,1,0])
binary_array_to_number([1,1,1,1])
binary_array_to_number([0,1,1,0])

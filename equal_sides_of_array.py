def find_even_index(arr):
    for i in range(len(arr)):
        left = arr[:i]
        right = arr[i + 1:]
        if sum(left) == sum(right):
            return i
    return -1

def find_even_index_comp(arr):
    index_list = [i for i in range(len(arr)) for a in [arr] if sum(a[:i]) == sum(a[i + 1:])]
    return index_list[0] if index_list else -1
    

print(find_even_index([10,-80,10,10,15,35,20]))
print(find_even_index_comp([10,-80,10,10,15,35,20]))
print(find_even_index_comp(range(1,100)))
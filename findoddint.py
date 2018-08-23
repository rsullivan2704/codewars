from collections import Counter

# def find_it(seq):
#     seq_dict = dict(zip(Counter(seq).keys(), Counter(seq).values()))
#     result = {k: v for k, v in seq_dict.iteritems() if v % 2 != 0}
#     print result.keys()[0]

# def find_it(seq):
#     seq_dict = dict(zip(Counter(seq).keys(), Counter(seq).values()))
#     result = list({k: v for k, v in seq_dict.iteritems() if v % 2 != 0}.keys())
#     print result[0]
#     return result[0]

def find_it(seq):
    for i in seq:
        if seq.count(i) %2 != 0:
            return i

find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])

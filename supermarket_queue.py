import collections

def queue_time(customers, n):
    if not customers:
        return 0
    if len(customers) == 1:
        return customers[0]
    registers = [[v] for v in customers[0:n]]
    queue = collections.deque(customers[n:])
    times = {}
    times = {i: sum(register) for i, register in enumerate(registers)}
    while len(queue) > 0:
        registers[min(times, key=times.get)].append(queue.popleft())
        times = {i: sum(register) for i, register in enumerate(registers)}
    return times[max(times, key=times.get)]

# print(queue_time([1,2,3,4,5], 1))
# print(queue_time([37, 38, 28, 19, 11, 2, 39, 40, 17, 5, 41, 34, 50, 35, 17, 12, 42, 17], 3))
print(queue_time([5, 50, 27, 29, 10, 35, 14, 28, 37, 16, 37, 37, 33, 31, 26, 17, 20, 9, 11, 41], 6))

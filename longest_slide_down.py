# pyramid slide kata

# def longest_slide_down(pyramid):
    #                             [75],                                         75
    #                           [95, 64],                                       95
    #                         [17, 47, 82],                                     82
    #                       [18, 35, 87, 10],                                   87
    #                     [20,  4, 82, 47, 65],                                 82
    #                   [19,  1, 23, 75,  3, 34],                               75
    #                 [88,  2, 77, 73,  7, 63, 67],                             88
    #               [99, 65,  4, 28,  6, 16, 70, 92],                           99
    #             [41, 41, 26, 56, 83, 40, 80, 70, 33],                         83
    #           [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],                       94
    #         [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],                     91
    #       [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],                   78
    #     [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],                 91
    #   [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],               89
    # [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]              98

    #     [3], 
    #   [7, 4], 
    #  [2, 4, 6], 
    # [8, 5, 9, 3]

import collections
import heapq

class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

class Pyramid:
    def __init__(self, data):
        self.data = data
        self.height = len(data)

    def in_bounds(self, id):
        (level, brick) = id
        return 0 <= level < self.height and 0 <= brick < self.height

    def neighbors(self, id):
        (level, brick) = id
        results = [(level + 1, brick), (level + 1, brick + 1)]
        results = filter(self.in_bounds, results)
        return results

    def cost(self, from_node, to_node):
        level, brick = to_node
        return self.data[level][brick] * -1

def get_pyramid(pyramid_data):
    pyramid = Pyramid(pyramid_data)
    # for level_idx, level in enumerate(pyramid_data):
    #     if level_idx + 1 < len(pyramid_data):
    #         for brick_idx, brick in enumerate(level):
    #             if brick_idx + 1 >= len(pyramid_data[level_idx + 1]):
    #                 pyramid.edges[(level_idx, brick_idx)] = [(level_idx + 1, brick_idx)]
    #             else:
    #                 pyramid.edges[(level_idx, brick_idx)] = [(level_idx + 1, brick_idx), (level_idx + 1, brick_idx + 1)]
    #     elif level_idx + 1 == len(pyramid_data):
    #         for brick_idx, brick in enumerate(level):
    #             pyramid.edges[(level_idx, brick_idx)] = []
    return pyramid

def breadth_first_search_1(pyramid, start):
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True
    while not frontier.empty():
        current = frontier.get()
        print("Visiting {0}".format(current))
        for next in pyramid.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True

def breadth_first_search_2(pyramid, start):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    while not frontier.empty():
        current = frontier.get()
        print("Visiting {0}".format(current))
        for next in pyramid.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    return came_from

def breadth_first_search_3(pyramid, start, goal):
    frontier = Queue()
    frontier.put(start)
    came_from = {}
    came_from[start] = None
    while not frontier.empty():
        current = frontier.get()
        if goal and current == goal:
            break
        for next in pyramid.neighbors(current):
            if next not in came_from:
                frontier.put(next)
                came_from[next] = current
    return came_from

def dijkstra_search(pyramid, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, pyramid.cost(None, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = pyramid.cost(None, start)
    while not frontier.empty():
        current = frontier.get()
        if goal and current == goal:
            break
        for next in pyramid.neighbors(current):
            new_cost = cost_so_far[current] + pyramid.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current
    return came_from, cost_so_far

def heuristic(goal, next):
    (goal_level, goal_brick) = goal
    (next_level, next_brick) = next
    return abs(goal_level - next_level) + abs(goal_brick - next_brick)

def a_star_search(pyramid, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, pyramid.cost(None, start))
    # came_from = {}
    cost_so_far = {}
    # came_from[start] = None
    cost_so_far[start] = pyramid.cost(None, start)
    while not frontier.empty():
        current = frontier.get()
        if goal and current == goal:
            break
        for next in pyramid.neighbors(current):
            new_cost = cost_so_far[current] + pyramid.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost # + heuristic(goal, next)
                frontier.put(next, priority)
                #came_from[next] = current
    # return came_from, cost_so_far
    return cost_so_far

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

# def longest_slide_down(pyramid_data):
#     pyramid = Pyramid(pyramid_data)
#     start = (0, 0)
#     goal = (pyramid.height - 1, pyramid.height - 1)
#     # came_from, cost_so_far = a_star_search(pyramid, start, goal)
#     cost_so_far = a_star_search(pyramid, start, goal)
#     return (cost_so_far[min(cost_so_far, key=cost_so_far.get)]) * -1

def longest_slide_down(pyramid):
    lowest_level = pyramid.pop()
    while pyramid:
        prior_level = pyramid.pop()
        lowest_level = [prior_level[brick] + max(lowest_level[brick],lowest_level[brick+1])  for brick in range(len(prior_level))] 
    return lowest_level.pop()

pyramid2 = longest_slide_down([
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
    ])

print(pyramid2)
6
# pyramid = get_pyramid([
#     [3],
#     [7, 4],
#     [2, 4, 6],
#     [8, 5, 9, 3]
#     ])

# start = (0, 0)
# goal = (pyramid.height - 1, pyramid.height - 1)

# print('Demo:', breadth_first_search_3.__name__)
# parents = breadth_first_search_3(pyramid, start, goal)
# print(parents)

# print('Demo - Pyramid 1:', dijkstra_search.__name__)
# came_from, cost_so_far = dijkstra_search(pyramid, start, goal)
# print(cost_so_far[min(cost_so_far, key=cost_so_far.get)])
# print(reconstruct_path(came_from, start, goal))

# print('Demo - Pyramid 1:', a_star_search.__name__)
# came_from, cost_so_far = a_star_search(pyramid, start, goal)
# print(cost_so_far[min(cost_so_far, key=cost_so_far.get)])
# print(reconstruct_path(came_from, start, goal))

# pyramid2 = get_pyramid([
#     [75],
#     [95, 64],
#     [17, 47, 82],
#     [18, 35, 87, 10],
#     [20,  4, 82, 47, 65],
#     [19,  1, 23, 75,  3, 34],
#     [88,  2, 77, 73,  7, 63, 67],
#     [99, 65,  4, 28,  6, 16, 70, 92],
#     [41, 41, 26, 56, 83, 40, 80, 70, 33],
#     [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
#     [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
#     [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
#     [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
#     [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
#     [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
#     ])

# start2 = (0, 0)
# goal2 = (pyramid2.height - 1, pyramid2.height - 1)

# print('Demo - Pyramid 2:', dijkstra_search.__name__)
# came_from, cost_so_far = dijkstra_search(pyramid2, start2, goal2)
# print(cost_so_far[min(cost_so_far, key=cost_so_far.get)])
# print(reconstruct_path(came_from, start2, goal2))

# print('Demo - Pyramid 2:', a_star_search.__name__)
# came_from, cost_so_far = a_star_search(pyramid2, start2, goal2)
# print(cost_so_far[min(cost_so_far, key=cost_so_far.get)])
# print(reconstruct_path(came_from, start2, goal2))

# pyramid2 = [
#     [75],
#     [95, 64],
#     [17, 47, 82],
#     [18, 35, 87, 10],
#     [20,  4, 82, 47, 65],
#     [19,  1, 23, 75,  3, 34],
#     [88,  2, 77, 73,  7, 63, 67],
#     [99, 65,  4, 28,  6, 16, 70, 92],
#     [41, 41, 26, 56, 83, 40, 80, 70, 33],
#     [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
#     [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
#     [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
#     [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
#     [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
#     [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
#     ]

# print(longest_slide_down(pyramid2))


# def next_level_down(pyramid, levelidx, valueidx):
#     current_value = pyramid[levelidx][valueidx]
#     if levelidx == len(pyramid) - 1:
#         maximum_value = current_value
#     else:
#         maximum_value = current_value + max(next_level_down(pyramid, levelidx + 1, valueidx), next_level_down(pyramid, levelidx + 1, valueidx + 1))
#     return maximum_value

# print breadth_first([
#     [3],
#     [7, 4],
#     [2, 4, 6],
#     [8, 5, 9, 3]
#     ])

# print longest_slide_down([
#     [3],
#     [7, 4],
#     [2, 4, 6],
#     [8, 5, 9, 3]
#     ])

# print longest_slide_down([
#     [75],
#     [95, 64],
#     [17, 47, 82],
#     [18, 35, 87, 10],
#     [20,  4, 82, 47, 65],
#     [19,  1, 23, 75,  3, 34],
#     [88,  2, 77, 73,  7, 63, 67],
#     [99, 65,  4, 28,  6, 16, 70, 92],
#     [41, 41, 26, 56, 83, 40, 80, 70, 33],
#     [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
#     [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
#     [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
#     [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
#     [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
#     [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
#     ])


    
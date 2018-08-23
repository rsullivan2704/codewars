def tower_builder(n_floors):
    tower = []
    block = '*'
    floor = block * (n_floors + (n_floors - 1))
    tower.append(floor)
    current_floor = n_floors - 1
    while current_floor > 0:
        floor = block * (current_floor + (current_floor - 1))
        floor = floor.ljust(len(floor) + (n_floors - current_floor), ' ')
        floor = floor.rjust(len(floor) + (n_floors - current_floor), ' ')
        tower.insert(0, floor)
        current_floor -= 1
    return tower

print(tower_builder(6))


[
    '     *     ', 
    '    ***    ', 
    '   *****   ', 
    '  *******  ', 
    ' ********* ', 
    '***********'
    ]
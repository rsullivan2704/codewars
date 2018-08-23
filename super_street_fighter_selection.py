import test

move_vals = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def get_new_pos(current_pos, move):
    current_y, current_x = current_pos
    move_y, move_x = move_vals[move]
    new_y, new_x = current_y + move_y, current_x + move_x
    return (new_y, new_x)

def move_up(fighters, current_pos):
    current_y, current_x = current_pos
    new_y, new_x = get_new_pos(current_pos, 'up')
    if new_y < 0 or fighters[new_y][new_x] == '':
        return fighters[current_y][current_x], current_pos
    return fighters[new_y][new_x], (new_y, new_x)
    

def move_down(fighters, current_pos):
    current_y, current_x = current_pos
    new_y, new_x = get_new_pos(current_pos, 'down')
    if new_y > len(fighters) - 1 or fighters[new_y][new_x] == '':
        return fighters[current_y][current_x], current_pos
    return fighters[new_y][new_x], (new_y, new_x)

def move_left(fighters, current_pos):
    new_y, new_x = get_new_pos(current_pos, 'left')
    if new_x < 0:
        new_x = len(fighters[new_y]) - 1
    while fighters[new_y][new_x] == '':
        new_x -= 1
        if new_x < 0:
            new_x = len(fighters[new_y]) - 1
    return fighters[new_y][new_x], (new_y, new_x)

def move_right(fighters, current_pos):
    new_y, new_x = get_new_pos(current_pos, 'right')
    if new_x > len(fighters[new_y]) - 1:
        new_x = 0
    while fighters[new_y][new_x] == '':
        new_x += 1
        if new_x > len(fighters[new_y]) - 1:
            new_x = 0
    return fighters[new_y][new_x], (new_y, new_x)

move_funcs = {
    'up': move_up,
    'down': move_down,
    'left': move_left,
    'right': move_right
}

def super_street_fighter_selection(fighters, position, moves):
    if not moves:
        return []
    results = []
    new_pos = position
    for move in moves:
        fighter, new_pos = move_funcs[move](fighters, new_pos)
        results.append(fighter)
    return results

fighters = [
	[       "",    "Ryu",  "E.Honda",  "Blanka",   "Guile", ""       ],
	[ "Balrog",    "Ken",  "Chun Li", "Zangief", "Dhalsim", "Sagat"  ],
	[   "Vega", "T.Hawk", "Fei Long",  "Deejay",   "Cammy", "M.Bison"]
]

#test.it("should stop on empty spaces vertically")
moves =  ["up"]*4
position = (1,0)
solution = ['Balrog']*4
print(super_street_fighter_selection(fighters,position, moves))

# test.it("should stop vertically")

# fighters = [
# 	[       "",    "Ryu",  "E.Honda",  "Blanka",   "Guile", ""       ],
# 	[ "Balrog",    "Ken",  "Chun Li", "Zangief", "Dhalsim", "Sagat"  ],
# 	[   "Vega", "T.Hawk", "Fei Long",  "Deejay",   "Cammy", "M.Bison"]
# ]

# moves =  ["up"]*4
# position = (1,5)
# # solution = ['Sagat']*4
# print(super_street_fighter_selection(fighters,position, moves))

# moves =  ["right"]*8
# position = (0,2)
# # solution = ['Blanka', 'Guile', 'Ryu', 'E.Honda', 'Blanka', 'Guile', 'Ryu', 'E.Honda']
# print(super_street_fighter_selection(fighters,position, moves))

# moves =  ["down"]*4
# position = (1,0)
# # solution = ['Vega']*4
# print(super_street_fighter_selection(fighters, position, moves))

# moves =  []
# position = (0,0)
# print(super_street_fighter_selection(fighters,position, moves))

# moves =  ["up"]
# position = (1,0)
# # solution = ['Balrog']
# print(super_street_fighter_selection(fighters,position, moves))

fighters4 = [
	[        "",     "Ryu",  "E.Honda",  "Cammy" ],
	[  "Balrog",     "Ken",  "Chun Li",       "" ],
	[    "Vega",        "", "Fei Long", "Balrog",],
    [  "Blanka",   "Guile",         "", "Chun Li"],
    [ "M.Bison", "Zangief",  "Dhalsim", "Sagat"  ],
    [  "Deejay",   "Cammy",         "", "T.Hawk" ]
]

# # test.it("should work with longer grid")
# moves =  ["left"]*2+["down"]+["right"]*4+["down"]+["left"]*4+["down"]+["right"]*2+["down"]+["right"]*3+["down"]+["left"]*3+["down"]+["left"]*3
# position = (0,3)
# # solution = ['E.Honda', 'Ryu', 'Ken', 'Chun Li', 'Balrog', 'Ken', 'Chun Li', 'Fei Long', 'Vega', 'Balrog', 'Fei Long', 'Vega', 'Blanka', 'Guile', 'Chun Li', 'Sagat', 'M.Bison', 'Zangief', 'Dhalsim', 'Dhalsim', 'Zangief', 'M.Bison', 'Sagat', 'T.Hawk', 'Cammy', 'Deejay', 'T.Hawk']
# print(super_street_fighter_selection(fighters4,position, moves))

# test.it("should work with odd initial position")
moves =  ["left"]*2+["down"]+["right"]*4+["down"]+["left"]*4+["up"]+["right"]*2+["up"]+["right"]*3
position = (3,3)
solution = ['Guile', 'Blanka', 'M.Bison', 'Zangief', 'Dhalsim', 'Sagat', 'M.Bison', 'Deejay', 'T.Hawk', 'Cammy', 'Deejay', 'T.Hawk', 'Sagat', 'M.Bison', 'Zangief', 'Guile', 'Chun Li', 'Blanka', 'Guile']
print(super_street_fighter_selection(fighters4,position, moves))
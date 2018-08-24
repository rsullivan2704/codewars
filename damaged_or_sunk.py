
def damaged_or_sunk(board, attacks):
  ships = {}
  hits = {}
  for row_index, row in enumerate(board[::-1]):
    for col_index, col in enumerate(row):
      if col > 0:
        position = (col_index + 1, row_index + 1)
        position_list = [col_index + 1, row_index + 1]
        if col not in ships:
          ships[col] = [position]
        else:
          ships[col].append(position)
        if position_list in attacks:
          if col not in hits:
            hits[col] = [position]
          else:
            hits[col].append(position)

  sunk = {ship: pos for ship, pos in ships.items() for hit_ship, hit_pos in hits.items() if ship in hits and ships[ship] == hits[ship]}

  ship_count = len(ships)
  sunk_count = len(sunk)
  damaged = len(hits) - sunk_count
  not_touched = ship_count - len(hits)
  points = (1 * sunk_count) + (.5 * damaged) + (-1 * not_touched)
      
  return { 'sunk': sunk_count, 'damaged': damaged , 'not_touched': not_touched, 'points': points }

board = [[0,0,0,2,2,0],
         [0,3,0,0,0,0],
         [0,3,0,1,0,0],
         [0,3,0,1,0,0]]
attacks = [[2, 1], [1, 3], [4, 2]]
result = damaged_or_sunk(board, attacks)
print(result)

board = [ [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 0] ]

attacks = [[3, 1], [3, 2], [3, 3]]
result = damaged_or_sunk(board, attacks)
# test.it("Game 1 result: { 'sunk': 1, 'damaged': 0 , 'not_touched': 0, 'points': 1}")
# test.assert_equals(result['sunk'], 1)
# test.assert_equals(result['damaged'], 0)
# test.assert_equals(result['not_touched'], 0)
# test.assert_equals(result['points'], 1)
print(result)

board = [ [3, 0, 1],
          [3, 0, 1],
          [0, 2, 1], 
          [0, 2, 0] ]

attacks = [[2, 1], [2, 2], [ 3, 2], [3, 3]]
result = damaged_or_sunk(board, attacks)
# test.it("Game 2 result: { 'sunk': 1, 'damaged': 1 , 'not_touched': 1, 'points': 0.5}")
# test.assert_equals(result['sunk'], 1)
# test.assert_equals(result['damaged'], 1)
# test.assert_equals(result['not_touched'], 1)
# test.assert_equals(result['points'], 0.5)
print(result)


def damaged_or_sunk(board, attacks):
  ship_positions = {(col_index + 1, row_index + 1): col for row_index, row in enumerate(board[::-1]) for col_index, col in enumerate(row) if col > 0}
  hit_positions = {hit_position: hit_ship for attack in attacks for hit_position, hit_ship in ship_positions.items() if (attack[0], attack[1]) == hit_position}
  ships = {}
  hits = {}
  for position, ship_number in ship_positions.items():
      if ship_number not in ships:
          ships[ship_number] = [position]
      else:
          ships[ship_number].append(position)
  for position_hit, ship_hit in hit_positions.items():
    if ship_hit not in hits:
      hits[ship_hit] = [position_hit]
    else:
      hits[ship_hit].append(position_hit)

  sunk = {ship: pos for ship, pos in ships.items() for hit_ship, hit_pos in hits.items() if ship in hits and ships[ship] == hits[ship]}

  ship_count = len(ships)
  sunk_count = len(sunk)
  damaged = len(hits) - sunk_count
  not_touched = ship_count - len(hits)
  points = (1 * sunk_count) + (.5 * damaged) + (-1 * not_touched)


  # print(ships)
  # print(hits)
      
  return { 'sunk': sunk_count, 'damaged': damaged , 'not_touched': not_touched, 'points': points }

# board = [[0,0,0,2,2,0],
#          [0,3,0,0,0,0],
#          [0,3,0,1,0,0],
#          [0,3,0,1,0,0]]
# attacks = [[2, 1], [1, 3], [4, 2]]
# print(damaged_or_sunk(board, attacks))

# board = [ [0, 0, 1, 0],
#           [0, 0, 1, 0],
#           [0, 0, 1, 0] ]

# attacks = [[3, 1], [3, 2], [3, 3]]
# result = damaged_or_sunk(board, attacks)
# # test.it("Game 1 result: { 'sunk': 1, 'damaged': 0 , 'not_touched': 0, 'points': 1}")
# # test.assert_equals(result['sunk'], 1)
# # test.assert_equals(result['damaged'], 0)
# # test.assert_equals(result['not_touched'], 0)
# # test.assert_equals(result['points'], 1)
# print(result)

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

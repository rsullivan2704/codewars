# def openOrSenior(data):
#     results = []
#     for member in data:
#         if member[0] >= 55 and member[1] > 7:
#             results.append('Senior')
#         else:
#             results.append('Open')
#     return results

def openOrSenior(data):
    return ['Senior' if age >= 55 and handicap >= 8 else 'Open' for (age, handicap) in data]

openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]])
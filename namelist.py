def namelist(names):
    name_list = []
    result = ''
    for name in names:
        name_list.append(name.get('name'))
    result = ', '.join(name_list[0:len(name_list)-1])
    result += ' & ' + name_list[-1]

namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])

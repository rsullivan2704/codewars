def find_nb(m):
    numBlocks = 0
    volume = 0
    while volume < m:
        volume += (numBlocks + 1)**3
        numBlocks += 1
    if volume == m:
        return numBlocks
    else:
        return -1

find_nb(4183059834009)
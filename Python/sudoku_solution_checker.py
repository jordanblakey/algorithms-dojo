from pprint import pprint
def validSolution(board):
    cols = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],]
    err = 0

    for y, row in enumerate(board):
        for x, col in enumerate(row):
            cols[x][y] = col

    if not [x for x in board if len(set(x)) != 9]:
      print("[PASS] All rows contain values 1-9.")
    else : err += 1

    if not [x for x in cols if len(set(x)) != 9]:
      print("[PASS] All columns contain values 1-9.")
    else : err += 1

    blocks = [[],[],[],[],[],[],[],[],[]]
    for row in board[:3]: blocks[0].append(row[:3])
    for row in board[:3]: blocks[1].append(row[3:6])
    for row in board[:3]: blocks[2].append(row[6:9])
    for row in board[3:6]: blocks[3].append(row[:3])
    for row in board[3:6]: blocks[4].append(row[3:6])
    for row in board[3:6]: blocks[5].append(row[6:9])
    for row in board[6:9]: blocks[6].append(row[:3])
    for row in board[6:9]: blocks[7].append(row[3:6])
    for row in board[6:9]: blocks[8].append(row[6:9])

    for block in blocks:
        if len(set([item for sublist in block for item in sublist])) == 9 : print('[PASS] Block #' + str(blocks.index(block)) + ' contains values 1-9')
        else : err += 1
        
    if err == 0 : return True
    else : return False
    
    #More Succinctly:    

    def validSolution2(board):
    blocks = [[board[x+a][y+b] for a in (0, 1, 2) for b in (0, 1, 2)] for x in (0, 3, 6) for y in (0, 3, 6)]
    return not filter(lambda x: set(x) != set(range(1, 10)), board + zip(*board) + blocks)

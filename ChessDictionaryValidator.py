

def isValidChessBoard(board):
    for k, v in board.items():
        if k[1] < 'a' or k[1] > 'h' or k[0] > '8' or k[0] < '1':
            return False
        if v[0] not in  ('w', 'b') or v[1:] not in ('pawn', 'knight', 'bishop', 'rook', 'queen', 'king'):
            return False
        
    values = list(board.values())
    if values.count('wking') != 1 or values.count('bking') != 1:
        return False
    
    else: 
        return True
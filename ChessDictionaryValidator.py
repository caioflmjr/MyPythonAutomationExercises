

def isValidChessBoard(board):
    for k, v in board.items():
        if k[0] == 'k':
            print("yes")


dic1 = {'k9': 'as'}
isValidChessBoard(dic1)
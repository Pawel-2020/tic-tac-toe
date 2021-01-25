import os

board = [[1,2,3],[4,5,6],[7,8,9]]
marker = 'X'
bloked = []

def show():
    print('')
    for i in board:
        print(i)
    print('')
def move():
    while True:
        try:
            move=int(input('move '))
            break
        except:
            print('type number: 1-9\n')
    global bloked
    while move in range(1,10):
        if move not in bloked:
            if move == 1:
                board[0][0]=marker
                bloked.append(move)
                break
            elif move == 2:
                board[0][1]=marker
                bloked.append(move)
                break
            elif move == 3:
                board[0][2]=marker
                bloked.append(move)
                break
            elif move == 4:
                board[1][0]=marker
                bloked.append(move)
                break
            elif move == 5:
                board[1][1]=marker
                bloked.append(move)
                break
            elif move == 6:
                board[1][2]=marker
                bloked.append(move)
                break
            elif move == 7:
                board[2][0]=marker
                bloked.append(move)
                break
            elif move == 8:
                board[2][1]=marker
                bloked.append(move)
                break
            elif move == 9:
                board[2][2]=marker
                bloked.append(move)
                break
        else:
            print('type number: 1-9 that is not taken\n')
            while True:
                try:
                    move=int(input('move '))
                    break
                except:
                    print('type number: 1-9\n')
def switch():
    global marker
    if marker == 'X':
        marker='O'
        print('Player 2\n')
    elif marker == 'O':
        marker = 'X'
        print('Player 1\n')
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
def win():
    if board[0][0]==marker and board[0][1]==marker and board[0][2]==marker:
        return True
    elif board[1][0]==marker and board[1][1]==marker and board[1][2]==marker:
        return True
    elif board[2][0]==marker and board[2][1]==marker and board[2][2]==marker:
        return True
    elif board[0][0]==marker and board[1][0]==marker and board[2][0]==marker:
        return True
    elif board[0][1]==marker and board[1][1]==marker and board[2][1]==marker:
        return True
    elif board[0][2]==marker and board[1][2]==marker and board[2][2]==marker:
        return True
    elif board[0][0]==marker and board[1][1]==marker and board[2][2]==marker:
        return True
    elif board[0][2]==marker and board[1][1]==marker and board[2][0]==marker:
        return True
    else:
        return False
def tie():
    tie = False
    for i in range(1,10):
        
        if i in board[0] or i in board[1] or i in board[2]:
            tie = False
            break
        else:
            tie = True
    return tie  
def game():
    print('Player 1\n')
    while True:
        show()
        move()
        clear()
        if win() is True:
            show()
            print('YOU WON!!!')
            break
        if tie() is True:
            show()
            print("It's a TIE")
            break
        switch()
      
game()
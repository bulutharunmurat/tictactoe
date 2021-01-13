import random

def init_game(board):
    print('\n')
    print("Welcome to tictactoe game!")
    board.append([' ', ' ', ' '])
    board.append([' ', ' ', ' '])
    board.append([' ', ' ', ' '])
    return random.randrange(0, 2)


def print_board(board):
    print('\n\n')
    print("  0  1  2")
    print("0  "+ board[0][0]+'|'+board[0][1]+'|'+board[0][2])
    print('   -----')
    print("1  "+ board[1][0]+'|'+board[1][1]+'|'+board[1][2])
    print('   -----')
    print("2  "+ board[2][0]+'|'+board[2][1]+'|'+board[2][2])
    print('\n\n')


def horizontal_run(board, symbol):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == symbol:
            return True
    return False


def vertical_run(board, symbol):
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == symbol:
            return True
    return False


def diagonal_run(board, symbol):
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True
    return False


def board_full(board):
    all_symbols = board[0]+board[1]+board[2]
    return ' ' not in all_symbols


def check_finished(board):
    if horizontal_run(board,'X') or vertical_run(board,'X') or diagonal_run(board,'X'):
        print('Player wins!!!!')
        return True
    elif horizontal_run(board,'O') or vertical_run(board,'O') or diagonal_run(board,'O'):
        print('Computer wins!!!!')
        return True
    elif board_full(board):
        print('Tie!!!!')
        return True
    return False


def move_by_player(board):
    while True:
        try:
            line = input('Player1, make your move:Coordinate that numbers seperated by comma!! ')
            x = int(line.split(",")[0].strip())
            y = int(line.split(",")[1].strip())
        except:
            print("You should Enter appropriate coordinate, Please try again! ")
            continue
        if x<3 and y<3 and board[x][y] != 'O' and board[x][y] != 'X':
            board[x][y] = 'X'
            break
        else:
            print("You should Enter appropriate coordinate, Please try again! ")


def empty_spaces(board):
    empty_cors = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                empty_cors.append((i,j))

    return empty_cors


def move_by_computer(board):
    print('Computer played!!')
    empty_cors = empty_spaces(board)
    rand = random.randrange(0, len(empty_cors))
    x = empty_cors[rand][0]
    y = empty_cors[rand][1]
    board[x][y] = 'O'


def play_tic_tac_toe():
    board = []
    count = init_game(board)
    print_board(board)
    while True:
        count = (count+1) % 2
        if count == 0:
            move_by_player(board)
            print_board(board)
        else:
            move_by_computer(board)
            print_board(board)
        
        if check_finished(board):
            break


if __name__ == '__main__':
    play_tic_tac_toe()
# create the board
my_board = [['    ', '|', '    ', '|', '    '],
            ['_ _ _ _ _ _ _ _'],
            ['    ', '|', '    ', '|', '    '],
            ['_ _ _ _ _ _ _ _'],
            ['    ', '|', '    ', '|', '    '],
]


# gets index for row/col, and converts it to fit with 'my_board' (5x5)
def get_index(location):
    while True:
        try:
            index = int(input(location))
            if 0 <= index <= 2:
                return index * 2 # multiply by 2 in order to get the correct index based on the format for my_board
            print("Must be 0-2 inclusive!")
        except ValueError:
            print("Index must be an integer")


def game_over(board):
    # check for horizontal win
    for i in range(0, 5, 2):
        if board[i][0] == board[i][2] == board[i][4] and board[i][0] != '    ':
            print_board(board)
            print(f'Horizonal streak. Player {board[i][0]} wins!')
            return True
    # check for vertical win
    for i in range(0, 5, 2):
        if board[0][i] == board[2][i] == board[4][i] and board[0][i] != '    ':
            print_board(board)
            print(f'Vertical streak. Player {board[0][i]} wins!')
            return True
    # check for diagonals
    if board[0][0] == board[2][2] == board[4][4] and board[0][0] != '    ':
        print_board(board)
        print(f'Diagonal streak. Player {board[0][0]} wins!')
        return True
    if board[0][4] == board[2][2] == board[4][0] and board[0][4] != '    ':
        print_board(board)
        print(f'Diagonal streak. Player {board[0][4]} wins!')
        return True
    # check for tie
    for i in range(0, 5, 2):
        if '    ' not in board[0] and '    ' not in board[2] and '    ' not in board[4]:
            print_board(board)
            print('Tie Game!')
            return True
    # game still on
    return False


# formats the board without commas
def print_board(board):
    for row in range(len(board)):
        print(''.join([str(col) for col in board[row]]))

# print_board(my_board)

# test out indices of board
# for row in range(0, 5, 2):
#     for col in range(5):
#         if my_board[row][col] == '    ':
#             print(f'Empty space at row: {row}, column: {col}')


# player 'X' starts first
turn = 'X'

while not game_over(my_board):
    print_board(my_board)
    print(f"It's {turn}'s turn")
    row = get_index('Row: ')
    col = get_index('Column: ')
    if my_board[row][col] == '    ':
        my_board[row][col] = f'  {turn} '
        if turn == 'X':
            turn = 'O'
        elif turn == 'O':
            turn = 'X'
    else:
        print('That spot is already taken')
        print(f"Still {turn}'s turn")




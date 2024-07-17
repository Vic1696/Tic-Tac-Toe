board = ['' for _ in range (9)]
current_player = 'X'

def print_board():
    print (f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print (f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print (f"{board[6]} | {board[7]} | {board[8]}")

def check_win():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], #Check rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Check columns
        [0, 4, 8], [2, 4, 6] #Check diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != '':
            return True
    return False
    
def check_draw():
    return '' not in board

def play_game():
    current_player = 'X'
    while True:
        print_board()
        move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
        if board[move] == '':
            board[move] = current_player
            if check_win():
                print_board()
                print(f"Player {current_player} wins!")
                break
            elif check_draw():
                print_board()
                print("It's a draw!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

play_game()
import math

# Board initialization
board = [" " for _ in range(9)]

# Display board
def print_board():
    for i in range(3):
        print("|".join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

# Check for winner
def check_winner(b, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8], # rows
        [0,3,6], [1,4,7], [2,5,8], # cols
        [0,4,8], [2,4,6]           # diagonals
    ]
    for cond in win_conditions:
        if b[cond[0]] == b[cond[1]] == b[cond[2]] == player:
            return True
    return False

# Check for draw
def is_draw():
    return " " not in board

# Minimax algorithm
def minimax(b, depth, is_maximizing):
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if is_draw():
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                score = minimax(b, depth + 1, False)
                b[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                score = minimax(b, depth + 1, True)
                b[i] = " "
                best = min(best, score)
        return best

# computer move
def computer_move():
    best_score = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

# Player move
def player_move():
    while True:
        try:
            move = int(input("Enter position (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Spot taken. Try again.")
        except:
            print("Invalid input. Enter number 1-9.")

# Main game loop
def play_game():
    print("Welcome to Tic Tac Toe! (You: X, computer: O)")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner(board, "X"):
            print("You win!")
            break
        if is_draw():
            print("It's a draw.")
            break

        print("computer is thinking...")
        computer_move()
        print_board()
        if check_winner(board, "O"):
            print("computer wins!")
            break
        if is_draw():
            print("It's a draw.")
            break

play_game()

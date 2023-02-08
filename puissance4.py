def create_board():
    board = []
    for i in range(6):
        row = []
        for j in range(7):
            row.append(" ")
        board.append(row)
    return board

def display_board(board):
    for row in board:
        print("|".join(row))
    print("-"*29)
    print("1 2 3 4 5 6 7")

def make_move(board, column, player):
    for i in range(5, -1, -1):
        if board[i][column-1] == " ":
            board[i][column-1] = player
            return board
    return False

def check_win(board, player):
    # check rows
    for row in board:
        for i in range(4):
            if row[i:i+4] == [player]*4:
                return True
    # check columns
    for col in range(7):
        for i in range(3):
            if board[i][col] == player and board[i+1][col] == player and board[i+2][col] == player and board[i+3][col] == player:
                return True
    # check diagonals
    for i in range(3):
        for j in range(4):
            if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
                return True
    for i in range(3):
        for j in range(3, 7):
            if board[i][j] == player and board[i+1][j-1] == player and board[i+2][j-2] == player and board[i+3][j-3] == player:
                return True
    return False

def puissance4():
    board = create_board()
    player = "X"
    while True:
        display_board(board)
        print("Player", player, "turn.")
        move = int(input("Choose a column (1-7): "))
        result = make_move(board, move, player)
        if not result:
            print("Column is full. Choose another one.")
            continue
        if check_win(board, player):
            display_board(board)
            print("Player", player, "wins!")
            break
        if player == "X":
            player = "O"
        else:
            player = "X"

puissance4()

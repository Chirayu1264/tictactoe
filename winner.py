# Initialize the game board
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

players = [1, 2]  # You can add more players here, e.g., [1, 2, 3]
current_player_index = 0  # Start with the first player


# Function to print the game board
def print_board(board):
    for row in board:
        print(row)


# Function to check for a win
def win(current_game):
    # Check horizontal wins
    for row in current_game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f"Player {row[0]} is the winner horizontally!")
            return True
    
    # Check diagonal (top-left to bottom-right)
    diags = [current_game[ix][ix] for ix in range(len(current_game))]
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally!")
        return True
    
    # Check diagonal (bottom-left to top-right)
    diags = [current_game[row][col] for col, row in enumerate(reversed(range(len(current_game))))]
    if diags.count(diags[0]) == len(diags) and diags[0] != 0:
        print(f"Player {diags[0]} is the winner diagonally reversed!")
        return True

    # Check vertical wins
    for col in range(len(current_game)):
        check = [row[col] for row in current_game]
        if check.count(check[0]) == len(check) and check[0] != 0:
            print(f"Player {check[0]} is the winner vertically!")
            return True
    
    return False


# Function to change the player after each move
def change_player():
    global current_player_index
    current_player_index = (current_player_index + 1) % len(players)
    return players[current_player_index]


# Function to check if the move is valid
def valid_move(row, col, board):
    if board[row][col] == 0:
        return True
    else:
        return False


# Main game loop
def play_game():
    global game
    print("Welcome to Tic-Tac-Toe!")
    print_board(game)

    moves = 0  # Count total moves to detect a draw

    while True:
        # Get the current player
        current_player = players[current_player_index]
        print(f"Player {current_player}'s turn.")
        
        # Ask for input from the current player
        row = int(input("Enter the row (0, 1, or 2): "))
        col = int(input("Enter the column (0, 1, or 2): "))

        # Check if the move is valid
        if valid_move(row, col, game):
            game[row][col] = current_player
            print_board(game)
            moves += 1
        else:
            print("Invalid move! Try again.")
            continue

        # Check for a winner
        if win(game):
            print(f"Player {current_player} wins!")
            break

        # If it's a draw
        if moves == 9:
            print("It's a draw!")
            break

        # Change to the next player
        change_player()


# Start the game
play_game()

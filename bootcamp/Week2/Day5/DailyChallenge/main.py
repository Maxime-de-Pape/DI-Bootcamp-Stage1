
board = [' '] * 9
current_player = 'X'


def display_board():
    left_display='*     '
    right_display='     *'
    intersection_display='*    ---|---|---    *'
    top_and_bottom_display='*'*21

    print(top_and_bottom_display)
    print(left_display + board[0] + ' | ' + board[1] + ' | ' + board[2] + right_display)
    print(intersection_display)
    print(left_display + board[3] + ' | ' + board[4] + ' | ' + board[5] + right_display)
    print(intersection_display)
    print(left_display + board[6] + ' | ' + board[7] + ' | ' + board[8] + right_display)

    print(top_and_bottom_display)


# Function to get the position from the player
def player_input(player):
    global current_player
    position = input(player + ", enter your position (1-9): ")
    while not position.isdigit() or int(position) < 1 or int(position) > 9 or board[int(position) - 1] != ' ':
        position = input("Invalid position. " + player + ", enter your position (1-9): ")
    return int(position) - 1


# Function to check whether there is a winner or not
def check_win():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != ' ':
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != ' ':
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True

    return False


# Function to play the game
def play():
    global current_player
    display_board()

    while True:
        position = player_input("Player " + current_player)
        board[position] = current_player
        display_board()

        if check_win():
            print("Player " + current_player + " wins!")
            break
        elif ' ' not in board:
            print("It's a tie!")
            break

        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


play()

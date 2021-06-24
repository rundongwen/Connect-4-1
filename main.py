width = 7
height = 6

board = []
for i in range(height):
    board.append([" "] * width)


def get_move():
    column = int(input("Which column do you want? (1-7) "))
    if (column > 7 or column < 1):
        print("ERROR CHARACTER OUT OF RANGE")
        column = get_move()
    column -= 1
    column_full = False
    for i in range(height):
        if board[i][column] == "O":
            column_full = True
            break
        if column_full:
            print("COLUMN IS FULL")
            column = get_move()
    return column


def make_move(col, player):
    row = 0
    for i in range(height):
        if board[i][col] == " ":
            row = i
        else:
            break
    board[row][col] = player
    return board


def draw_board(board):
    print("1,2,3,4,5,6,7")
    for i in board:
        print("|".join(i))


draw_board(board)



def check_win():
    #check Horizontal
    for row in range(width - 1):
        for col in range(height - 1):
            if board[row][col] != " ":
                if board[row][col] == board[row][col + 1] == board[row][
                        col + 2] == board[row][col + 3]:
                    return board[row][col]
    #checks Vertical
    for row in range(width - 1):
        for col in range(height - 1):
            if board[row][col] != " ":
                if board[row][col] == board[row - 1][col] == board[
                        row - 2][col] == board[row - 3][col]:
                    return board[row][col]
    #checks Diagonal (top-left to bottom-right)
    for col in range(height - 3):
        for row in range(width - 3):
            if board[row][col] == board[row - 1][col + 1] == board[row - 2][
                    col + 2] == board[row - 3][col + 3]:
                return board[row][col]
    #checks Diagonal (bottom-left to top-right)
    for col in range(height - 1, height - 3):
        for row in range(width - 3):
            if board[row][col] == board[row - 1][col - 1] == board[row - 2][
                    col - 2] == board[row - 3][col - 3]:
                return board[row][col]
    #cat's game/tie
    full = True
    for col in range(height):
        for row in range(width):
            if board[col][row] == " ":
                full = False
                break

    if full:
        return "Cat"


def main():
    winner = " "
    player = "O"

    while winner == " ":
        col = get_move()
        board2 = make_move(col, player)
        if player == "O":
          player = "X"
        elif player == "X":
          player = "O"
        draw_board(board2)
        winner = check_win()
        print(check_win())
    if winner == "Cat":
        print("It's a Tie!")
    else:
        print("{} is the winner".format(winner))


main()

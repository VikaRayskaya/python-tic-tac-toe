import random


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("_" * 10)


def check_winner(board, player):
    # check row
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # check column
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # check diagonal
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False


def get_empty_cells(board):
    res = list()
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                res.append((row, col))
    return res


# choose who to start
def coin_toss():
    return random.choice(["user", "computer"])


def computer_move(board, user_char):
    # choose computer move
    empty_cells = get_empty_cells(board)

    # Try to win or not to loose
    for cell in empty_cells:
        for player in ["O", user_char]:
            board[cell[0]][cell[1]] = player
            if check_winner(board, player):
                return
            board[cell[0]][cell[1]] = " "

    # random
    move = random.choice(empty_cells)
    board[move[0]][move[1]] = "O"


def main():
    # init board
    board = [[" "] * 3 for _ in range(3)]
    user_char = "X"

    first_player = coin_toss()
    print(f"{first_player.capitalize()} goes first.")

    while True:
        print_board(board)

        if first_player == "user":
            print("User's turn:")
            row = int(input("Enter row number (0-2): "))
            col = int(input("Enter column number (0-2): "))
            if board[row][col] == " ":
                board[row][col] = user_char
                if check_winner(board, user_char):
                    print_board(board)
                    print("User wins!")
                    break
                first_player = "computer"

        if first_player == "computer":
            print("Computer is thinking...")
            computer_move(board, user_char)
            if check_winner(board, "O"):
                print_board(board)
                print("Computer wins!")
                break
            first_player = "user"


if __name__ == "__main__":
    main()
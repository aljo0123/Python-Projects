def display_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(board):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_combinations:
        a, b, c = combo
        if board[a] == board[b] == board[c] != " ":
            return True

    return False


while True:
    board = [" "] * 9

    player_x = input("Enter Player 1 name (X): ")
    player_o = input("Enter Player 2 name (O): ")

    current_player = "X"
    moves = 0

    print("\nPositions:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")

    while True:
        display_board(board)

        if current_player == "X":
            player_name = player_x
        else:
            player_name = player_o

        try:
            position = int(input(f"{player_name}, choose a position (1-9): "))

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")
                continue

            if board[position - 1] != " ":
                print("That position is already taken.")
                continue

            board[position - 1] = current_player
            moves += 1

            if check_winner(board):
                display_board(board)
                print(f"🎉 {player_name} wins!")
                break

            if moves == 9:
                display_board(board)
                print("🤝 It's a draw!")
                break

            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

        except ValueError:
            print("Please enter a valid number.")

    again = input("\nDo you want to play again? (yes/no): ")

    if again.lower() != "yes":
        print("Thanks for playing!")
        break
def game_status(board):
    for i in range(3):
        if board[i][0] != ' ' and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0] + ' wins'

        if board[0][i] != ' ' and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i] + ' wins'
        
    if board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0] + ' wins'

    if board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2] + ' wins'

    for row in board:
        if " " in row:
            return "In progress"
    return "Draw"


# Bonus Version (includes validation for impossible board states)
def game_status_bonus(board: list) -> str:
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == "X":
                x_count += 1
            elif cell == "O":
                o_count += 1

    # Check if X and O counts differ by more than 1
    if abs(x_count - o_count) > 1:
        return "Invalid"

    winners = set()

    for i in range(3):
        if board[i][0] != " " and board[i][0] == board[i][1] == board[i][2]:
            winners.add(board[i][0])
        if board[0][i] != " " and board[0][i] == board[1][i] == board[2][i]:
            winners.add(board[0][i])

    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        winners.add(board[0][0])

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        winners.add(board[0][2])

    # Both players cannot win in a valid game
    if len(winners) > 1:
        return "Invalid"

    if "X" in winners:
        return "X wins"
    if "O" in winners:
        return "O wins"

    for row in board:
        if " " in row:
            return "In progress"

    return "Draw"


# --- Testing ---
# Prompt examples
print(game_status([["X", "X", "X"],
                   ["O", "O", " "],
                   [" ", " ", " "]]))  # "X wins"

print(game_status([["O", "X", "X"],
                   ["X", "O", " "],
                   [" ", " ", "O"]]))  # "O wins"

print(game_status([["X", "O", "X"],
                   ["O", "X", "O"],
                   ["O", "X", "O"]]))  # "Draw"

print(game_status([["X", " ", " "],
                   [" ", "O", " "],
                   [" ", " ", " "]]))  # "In progress"

# Required extra tests: empty board, last row win, and last column win
empty_board = [[" ", " ", " "],
               [" ", " ", " "],
               [" ", " ", " "]]
print("Empty board:", game_status(empty_board))  # "In progress"

last_row_win = [["O", "X", " "],
                ["O", " ", " "],
                ["X", "X", "X"]]
print("Last row win:", game_status(last_row_win))  # "X wins"

last_col_win = [["X", " ", "O"],
                ["X", " ", "O"],
                [" ", "X", "O"]]
print("Last col win:", game_status(last_col_win))  # "O wins"




# Prompt examples
assert game_status([["X", "X", "X"],
                    ["O", "O", " "],
                    [" ", " ", " "]]) == "X wins"

assert game_status([["O", "X", "X"],
                    ["X", "O", " "],
                    [" ", " ", "O"]]) == "O wins"

assert game_status([["X", "O", "X"],
                    ["O", "X", "O"],
                    ["O", "X", "O"]]) == "Draw"

assert game_status([["X", " ", " "],
                    [" ", "O", " "],
                    [" ", " ", " "]]) == "In progress"

# Required extra test cases
assert game_status([[" ", " ", " "],
                    [" ", " ", " "],
                    [" ", " ", " "]]) == "In progress"  # Empty board

assert game_status([["O", "X", " "],
                    ["O", " ", " "],
                    ["X", "X", "X"]]) == "X wins"       # Last row win

assert game_status([["X", " ", "O"],
                    ["X", " ", "O"],
                    [" ", "X", "O"]]) == "O wins"       # Last column win

print("All C6 tests passed!")


# Bonus tests
assert game_status_bonus([["X", "X", "X"],
                          ["O", "O", "O"],
                          [" ", " ", " "]]) == "Invalid"  # Both win

assert game_status_bonus([["X", "X", "X"],
                          [" ", " ", " "],
                          [" ", " ", " "]]) == "Invalid"  # 3 X's, 0 O's




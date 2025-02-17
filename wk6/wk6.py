board_size = 10

# TODO : 1. Initialize a board_sizexboard_size game board with all cells set to 0 (empty) 
# # Add you code of TODO 1 here
board = []
for i in range(board_size):
    board_row = []
    for j in range(board_size):
        board_row.append(0)
    board.append(board_row)


# TODO : 2.While loop to repeatedly ask for valid attack coordinates 
# # Add you code of TODO 2 here
is_attacking = True
while is_attacking:
    x = int(input(f"Enter attack row (0-{board_size-1}): "))
    y = int(input(f"Enter attack column (0-{board_size-1}): "))

    if x < 0 or x >= board_size or y < 0 or y >= board_size:
        is_valid = False
    else:
        is_valid = True
    print(f"Coordinates {(x, y)} are valid: {is_valid}")

    if is_valid:
        # break the loop
        is_attacking = False
    else:
        print("Please enter again.")

# Set the cell to 1 to indicate a successful attack
board[x][y] = 1


# TODO : 3. For loop to iterate through each row and column of the board 
# # Add you code of TODO 3 here
for i in range(board_size):
    for j in range(board_size):
        print(board[i][j], end=" ")
    print()
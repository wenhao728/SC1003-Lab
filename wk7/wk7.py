board_size = 10

# Get the start position for the Carrier 
print("Please enter start_position of Carrier in the following format (row,col). E.g. 6,4")
user_input_c = input("Enter coordinates: ")


# TODO : 1. Split the string at the comma and convert to a tuple of integers 
# Add you code of TODO 1 here
start_position_c = tuple(map(lambda s: int(s.strip()), user_input_c.split(",")))

# Get the start position for the Submarine
print("Please enter start_position of Submarine in the following format (row,col). E.g. 6,4") 
user_input_s = input("Enter coordinates: ")


# TODO : 2. Split the string at the comma and convert to a tuple of integers
# Add you code of TODO 2 here
start_position_s = tuple(map(lambda s: int(s.strip()), user_input_s.split(",")))


# TODO : 3. Dictionary to store ship details (name, length, and starting coordinates)
# # Add you code of TODO 3 here
ships = {
    "Carrier": {"length": 5, "start_position": start_position_c},
    "Submarine": {"length": 3, "start_position": start_position_s}
}


# code from lab4
# # Initialize a board_size x board_size game board with all cells set to 0 (empty)
game_board = [[0] * board_size for _ in range(board_size)]


# TODO : 4.Function to place ships on the board based on their start position and length
# Add you code of TODO 4 here
def place_ship(ship_name):
    # Declare global variables explicitly if you want to modify them
    # A better approach is always using them as the function arguments and return the modified values 
    # to avoid the mis-modification of global variables
    global ships, game_board

    # Get the ship details
    ship_info = ships[ship_name]
    ship_length = ship_info["length"]
    x, y = ship_info["start_position"]

    # Check if the ship can be placed on the board
    if x < 0 or x >= board_size or y < 0 or y >= board_size:
        print(f"Invalid start position for {ship_name}")
        return
    
    # Note: ships are placed horizontally only in this exercise
    if x + ship_length > board_size:
        print(f"Cannot place {ship_name} at {x, y} horizontally with length {ship_length}")
        return
    
    # Place the ship on the board
    for i in range(ship_length):
        if game_board[x][y+i] != 0:
            print(
                f"Cannot place {ship_name} at {x, y} horizontally with length {ship_length}"
                f" due to overlap with another ship at {(x, y+i)}"
            )
        else:
            game_board[x][y+i] = 'S'

# Place the ships on the board
place_ship("Carrier") 
place_ship("Submarine")


# code from lab4
# While loop to repeatedly ask for valid attack coordinates
def get_attack_coordinates(board_size):
    while True:
        x = int(input(f"Enter attack row (0-{board_size-1}): "))
        y = int(input(f"Enter attack column (0-{board_size-1}): "))

        if x < 0 or x >= board_size or y < 0 or y >= board_size:
            is_valid = False
        else:
            is_valid = True
        print(f"Coordinates {(x, y)} are valid: {is_valid}")

        if is_valid:
            # break the loop
            return x, y
        else:
            print("Please enter again.")

x, y = get_attack_coordinates(board_size)
game_board[x][y] = 1


# code from lab4
# For loop to iterate through each row and column of the board
for row in game_board:
    print(" ".join(str(cell) for cell in row))
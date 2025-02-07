# TODO : 1. There are two players in the game. Initialize their names as string
player1: str = "Computer"
player2: str = "User"

# TODO : 2. There are two layers in the sea. Initialize the integer variable layer
layer: int = 2

# TODO : 3. The battleship board is 10 by 10 dimension. Initialize the integer variables # width and height
width: int = 10
height: int = 10

# TODO : 4. Initialize a boolean variable that will be used to indicate # whether user input is valid or not, two boolean variables hit and miss that indicate # whether the ship is hit or missed 
valid: bool = False
hit: bool = False
miss: bool = False

# TODO : 5. The ships have only two orientation, either vertical or horizontal.
# Initialize a variable as ship orientation
ori: str = 'v'

# TODO : 6. The coordinates of where to put ship or where to hit on the board have a # specific format. Create a string variable as coordinates
coor: str = 'A,4,1'

# TODO : 7. There are only two types of ships. Initialize two string variables as ship names
ship1: str = 'submarine'
ship2: str = 'carrier'

# TODO : 8. Initialize a string variable holding a welcome message that can be displayed to user 
welmes: str = "Welcome to Battleships! Hit ENTER to continue..."
input(welmes)
print(
    "Please enter coordinate of the attack center point in following this format (row,col,depth). E.g. A,4,1\n"
    "Note: depth = 0 represents the subsea layer, and depth = 1 represents the surface level."
)

# TODO : 9. Take user input for attack coordinates and display the result.
coor = input("Enter coordinates: ")
print(f"Hit at area centering {coor}")
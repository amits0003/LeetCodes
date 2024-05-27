import random

# Constants
ROWS = 5
COLS = 5
CANDY_TYPES = ['A', 'B', 'C', 'D', 'E']


# Function to initialize the game board
def initialize_board():
    return [[random.choice(CANDY_TYPES) for _ in range(COLS)] for _ in range(ROWS)]


# Function to display the game board
def display_board(board):
    for row in board:
        print(" ".join(row))
    print()


# Function to swap candies on the board
def swap_candies(board, row1, col1, row2, col2):
    board[row1][col1], board[row2][col2] = board[row2][col2], board[row1][col1]


# Function to check for matches in rows and columns
def check_matches(board):
    matches = set()

    # Check for horizontal matches
    for row in range(ROWS):
        for col in range(COLS - 2):
            if board[row][col] == board[row][col + 1] == board[row][col + 2]:
                matches.add((row, col))
                matches.add((row, col + 1))
                matches.add((row, col + 2))

    # Check for vertical matches
    for row in range(ROWS - 2):
        for col in range(COLS):
            if board[row][col] == board[row + 1][col] == board[row + 2][col]:
                matches.add((row, col))
                matches.add((row + 1, col))
                matches.add((row + 2, col))

    return matches


# Function to remove matched candies and fill the board
def remove_and_fill(board, matches):
    for row, col in matches:
        board[row][col] = ' '

    for col in range(COLS):
        empty_cells = [row for row in range(ROWS) if board[row][col] == ' ']
        for row in range(ROWS - 1, -1, -1):
            if empty_cells and row > empty_cells[0]:
                board[row][col], board[empty_cells.pop(0)][col] = board[empty_cells.pop(0)][col], board[row][col]


# Main game loop
def candy_crush():
    board = initialize_board()

    try:
        while True:
            display_board(board)

            row1 = int(input("Enter the row of the first candy to swap (0-4): "))
            col1 = int(input("Enter the column of the first candy to swap (0-4): "))
            row2 = int(input("Enter the row of the second candy to swap (0-4): "))
            col2 = int(input("Enter the column of the second candy to swap (0-4): "))

            swap_candies(board, row1, col1, row2, col2)
            matches = check_matches(board)

            if matches:
                remove_and_fill(board, matches)
                print("Match found! Board updated.")
            else:
                print("No match found. Swapping back.")
                swap_candies(board, row1, col1, row2, col2)
    except Exception as e:
        print(e)



if __name__ == "__main__":
    candy_crush()

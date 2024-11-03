def print_board(board):
    """Print the Sudoku board in a readable format."""
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
                
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def find_empty(board):
    """Find an empty cell in the board (represented by 0)."""
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, column
    return None

def valid(board, num, pos):
    """Check if the number is valid in the given position."""
    # Check row
    for j in range(len(board[0])):
        if board[pos[0]][j] == num and pos[1] != j:
            return False
    
    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Check 3x3 box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    
    return True

def solve(board):
    """Solve the Sudoku puzzle using backtracking."""
    empty = find_empty(board)
    if not empty:
        return True
    
    row, col = empty
    
    for num in range(1, 10):
        if valid(board, num, (row, col)):
            board[row][col] = num
            
            if solve(board):
                return True
            
            board[row][col] = 0
    
    return False

# Example usage
if __name__ == "__main__":
    # 0 represents empty cells
    puzzle = [
        [4, 0, 0, 0, 0, 8, 0, 0, 2],
        [0, 0, 0, 7, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 1, 0, 7, 0],
        [0, 1, 0, 5, 0, 6, 0, 0, 0],
        [6, 0, 0, 0, 0, 4, 0, 9, 0],
        [0, 5, 0, 0, 0, 0, 8, 0, 0],
        [3, 4, 0, 0, 0, 2, 0, 0, 1],
        [8, 0, 0, 0, 3, 0, 0, 0, 6],
        [0, 2, 0, 8, 1, 0, 0, 0, 0]
    ]
    
    print("Original Sudoku puzzle:")
    print_board(puzzle)
    print("\nSolving...\n")
    
    if solve(puzzle):
        print("Solved Sudoku:")
        print_board(puzzle)
    else:
        print("No solution exists.")

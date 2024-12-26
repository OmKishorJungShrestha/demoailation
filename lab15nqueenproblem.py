#lab15:N queen problem
def is_safe(board, row, col, N):
    # Check left side in the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower-left diagonal
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, N):
    # If all queens are placed, return True
    if col >= N:
        return True

    # Try placing the queen in all rows of the current column
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1  # Place the queen
            
            # Recurse for the next column
            if solve_n_queens_util(board, col + 1, N):
                return True

            board[i][col] = 0  # Backtrack

    return False

def solve_n_queens(N):
    # Initialize the board
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    if not solve_n_queens_util(board, 0, N):
        print("Solution does not exist.")
        return

    # Print the solution
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()

# Input from the user
N = int(input("Enter the value of N for the N-Queen problem: "))
solve_n_queens(N)





def is_safe(board, row, col, N):
    # Check left side in the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower-left diagonal
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, N):
    # If all queens are placed, return True
    if col >= N:
        return True

    # Try placing the queen in all rows of the current column
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1  # Place the queen
            
            # Recurse for the next column
            if solve_n_queens_util(board, col + 1, N):
                return True

            board[i][col] = 0  # Backtrack

    return False

def solve_n_queens(N):
    # Initialize the board
    board = [[0 for _ in range(N)] for _ in range(N)]
    
    if not solve_n_queens_util(board, 0, N):
        print("Solution does not exist.")
        return

    # Print the solution
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()

# Input from the user
N = int(input("Enter the value of N for the N-Queen problem: "))
solve_n_queens(N)




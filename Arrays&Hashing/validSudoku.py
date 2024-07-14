
def isValidSudoku(board: list[list[str]]) -> bool:
    cnt = 0
    
    for row in range(9):
        rows = board[row]
        open_rows = ''.join(sorted(''.join(rows).replace('.', '')))
        open_rows_set = ''.join(sorted(set(open_rows)))
        if open_rows == open_rows_set:
            cnt += 1
        else:
            return False

    for col in range(0, len(board[0])):
        cols = [row[col] for row in board]
        open_cols = ''.join(sorted(''.join(cols).replace('.', '')))
        open_cols_set = ''.join(sorted(set(open_cols)))
        if open_cols == open_cols_set:
            cnt += 1
        else:
            return False

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subGrid = board[row][col:col+3] + board[row+1][col:col+3] + board[row+2][col:col+3]
            open_grid = ''.join(sorted(''.join(subGrid).replace('.', '')))
            open_cols_set = ''.join(sorted(set(open_grid)))
            if open_grid == open_cols_set:
                cnt += 1
                if cnt == 27:
                    return True
            else:
                return False

print(isValidSudoku([[".",".",".",".","5",".",".","1","."],
                     [".","4",".","3",".",".",".",".","."],
                     [".",".",".",".",".","3",".",".","1"],
                     ["8",".",".",".",".",".",".","2","."],
                     [".",".","2",".","7",".",".",".","."],
                     [".","1","5",".",".",".",".",".","."],
                     [".",".",".",".",".","2",".",".","."],
                     [".","2",".","9",".",".",".",".","."],
                     [".",".","4",".",".",".",".",".","."]])) # Output -> False




# print(isValidSudoku([["5","3",".",".","7",".",".",".","."]
                    # ,["6",".",".","1","9","5",".",".","."]
                    # ,[".","9","8",".",".",".",".","6","."]
                    # ,["8",".",".",".","6",".",".",".","3"]
                    # ,["4",".",".","8",".","3",".",".","1"]
                    # ,["7",".",".",".","2",".",".",".","6"]
                    # ,[".","6",".",".",".",".","2","8","."]
                    # ,[".",".",".","4","1","9",".",".","5"]
                    # ,[".",".",".",".","8",".",".","7","9"]])) # Output -> True

# print(isValidSudoku([["8","3",".",".","7",".",".",".","."]
                    # ,["6",".",".","1","9","5",".",".","."]
                    # ,[".","9","8",".",".",".",".","6","."]
                    # ,["8",".",".",".","6",".",".",".","3"]
                    # ,["4",".",".","8",".","3",".",".","1"]
                    # ,["7",".",".",".","2",".",".",".","6"]
                    # ,[".","6",".",".",".",".","2","8","."]
                    # ,[".",".",".","4","1","9",".",".","5"]
                    # ,[".",".",".",".","8",".",".","7","9"]])) # Output -> False

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS = len(board),len(board[0])

       ##Do dfs, make a set to count consecutive Os, in the set keep track of their positions.
       # if its 4 change it to X's 
       #Also need a visit set so we dont keep going over same cells

        def dfs(r,c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O"):
                    return 
            board[r][c] = "T"      
            #The 4 directions
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and
                    (r in [0,ROWS - 1] or c in [0,COLS-1])):
                    dfs(r,c) 

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        



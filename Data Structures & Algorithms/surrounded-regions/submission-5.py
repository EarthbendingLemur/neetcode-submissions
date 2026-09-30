class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        # Find all bordering O's

        border_O = set()

        for c in range(COLS):
            if board[0][c] == "O":
                border_O.add((0, c))
            if board[ROWS - 1][c] == "O":
                border_O.add((ROWS - 1, c))
        
        for r in range(ROWS):
            if board[r][0] == "O":
                border_O.add((r, 0))
            if board[r][COLS - 1] == "O":
                border_O.add((r, COLS - 1))
        

        safe = set()
        def dfs(root_r, root_c):
            nonlocal safe
            stack = [(root_r, root_c)]
            safe.add((root_r, root_c))
            dx = [(0, 1), (0, -1), (-1, 0), (1, 0)]
            while stack:
                r, c = stack.pop()

                for dr, dc in dx:
                    row = dr + r
                    col = dc + c
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        board[row][col] != "O" or (row, col) in safe):
                        continue
                    stack.append((row, col))
                    safe.add((row, col))
        

        for r, c in border_O:
            dfs(r, c)
        
        print(safe)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in safe and board[r][c] == "O":
                    board[r][c] = "X"
        






        
        
    
        
                


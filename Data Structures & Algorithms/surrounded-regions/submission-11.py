class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        non_surrounded = set()

        def DFS(root_r, root_c):
            stack = [(root_r, root_c)]
            while stack:
                r, c = stack.pop()
                if (r, c) in non_surrounded:
                    continue
                
                non_surrounded.add((r, c))
                for dr, dc in dx:
                    row, col = dr + r, dc + c
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        (row, col) in non_surrounded or
                        board[row][col] != "O"):
                        continue
                    stack.append((row, col))
        
        for c in range(COLS):
            if board[0][c] == "O" and (0, c) not in non_surrounded:
                DFS(0, c)
            if board[ROWS - 1][c] == "O" and (ROWS - 1, c) not in non_surrounded:
                DFS(ROWS - 1, c)
        for r in range(ROWS):
            if board[r][0] == "O" and (r, 0) not in non_surrounded:
                DFS(r, 0)
            if board[r][COLS - 1] == "O" and (r, COLS - 1) not in non_surrounded:
                DFS(r, COLS - 1)
        


        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in non_surrounded and board[r][c] == "O":
                    board[r][c] = "X"





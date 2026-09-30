class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])

        def BFS_mark(root_r: int, root_c: int):
            q = deque()
            q.append((root_r, root_c))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        board[row][col] != 'O'):
                        continue
                    board[row][col] = '-'
                    q.append((row, col))

        starts = set()
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS - 1) and board[r][c] == 'O' or ((c == 0 or c == COLS - 1) and board[r][c] == 'O'):
                    board[r][c] = '-'
                    starts.add((r, c))
        
        
        for start_r, start_c in starts:
            BFS_mark(start_r, start_c)
        
        # Surround O's and remark remaining O's
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '-':
                    board[r][c] = 'O'

        
    
        
                


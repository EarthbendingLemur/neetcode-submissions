class Solution:
    def solve(self, board: List[List[str]]) -> None:
        non_surrounded = set()

        ROWS, COLS = len(board), len(board[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        for c in range(COLS):
            if board[0][c] == "O":
                non_surrounded.add((0, c))
                q.append((0, c))
            if board[ROWS - 1][c] == "O":
                non_surrounded.add((ROWS - 1, c))
                q.append((ROWS - 1, c))
        for r in range(ROWS):
            if board[r][0] == "O":
                non_surrounded.add((r, 0))
                q.append((r, 0))
            if board[r][COLS - 1] == "O":
                non_surrounded.add((r, COLS - 1))
                q.append((r, COLS - 1))

    
        while q:
            row, col = q.popleft()

            for dr, dc in dx:
                r, c = row + dr, col + dc
                if (r < 0 or r == ROWS or
                    c < 0 or c == COLS or
                    (r, c) in non_surrounded or
                    board[r][c] != "O"):
                    continue
                q.append((r, c))
                non_surrounded.add((r, c))
        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in non_surrounded:
                    board[r][c] = "X"
        


        
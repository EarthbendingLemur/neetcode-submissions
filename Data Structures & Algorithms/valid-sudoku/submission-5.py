class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}
        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            rows[r] = set()
            for c in range(COLS):
                cols[c] = set()

                squares[(r // 3, c // 3)] = set()

        for r in range(ROWS):
            for c in range(ROWS):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                
                if board[r][c] in squares[(r // 3, c // 3)]:
                    return False
                squares[(r // 3, c // 3)].add(board[r][c])


        return True


                

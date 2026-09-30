class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        seenRows = defaultdict(set)
        seenCols = defaultdict(set)
        seenSquares = defaultdict(set)

        for i in range(ROWS):
            seenRows[i] = set()
            seenCols[i] = set()

            for j in range(COLS):
                seenSquares[(i // 3, j // 3)] = set()


        for r in range(ROWS):
            for c in range(COLS):
                
                if board[r][c] == ".":
                    continue
                # Check Rows
                # Check Cols
                # Check Squares
                if (board[r][c] in seenRows[r] or 
                    board[r][c] in seenCols[c] or
                    board[r][c] in seenSquares[(r // 3, c // 3)]):
                    return False
                # Add if valid
                seenRows[r].add(board[r][c])
                seenCols[c].add(board[r][c])
                seenSquares[(r // 3, c // 3)].add(board[r][c])
                
        return True
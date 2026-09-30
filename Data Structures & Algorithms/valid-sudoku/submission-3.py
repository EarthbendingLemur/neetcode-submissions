class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows, cols = len(board), len(board[0])
        seenRows = defaultdict(set)
        seenCols = defaultdict(set)
        seenSquares = defaultdict(set)

        for i in range(rows):
            seenRows[i] = set()
            seenCols[i] = set()
            for j in range(cols):
                seenSquares[(i // 3 , j // 3)] = set()
        

        print(seenSquares)
        

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == '.': continue

                if board[r][c] not in seenRows[r]:
                    seenRows[r].add(board[r][c])
                else:
                    return False
                
                if board[r][c] not in seenCols[c]:
                    seenCols[c].add(board[r][c])
                else:
                    return False
                
                if board[r][c] not in seenSquares[(r//3, c//3)]:
                    seenSquares[(r//3, c//3)].add(board[r][c])
                else:
                    return False

        return True
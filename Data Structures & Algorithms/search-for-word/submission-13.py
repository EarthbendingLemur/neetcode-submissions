class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(board), len(board[0])


        def backtrack(r, c, word_idx, visited):
            # Out  of bounds or in visited path
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS or
                (r, c) in visited):
                return False

            # Word index mismatch
            if board[r][c] != word[word_idx]:
                return False

            # Found the word
            if word_idx == len(word) - 1:
                return True
            visited.add((r, c))
            for dr, dc in dx:
                nr, nc = dr + r, dc + c
                if backtrack(nr, nc, word_idx + 1, visited):
                    return True
            visited.remove((r, c))
            


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0, set()):
                        return True
        

        return False
        

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def backtrack(r, c, word_idx, visited):
            # Bound Check
            if (r < 0 or r == ROWS or
                c < 0 or c == COLS):
                return False
            if (r, c) in visited:
                return False
            # Word doesn't match
            if word_idx >= len(word) or word[word_idx] != board[r][c]:
                return False
            if word_idx == len(word) - 1:
                return True
            visited.add((r, c))
            # here the word matches so we 'backtrack/dfs' to neighbours
            for dr, dc in dx:
                nr, nc = dr + r, dc + c
                if backtrack(nr, nc, word_idx + 1, visited):
                    return True
            visited.remove((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, 0, set()):
                    return True
        
        return False

        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        ROWS, COLS = len(board), len(board[0])

        def backtrack(word_idx, r, c, visited):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited:
                return False
            if word[word_idx] != board[r][c]: return False

            if word_idx == len(word) - 1: return True
            visited.add((r, c))
            for dr, dc in dx:
                nr, nc = dr + r, dc + c
                if (backtrack(word_idx + 1, nr, nc, visited)): return True
            visited.remove((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if backtrack(0, r, c, set()):
                        return True
        return False   
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col, word_idx, visited):
            if (row < 0 or row == ROWS or 
                col < 0 or col == COLS or
                (row, col) in visited):
                return False
            
            if word_idx == len(word) or word[word_idx] != board[row][col]:
                return False
            if word_idx == len(word) - 1:
                return True
            visited.add((row, col))
            for dr, dc in dx:
                r, c = dr + row, dc + col
                if dfs(r, c, word_idx + 1, visited):
                    return True
            visited.remove((row, col))

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True
        
        return False





        

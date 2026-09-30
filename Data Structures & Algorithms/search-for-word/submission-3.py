class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
    

        def backtrack(word_idx, r, c, visited):
            # Already visited
            if (r, c) in visited:
                return False
            # mismatch
            if board[r][c] != word[word_idx]:
                return False
            # Found word
            if word_idx == len(word) - 1:
                return True
            
            visited.add((r, c))
            for dr, dc in dx:
                row, col = dr + r, dc + c
                if (row < 0 or row == len(board) or
                    col < 0 or col == len(board[0])):
                    continue
                if backtrack(word_idx + 1, row, col, visited):
                    return True
            visited.remove((r, c))
            return False
                
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(0, r, c, set()):
                    return True


        return False
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
    

        def backtrack(word_idx, r, c, visited):
            # Bound check
            if r < 0 or r == len(board) or c < 0 or c == len(board[0]):
                return False
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
                if backtrack(word_idx + 1, dr + r, dc + c, visited):
                    return True
            visited.remove((r, c))
            return False
                
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(0, r, c, set()):
                    return True


        return False
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        dx = [(0,1), (0,-1), (1,0), (-1,0)]
        ROWS, COLS = len(grid), len(grid[0])
        res = 0


        def dfs(r, c, visited, gold):

            if (r < 0 or r == ROWS or c < 0 or c == COLS or 
            (r, c) in visited or grid[r][c] == 0): return gold

            visited.add((r, c))
            gold += grid[r][c]
            best = gold
            for dr, dc in dx:
                nr, nc = dr + r, dc + c
                best = max(best, dfs(nr, nc, visited, gold))
            visited.remove((r, c))
            return best
            
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] != 0:
                    res = max(dfs(r, c, set(), 0), res)
                   

        return res






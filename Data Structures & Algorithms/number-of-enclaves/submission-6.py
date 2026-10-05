class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = 0
        visited = set()
        def BFS(sr, sc):
            q = deque()
            q.append((sr, sc))
            visited.add((sr, sc))
            isEnclave = True
            sze = 0
            while q:
                r, c = q.popleft()
                sze += 1

                for dr, dc in dx:
                    nr, nc = dr + r, dc + c
                    if (nr < 0 or nr == ROWS or nc < 0 or nc == COLS or
                        grid[nr][nc] != 1 or (nr, nc) in visited): continue
                    
                    if nr == 0 or nr == ROWS - 1 or nc == 0 or nc == COLS - 1:
                        isEnclave = False
                    q.append((nr, nc))
                    visited.add((nr ,nc))
                
            return isEnclave, sze

        

        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if grid[r][c] == 1 and (r, c) not in visited:
                    isEnclave, sze = BFS(r, c)
                    if isEnclave:
                        res += sze
            
        return res
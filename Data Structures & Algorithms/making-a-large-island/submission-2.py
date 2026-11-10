from collections import deque
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        islands = {}
        ROWS, COLS = len(grid), len(grid[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def BFS(sr, sc, _id):
            q = deque()
            q.append((sr, sc))
            sz = 0
            grid[sr][sc] = _id
            while q:
                r, c = q.popleft()
                sz += 1

                for dr, dc in dx:
                    nr, nc = dr + r, dc + c
                    if (nr < 0 or nr == ROWS or
                        nc < 0 or nc == COLS or
                        grid[nr][nc] != 1):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = _id
            islands[_id] = sz
        
        _id = 'A'
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    BFS(r, c, _id)
                    _id = chr(ord(_id) + 1)
        
        res = max(islands.values()) if islands else 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    neis = set()
                    for dr, dc in dx:
                        nr, nc = dr + r, dc + c
                        if (nr < 0 or nr == ROWS or
                            nc < 0 or nc == COLS or grid[nr][nc] == 0): 
                            continue
                        neis.add(grid[nr][nc])
                    
                    resulting_area = 1
                    for n in neis:
                        resulting_area += islands[n]
                    res = max(res, resulting_area)
                        

        return res

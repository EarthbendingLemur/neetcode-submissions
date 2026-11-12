from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        def BFS(source, visited, explore):
            q = deque()
            for sr, sc in source:
                q.append((sr, sc))
                visited.add((sr, sc))
            dist = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    
                    for dr, dc in dx:
                        nr, nc = dr + r, dc + c
                        if (nr < 0 or nr == ROWS or
                            nc < 0 or nc == COLS or
                            (nr, nc) in visited):
                            continue
                        if not explore and grid[nr][nc] == 0:
                            continue
                        if explore and grid[nr][nc] == 1:
                            return dist
                        q.append((nr, nc))
                        visited.add((nr, nc))
                
                dist += 1



        first_island = set()
        found_first = False
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    BFS({(r, c)}, first_island, False)
                    found_first = True
            if found_first: break
        return BFS(first_island, set(), True)

        
        
        
        
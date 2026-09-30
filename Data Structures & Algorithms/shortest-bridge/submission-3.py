class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dx = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def BFS(sr, sc, id):
            grid[sr][sc] = id
            q = deque()
            q.append((sr, sc))
            while q:
                r, c = q.popleft()
                
                for dr, dc in dx:
                    nr, nc = dr + r, dc + c
                    if (nr < 0 or nr == ROWS or
                        nc < 0 or nc == COLS or
                        grid[nr][nc] != 1):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = id
        id = 2
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    BFS(r, c, id)
                    id += 1
    

        visited = set()
        def BridgeBFS():
            q = deque()
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == 2:
                        q.append((r, c))
                        visited.add((r, c))
            dist = 0
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()

                    if grid[r][c] == 3:
                        return dist - 1

                    for dr, dc in dx:
                        nr, nc = dr + r, dc + c
                        if (nr < 0 or nr == ROWS or
                            nc < 0 or nc == COLS or
                            (nr, nc) in visited):
                            continue
                        q.append((nr, nc))
                        visited.add((nr ,nc))            
                dist += 1
            
            return float('inf')
        
        # BFS Until you hit 2 and 3 count distance
        return BridgeBFS()

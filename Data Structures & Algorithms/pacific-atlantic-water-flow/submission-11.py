from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac_sources = set()
        atl_sources = set()
        ROWS, COLS = len(heights), len(heights[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for c in range(COLS):
            pac_sources.add((0, c))
            atl_sources.add((ROWS - 1, c))
        for r in range(ROWS):
            pac_sources.add((r, 0))
            atl_sources.add((r, COLS - 1))
        
        def BFS(sources):
            q = deque()
            for r, c in sources:
                q.append((r, c))
            while q:
                r, c = q.popleft()

                for dr, dc in dx:
                    nr, nc = dr + r, dc + c
                    if (nr < 0 or nr == ROWS or
                        nc < 0 or nc == COLS or
                        (nr, nc) in sources or heights[nr][nc] < heights[r][c]):
                        continue
                    q.append((nr, nc))
                    sources.add((nr, nc))
        

        BFS(pac_sources)
        BFS(atl_sources)
        res = []
        for r, c in pac_sources:
            if (r, c) in atl_sources:
                res.append([r, c])
        
        return res

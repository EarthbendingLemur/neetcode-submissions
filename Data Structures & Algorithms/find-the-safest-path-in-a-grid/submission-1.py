from collections import deque
import heapq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[0] * COLS for _ in range(ROWS)]
        q = deque()
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    q.append((r, c, 0))
                    visited.add((r, c))
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            r, c, d = q.popleft()
            dp[r][c] = d

            for dr, dc in dx:
                nr, nc = dr + r, dc + c
                if (nr < 0 or nr == ROWS or 
                    nc < 0 or nc == COLS or
                    (nr, nc) in visited):
                    continue
                q.append((nr, nc, d + 1))
                visited.add((nr, nc))
        
        for r in dp:
            print(*r)
        hp = [(-dp[0][0], 0, 0)]
        visited = {(0, 0)}
        res = float('inf')
        while hp:
            val, r, c = heapq.heappop(hp)
            res = min(res, -val)
            if r == ROWS - 1 and c == COLS - 1:
                break

            for dr, dc in dx:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nr == ROWS or 
                    nc < 0 or nc == COLS or
                    (nr, nc) in visited):
                    continue
                heapq.heappush(hp, (-dp[nr][nc], nr, nc))
                visited.add((nr , nc))
        return res

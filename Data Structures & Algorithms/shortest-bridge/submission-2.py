class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # Find One island
        # Expand BFS from that island keeping track of distance
        # When we reach second island, return distance required
        # Use visited set for first island

        ROWS, COLS = len(grid), len(grid[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        def BFS(coords, explore):
            q = deque()
            res = float('inf')
            for row, col in coords:
                q.append((row, col, 0))
                visited.add((row, col))
            while q:
                r, c, dist = q.popleft()
                for dr, dc in dx:
                    nr, nc = dr + r, dc + c
                    # Bound check + visited set check
                    if (nr < 0 or nr == ROWS or
                        nc < 0 or nc == COLS or
                        (nr, nc) in visited):
                        continue
                    # If we are just exploring the island not scouting for the second to build a bridge
                    if explore and grid[nr][nc] == 0:
                        continue
                    # We arrive at "1" that is not a part of the first island but it is also not in visited
                    if not explore and grid[nr][nc] == 1:
                        res = min(dist + 1, res)
                    visited.add((nr, nc))
                    q.append((nr, nc, dist + 1))
            return res if not explore else None
        

        island_explored = False
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    BFS({(r, c)}, True)
                    island_explored = True
                    break
            if island_explored:
                break
        
        first_island = visited.copy()
        shortest_bridge = BFS(first_island, False)


        return shortest_bridge - 1 if shortest_bridge != float('inf') else -1



        
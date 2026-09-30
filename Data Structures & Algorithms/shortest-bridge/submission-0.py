class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # DFS to get all coordinates of first island and mark them
        # BFS from all marked islands till we hit land
        # record distance
        ROWS, COLS = len(grid), len(grid[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dfs_start = [-1, -1]
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs_start = [r, c]
                    break
        island_starts = set()
        def DFS():
            stack = [tuple(dfs_start)]
            while stack:
                row, col = stack.pop()
                if (row, col) in island_starts:
                    continue
                island_starts.add((row, col))
                for dr, dc in dx:
                    r, c = row + dr, col + dc
                    if (r < 0 or r == ROWS or
                        c < 0 or c == COLS or
                        grid[r][c] != 1 or (r, c) in island_starts):
                        continue
                    stack.append((r, c))
        
        def BFS():
            q = deque()
            res = 0
            for r, c in island_starts:
                q.append((r, c))
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    
                    for dr, dc in dx:
                        row, col = dr + r, dc + c
                        if (row < 0 or row == ROWS or
                            col < 0 or col == COLS or
                            (row, col) in island_starts):
                            continue
                        if grid[row][col] == 1:
                            return res
                        q.append((row, col))
                        island_starts.add((row, col))
                res += 1

        DFS()

        return BFS()
                




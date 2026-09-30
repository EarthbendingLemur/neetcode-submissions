class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_starts = []
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    island_starts.append((r, c))
        

        visited = set()
        islands = 0
        def DFS(root_r, root_c):
            stack = [(root_r, root_c)]
            dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            while stack:
                r, c = stack.pop()
                visited.add((r, c))
                for dr, dc in dx:
                    row = r + dr
                    col = dc + c
                    if (row < 0 or row == rows or 
                        col < 0 or col == cols or
                        grid[row][col] != "1" or 
                        (row, col) in visited):
                        continue
                    stack.append((row, col))


        for r, c in island_starts:
            if (r, c) not in visited:
                DFS(r, c)
                islands += 1
        


        return islands
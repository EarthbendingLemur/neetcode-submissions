class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = set()
        num_islands = 0

        ROWS, COLS = len(grid), len(grid[0])

        def BFS(island_root_r: int, island_root_col: int):
            q = deque()
            q.append((island_root_r, island_root_col))
            directions = [(1, 0), (-1, 0), (0, 1), (0,-1)]
            while q:
                r, c = q.popleft()
                islands.add((r, c))
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        grid[row][col] != "1" or (row, col) in islands):
                        continue
                    q.append((row, col))                           




        for r in range(ROWS):
            for c in range(COLS):
                if (grid[r][c] == "1" and (r, c) not in islands):
                    BFS(r, c)
                    num_islands += 1


        return num_islands
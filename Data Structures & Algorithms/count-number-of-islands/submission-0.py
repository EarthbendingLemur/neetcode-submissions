class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        global islands
        islands = set()
        num_islands = 0

        q = deque()

        global ROWS
        ROWS = len(grid)
        global COLS
        COLS = len(grid[0])
        def BFS(root_r: int, root_c: int):
            q = deque()
            q.append([root_r,root_c])
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        row = dr + r
                        col = dc + c
                        if (row < 0 or row == ROWS or
                            col < 0 or col == COLS or
                            grid[row][col] != "1" or
                            (row, col) in islands):
                            continue
                        islands.add((row, col))
                        q.append([row, col])


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in islands:
                    num_islands += 1
                    islands.add((r, c))
                    BFS(r, c)
        print(islands)
            

        return num_islands
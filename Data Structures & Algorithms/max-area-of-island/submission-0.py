class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # Iterate through grid
        # do bfs on island starts, keep track of area (num of new island parts discovered)
        islands = set()
        global area
        area = 0
        ROWS, COLS = len(grid), len(grid[0])
        
        def BFS(r:int , c:int) -> int:
            bfs_area = 1
            q = deque()
            q.append((r, c))
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:

                for i in range(len(q)):
                    bfs_r, bfs_c = q.popleft()
                    for dr, dc in directions:
                        row = dr + bfs_r
                        col = dc + bfs_c

                        if (row < 0 or row == ROWS or
                            col < 0 or col == COLS or 
                            grid[row][col] != 1 or 
                            (row, col) in islands):
                            continue
                        islands.add((row, col))
                        q.append((row, col))
                        bfs_area += 1     
            return bfs_area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in islands:
                    islands.add((r, c))
                    area = max(area, BFS(r, c))
        
        # return max length
        return area
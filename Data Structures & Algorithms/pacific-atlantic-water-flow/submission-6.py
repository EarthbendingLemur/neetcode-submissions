class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # DFS from every node adjacent to atlantic and pacific ocean
        # keep track in separate sets which coords reach atlantic and pacific
        # return the intersect of the sets
        ROWS, COLS = len(heights), len(heights[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        pac = set()
        atl = set()
        for c in range(COLS):
            pac.add((0, c))
            atl.add((ROWS - 1, c))
        for r in range(ROWS):
            pac.add((r, 0))
            atl.add((r, COLS - 1))
        
        def DFS(ocean_set):
            stack = list(ocean_set)
            while stack:
                r, c = stack.pop()
                for dr, dc in dx:
                    row = dr + r
                    col = dc + c
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        heights[row][col] < heights[r][c] or
                        (row, col) in ocean_set):
                        continue
                    stack.append((row, col))
                    ocean_set.add((row, col))

        DFS(pac)
        DFS(atl)
        res = []
        for r, c in pac:
            if (r, c) in atl:
                res.append([r, c])

        return res


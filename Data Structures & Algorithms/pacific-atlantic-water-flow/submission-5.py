class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        # Store all nodes that touch pacific
        pac = set()
        # Store all nodes that touch atlantic
        atl = set()
        
        def DFS(row_root, c_root, visited):
            stack = [(row_root, c_root)]
            visited.add((row_root, c_root))
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            while stack:
                r, c = stack.pop()

                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS  or
                        (row, col) in visited or
                        heights[row][col] < heights[r][c]):
                        continue
                    stack.append((row, col))
                    visited.add((row, col))

        # DFS From every Pacific node
        # DFS from every Atl node

        # Call DFS for top and bottom rows (top touches PAC, bot touches ATL)
        for c in range(COLS):
            DFS(0, c, pac)
            DFS(ROWS - 1, c, atl)
        # Call DFS for left and right cols
        for r in range(ROWS):
            DFS(r, 0, pac)
            DFS(r, COLS - 1, atl)

        # Find all nodes in pacific map that also are in atlantic map

        res = []
        for (r, c) in pac:
            if (r, c) in atl:
                res.append([r, c])
        
        return res
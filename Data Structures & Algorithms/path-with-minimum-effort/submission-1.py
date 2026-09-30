class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        dx = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        minheap = [(0, 0, 0)] # diff, row, col
        visited = set()
        while minheap:
            diff, r, c = heapq.heappop(minheap)
            # If node visited already
            if (r, c) in visited:
                continue
            visited.add((r, c))
            # Reached Target
            if (r == ROWS - 1 and c == COLS - 1):
                return diff
            
            for dr, dc in dx:
                row, col = dr + r, dc + c
                if (row < 0 or row == ROWS or
                    col < 0 or col == COLS or
                    (row, col) in visited):
                    continue
                # calc new diff and compare to current diff
                # max absolute difference between two cells so FAR in path
                new_diff = abs(heights[row][col] - heights[r][c])
                heapq.heappush(minheap, (max(new_diff, diff), row, col))
    

        return 0


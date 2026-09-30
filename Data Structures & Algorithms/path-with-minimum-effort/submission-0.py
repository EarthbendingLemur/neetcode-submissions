class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])

        minHeap = [(0, 0, 0)]
        visited = set()

        dx = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if (r, c) == (ROWS - 1, COLS - 1):
                return diff
            
            for dr, dc in dx:
                row = dr + r
                col = dc + c
                if (row < 0 or row == ROWS or
                    col < 0 or col == COLS or
                    (row, col) in visited):
                    continue
                new_diff = max(diff, abs(heights[r][c] - heights[row][col]))
                heapq.heappush(minHeap, (new_diff, row, col))
        
        return 0
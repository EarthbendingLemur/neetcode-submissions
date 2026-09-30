class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        dx = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        # BFS
        # store with (node, effort to get to that node)
        start = (0, (0, 0))
        hp = [start]
        # Visited set (node, effort to get to this node)
        visited = set()
        res = float('inf')
        while hp:
            effort, node = heapq.heappop(hp)
            if node in visited:
                continue
            visited.add(node)
            if (node[0] == ROWS - 1 and node[1] == COLS - 1):
                return effort
            
            for dr, dc in dx:
                row, col = dr + node[0], dc + node[1]
                if (row < 0 or row == ROWS or
                    col < 0 or col == COLS or
                    (row, col) in visited):
                    continue
                new_effort = abs(heights[row][col] - heights[node[0]][node[1]])
                heapq.heappush(hp, (max(new_effort, effort), (row, col)))
        
        return -1



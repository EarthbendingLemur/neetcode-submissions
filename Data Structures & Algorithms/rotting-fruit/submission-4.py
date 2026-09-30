class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi source BFS from every rotten orange
        ROWS, COLS = len(grid), len(grid[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = deque()
        num_fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    num_fresh += 1

        minutes = 0
        while q and num_fresh > 0:
            # Multi source BFS here            
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dx:
                    row = dr + r
                    col = dc + c
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    num_fresh -= 1
                    q.append((row, col))
            minutes += 1 
        
        return minutes if num_fresh == 0 else -1
        


                

        

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
        

        time = 0
        while q and num_fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dr, dc in dx:
                    r, c = dr + row, dc + col
                    if (r < 0 or r == ROWS or
                        c < 0 or c == COLS or
                        grid[r][c] != 1):
                        continue
                    grid[r][c] = 2
                    num_fresh -= 1
                    q.append((r, c))
            time += 1
        
        return time if num_fresh == 0 else -1


        
        


                

        

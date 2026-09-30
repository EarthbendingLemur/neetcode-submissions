class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Keep track of fresh amount
        # Take all Rottens and append to queue for BFS
        # Key note, run BFS simultaneously on all rotten ones
        # Count each outer iteration
        # Return count if fresh == 0 or -1

        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])
        minutes = 0
        q = deque()
        # Add all rotten oranges to the queue initially
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        directions = [
            (1, 0),
            (-1, 0),
            (0, -1),
            (0, 1)
        ]
        # BFS to Rot Fresh Oranges
        while fresh > 0 and q:
            # Do all rotten oranges together
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row = dr + r
                    col = dc + c
                    # Check Boundaries
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        # Check fresh status
                        grid[row][col] != 1):
                        continue
                    # At a Fresh Fruit, time to rot it
                    grid[row][col] = 2
                    q.append((row, col))
                    fresh -= 1
            print(grid)
            minutes += 1
        return minutes if fresh == 0 else -1


        





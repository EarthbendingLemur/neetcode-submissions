class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(image), len(image[0])

        start = (sr, sc)
        starting_colour = image[sr][sc]

        q = deque()
        q.append(start)
        visited = set()
        while q:
            r, c = q.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            image[r][c] = color
            for dr, dc in dx:
                row, col = dr + r, dc + c
                if (row < 0 or row == ROWS or
                    col < 0 or col == COLS or
                    image[row][col] != starting_colour):
                    continue
                q.append((row, col))
        
        return image


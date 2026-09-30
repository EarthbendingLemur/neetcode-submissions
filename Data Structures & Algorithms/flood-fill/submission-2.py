class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        

        q = deque()
        q.append((sr, sc))
        ROWS, COLS = len(image), len(image[0])
        dx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        starting_color = image[sr][sc]
        visited = set()
        visited.add((sr, sc))
        while q:
            r, c = q.popleft()  
            image[r][c] = color
            for dr, dc in dx:
                row = dr + r
                col = dc + c
                if (row < 0 or row == ROWS or col < 0 or col == COLS or image[row][col] != starting_color or (row, col) in visited): continue
                q.append((row, col))
                visited.add((row, col))


        return image


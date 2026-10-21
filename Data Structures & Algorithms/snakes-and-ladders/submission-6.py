from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(board), len(board[0])
        start = (ROWS - 1, 0)
        
        rcToVal = {}
        valToRC = {}
        flag = True
        val = 1
        for r in range(ROWS - 1, -1, -1):
            if flag:
                for c in range(COLS):
                    rcToVal[(r, c)] = val
                    valToRC[val] = (r, c)
                    val += 1
            else:
                for c in range(COLS - 1, -1, -1):
                    rcToVal[(r, c)] = val
                    valToRC[val] = (r, c)
                    val += 1
            flag = not flag
            
        end = valToRC[ROWS * COLS]
        q = deque()
        q.append(start)
        visited = set()
        visited.add(start)

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r, c) == end:
                    return res
                
                for j in range(1, 7):
                    newVal = j + rcToVal[(r, c)]

                    if newVal > ROWS * COLS:
                        continue

                    nr, nc = valToRC[newVal]
                    if board[nr][nc] != -1:
                        newVal = board[nr][nc]
                        nr, nc = valToRC[newVal]
                
                    if (nr , nc) in visited:
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
            res += 1

    
        return -1
                
            


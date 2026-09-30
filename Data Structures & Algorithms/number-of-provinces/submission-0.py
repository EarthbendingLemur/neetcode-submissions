class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        visited = set()
        def BFS(row_idx):
            visited.add(row_idx)
            q = deque()
            q.append(row_idx)
            while q:
                r = q.popleft()

                for i in range(len(isConnected[r])):
                    if isConnected[r][i] == 1 and i not in visited:
                        q.append(i)
                        visited.add(i)
            
        res = 0
        for r in range(len(isConnected)):
            if r not in visited:
                BFS(r)
                res += 1
        

        return res
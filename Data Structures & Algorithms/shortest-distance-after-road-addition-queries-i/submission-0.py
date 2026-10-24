from collections import deque
class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = {i: [i + 1] for i in range(n - 1)}
        res = []

        def processQuery(s, d):
            q = deque()
            q.append(0)
            dist = 0
            visited = set()
            visited.add(0)
            adj[s].append(d)
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    if node == n - 1:
                        return dist

                    for nei in adj[node]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
                
                dist += 1
            return -1
        for s, d in queries:
            res.append(processQuery(s, d))
        return res

        
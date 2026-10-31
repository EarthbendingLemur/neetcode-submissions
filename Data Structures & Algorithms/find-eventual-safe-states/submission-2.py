from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        outdegree = [0] * n
        rev_graph = {i:[] for i in range(n)}
        for s in range(n):
            outdegree[s] += len(graph[s])
            for d in graph[s]:
                rev_graph[d].append(s)

        res = []
        q = deque()
        for i in range(n):
            if outdegree[i] == 0:
                res.append(i)
                q.append(i)
        while q:
            node = q.popleft()

            for par in rev_graph[node]:
                outdegree[par] -= 1
                if outdegree[par] == 0:
                    q.append(par)
                    res.append(par)
        res.sort()
        return res


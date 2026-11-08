class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        
        colors = [0] * n
        for start in range(len(graph)):
            if colors[start]:
                continue
            colors[start] = 1
            q = [start]
            for node in q:
                for nei in graph[node]:

                    if colors[nei] == colors[node]:
                        return False

                    if colors[nei] == 0:
                        colors[nei] = -colors[node]
                        q.append(nei)

        return True

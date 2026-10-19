from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        def overlap(x1, y1, r, x2, y2):
            d = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
            return d <= r ** 2
        
        n = len(bombs)
        adj = defaultdict(list)
        for i in range(n):
            x1, y1, r1 = bombs[i]

            for j in range(n):
                if i == j:
                    continue
                x2, y2, r2 = bombs[j]
                if overlap(x1, y1, r1, x2, y2):
                    adj[i].append(j)
        
        
        def dfs(sr, visited):
            stack = [sr]
            visited.add(sr)
            res = 0
            while stack:
                node = stack.pop()
                res += 1
                for nei in adj[node]:
                    if nei not in visited:
                        stack.append(nei)
                        visited.add(nei)
            return res

        maxres = 0
        for i in range(n):
            maxres = max(maxres, dfs(i, set()))
        return maxres


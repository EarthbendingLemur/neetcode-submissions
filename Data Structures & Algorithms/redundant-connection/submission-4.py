class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for s, d in edges:
            n = max(s, d, n)

        par = [i for i in range(n)]
        rank = [0] * n

        def find(u):
            cur = u - 1
            while par[cur] != cur:
                cur = par[par[cur]]
            return cur

        def union(u, v):
            p1, p2 = find(u), find(v)

            if p1 == p2:
                return 1
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += 1
            else:
                par[p1] = p2
                rank[p2] += 1
            return 0
        
        for u, v in edges:
            if union(u, v):
                return [u, v]
        
        return [-1, -1]



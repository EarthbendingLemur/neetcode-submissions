class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union Find
        n = 0
        for a, b in edges:
            n = max(n, a, b)
        
        par = [i for i in range(n)]
        rank = [1] * n


        def find(n1):
            # Account for 1-indexing
            res = n1 - 1
            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += 1
            else:
                par[p2] = p1
                rank[p1] += 1
            return 1
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        return []
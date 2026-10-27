class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = {}
        for t in tiles:
            count[t] = count.get(t, 0) + 1
        res = []

        def dfs(sol):
            
            for v,f in count.items():
                if f == 0:
                    continue
                
                sol += v
                count[v] -= 1
                res.append(sol)
                dfs(sol)

                count[v] += 1
                sol = sol[:-1]

        
        dfs("")

        return len(res)

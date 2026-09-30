class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        


        def dfs(cur, par):
            time = 0
            for child in adj[cur]:
                if child == par:
                    continue
                childTime = dfs(child, cur)
                if childTime > 0 or hasApple[child]:
                    time += 2 + childTime
            
            return time


        return dfs(0, -1)
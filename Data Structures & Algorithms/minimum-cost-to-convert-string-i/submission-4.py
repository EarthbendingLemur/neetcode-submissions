from collections import defaultdict
import heapq
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        res = 0
        adj = defaultdict(list)
        for i in range(len(original)):
            adj[original[i]].append((changed[i], cost[i]))
        def cheapestPath(s, t):
            res = 0
            hp = [(0, s)]
            mp = {s:0}

            while hp:
                pth_sum, node = heapq.heappop(hp)
                if node == t:
                    return pth_sum
                for nei, w in adj[node]:
                    if nei in mp and w + pth_sum >= mp[nei]:
                        continue
                    heapq.heappush(hp, (w + pth_sum, nei))
                    mp[nei] = w + pth_sum
                    
            return -1


        cache = {}

        for i in range(len(source)):
            if (source[i], target[i]) in cache:
                res += cache[(source[i], target[i])]
                continue

            pth_cost = cheapestPath(source[i], target[i])
            if pth_cost == -1:
                return -1
            cache[(source[i], target[i])] = pth_cost
            res += pth_cost
        return res



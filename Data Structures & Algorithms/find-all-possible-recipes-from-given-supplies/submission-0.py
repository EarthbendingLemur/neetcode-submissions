from collections import deque
from collections import defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(list)
        indegree = {r:0 for r in recipes}
        for i, ings in enumerate(ingredients):
            for ingredient in ings:
                adj[ingredient].append(recipes[i])
                indegree[recipes[i]] += 1
        q = deque()
        for s in supplies:
            q.append(s)
        res = []
        while q:
            node = q.popleft()

            for par in adj[node]:
                indegree[par] -= 1
                if indegree[par] == 0:
                    res.append(par)
                    q.append(par)

    
        return res

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            adj[a].append(b)

        reachable = [set() for _ in range(numCourses)]

        def dfs(start) -> bool:
            stack = [start]
            visited = set()
            while stack:
                crs = stack.pop()
                if crs in visited:
                    continue
                visited.add(crs)
                
                for neigh in adj[crs]:
                    stack.append(neigh)
            
            reachable[start] = visited
        
        for i in range(numCourses):
            dfs(i)
            
        return [v in reachable[u] for u, v in queries]

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            adj[a].append(b)
        
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False
            
            if adj[course] == []:
                return True
            visiting.add(course)
            for prereq in adj[course]:
                if not dfs(prereq):
                    return False
                
            visiting.remove(course)
            adj[course] = []
            return True


        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
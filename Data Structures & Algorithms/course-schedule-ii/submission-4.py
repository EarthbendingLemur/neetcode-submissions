class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses

        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
            indegree[b] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        path = []
        while q:
            course = q.popleft()
            path.append(course)
        
            for neigh in adj[course]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        return path[::-1] if len(path) == numCourses else []
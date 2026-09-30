class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        indegree = [0] * numCourses

        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)
            indegree[b] += 1
        
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        numFinished = 0
        while q:
            course = q.popleft()
            numFinished += 1
        
            for neigh in adj[course]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        
        return numFinished == numCourses

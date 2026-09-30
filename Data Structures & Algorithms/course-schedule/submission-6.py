class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for crs, prereq in prerequisites:
            indegree[prereq] += 1
            adj[crs].append(prereq)
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        finished = 0
        while q:
            crs = q.popleft()
            finished += 1

            for neigh in adj[crs]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)


        return True if finished == numCourses else False
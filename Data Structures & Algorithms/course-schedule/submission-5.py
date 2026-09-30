class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj[a].append(b)
            indegree[b] += 1
        
        print(indegree)
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        finished = 0
        while q:
            node = q.popleft()
            finished += 1
            for neigh in adj[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return finished == numCourses





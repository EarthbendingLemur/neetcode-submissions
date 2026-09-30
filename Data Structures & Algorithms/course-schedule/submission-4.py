class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        indegrees = [0] * numCourses

        for src, dest in prerequisites:
            adj[src].append(dest)
            indegrees[dest] += 1
        
        q = []
        for n in range(numCourses):
            if indegrees[n] == 0:
                q.append(n)


        finished = 0
        while q:
            node = q.pop()
            finished += 1
            for neigh in adj[node]:
                indegrees[neigh] -= 1
                if indegrees[neigh] == 0:
                    q.append(neigh)

        return finished == numCourses


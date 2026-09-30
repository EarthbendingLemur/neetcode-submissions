class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegrees = [0] * numCourses

        for src, dest in prerequisites:
            adj[src].append(dest)
            indegrees[dest] += 1
        
        q = deque()
        path = []
        for n in range(numCourses):
            if indegrees[n] == 0:
                q.append(n)

        
        finished = 0
        while q:
            node = q.popleft()
            finished += 1
            path.append(node)
            endnode = node
            for neigh in adj[node]:
                indegrees[neigh] -= 1
                if indegrees[neigh] == 0:
                    q.append(neigh)


        return path[::-1] if finished == numCourses else []
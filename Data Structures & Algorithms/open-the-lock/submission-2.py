class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Can be simplified to a boolean array of 10000 elements
        visited = set()

        q = deque()
        q.append(("0000", 0))
        visited.add("0000")
        for d in deadends:
            if d == "0000": return -1
            visited.add(d)

        def findNeighs(lock):
            dx = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1), 
                (-1, 0, 0, 0), (0, -1, 0, 0), (0, 0, -1, 0), (0, 0, 0, -1)]
            
            lock_arr = [0, 0, 0, 0]
            for i in range(len(lock)):
                lock_arr[i] = int(lock[i])
            res = []
            for spin in dx:
                new_neigh = lock_arr[:]
                for i in range(len(new_neigh)):
                    if new_neigh[i] + spin[i] < 0:
                        new_neigh[i] = 9
                    elif new_neigh[i] + spin[i] == 10:
                        new_neigh[i] = 0
                    else:
                        new_neigh[i] += spin[i]
                
                neighbour = ""
                for n in new_neigh:
                    neighbour += str(n)
                if neighbour in visited:
                    continue
                res.append(neighbour)
            
            return res


        while q:
            node, steps = q.popleft()
            if node == target:
                return steps
            
            for neigh in findNeighs(node):
                q.append((neigh, steps + 1))
                visited.add(neigh)
            
        return -1
            




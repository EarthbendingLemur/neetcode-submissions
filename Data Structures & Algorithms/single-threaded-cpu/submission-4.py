class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        time = 0
        taskcpy = []
        for i, task in enumerate(tasks):
            taskcpy.append(task + [i])
        taskcpy.sort(key=lambda x:x[0])

        q = deque()
        for t in taskcpy:
            q.append(tuple(t))
        res = []    
        tmphp = []
        while len(res) < len(tasks):
            
            while q and q[0][0] <= time:
                enqtime, proctime, idx = q.popleft()
                heapq.heappush(tmphp, (proctime, idx))
            
            if tmphp:
                proctime, idx = heapq.heappop(tmphp)
                time += proctime
                res.append(idx)
            else:            
                time += 1
        
        return res
        

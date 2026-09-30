class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = defaultdict(int)
        for t in tasks:
            mp[t] += 1
        maxheap = []
        for _, v in mp.items():
            heapq.heappush(maxheap, -v)
        
        print(maxheap)
        # Put freq, time this task can next be decremented
        # into queue
        # pop from queue when time reached
        # keep track of time
        time = 0
        cpu_q = deque()
        while maxheap or cpu_q:
            time += 1
            if not maxheap:
                time = cpu_q[0][1]
            else:
                freq = 1 + heapq.heappop(maxheap)
                if freq != 0:
                    cpu_q.append((freq, time + n))
                
            if cpu_q and cpu_q[0][1] == time:
                heapq.heappush(maxheap, cpu_q.popleft()[0])
        
        return time

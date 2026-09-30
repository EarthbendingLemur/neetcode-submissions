class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = defaultdict(int)
        for t in tasks:
            mp[t] += 1
        heap = []
        for k,v in mp.items():
            heap.append(-v)
        
        heapq.heapify(heap)
        cpu_q = deque()
        time = 0
        while heap or cpu_q:
            time += 1
        
            if not heap:
                time = cpu_q[0][1]
            else:
                freq = 1 + heapq.heappop(heap)
                if freq != 0:
                    cpu_q.append((freq, time + n))
            
            if cpu_q and cpu_q[0][1] == time:
                heapq.heappush(heap, cpu_q.popleft()[0])
                
        return time
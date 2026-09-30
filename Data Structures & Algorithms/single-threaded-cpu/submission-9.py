class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        hp = []

        for i, [enq_time, proc_time] in enumerate(tasks):
            heapq.heappush(hp, (enq_time, proc_time, i))
        
        res = []
        time = 0
        potential_tasks = []
        while hp or potential_tasks:
            if hp and time < hp[0][0]:
                time = hp[0][0]

            while hp and hp[0][0] <= time:
                enq_time, proc_time, idx = heapq.heappop(hp)
                heapq.heappush(potential_tasks,(proc_time, idx))
            
            proc_time, idx = heapq.heappop(potential_tasks)
            res.append(idx)
            time += proc_time
                
        return res


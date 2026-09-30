class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t = 0
        totalTime = 0

        for start, task_time in customers:
            if t > start:
                totalTime += t - start
            else:
                t = start
            
            totalTime += task_time
            t += task_time
        
        return totalTime / len(customers)
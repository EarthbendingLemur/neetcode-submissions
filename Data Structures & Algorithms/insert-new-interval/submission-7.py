class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res_a = []
        # Add interval
        added = False
        for start, end in intervals:
            if newInterval[0] < start:
                res_a.append(newInterval)
                added = True
            res_a.append([start, end])
        if not added:
            res_a.append(newInterval)
        if not res_a:
            return [newInterval]
        # Merge 
        res = [res_a[0]]
        res_idx = 0
        for i in range(1, len(res_a)):
            if res_a[i][0] <= res[res_idx][1]:
                res[res_idx] = [res[res_idx][0], max(res[res_idx][1], res_a[i][1])]
            else:
                res.append([res_a[i][0], res_a[i][1]])
                res_idx += 1
        
        return res
    
            


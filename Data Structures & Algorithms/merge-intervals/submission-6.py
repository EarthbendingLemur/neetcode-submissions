class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])

        res = [intervals[0]]
        mp = {}
        res_idx = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[res_idx][1]:
                print(res)
                res[res_idx] = [res[res_idx][0], max(res[res_idx][1], intervals[i][1])]
            else:
                res.append([intervals[i][0], intervals[i][1]])
                res_idx += 1
        
        return res
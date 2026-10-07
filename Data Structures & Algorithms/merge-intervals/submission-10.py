class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        res_iter = 0
        for i in range(1, len(intervals)):
            prev_s, prev_e = res[res_iter][0], res[res_iter][1]
            cur_s, cur_e = intervals[i][0], intervals[i][1]

            if cur_s <= prev_e:
                res[res_iter][1] = max(prev_e, cur_e)
            else:
                res.append([cur_s, cur_e])
                res_iter += 1
        
        return res
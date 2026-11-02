class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])

        res = 1

        prevStart, prevEnd = points[0][0], points[0][1]
        for i in range(1, len(points)):
            curStart, curEnd = points[i][0], points[i][1]
            if prevEnd >= curStart:
                prevStart = curStart
                prevEnd = min(prevEnd, curEnd)
            else:
                res += 1
                prevStart, prevEnd = curStart, curEnd
        
        return res



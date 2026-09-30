class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key=lambda x:x[1])
        curCap = 0
        mh = []

        for passengers, start, end in trips:
            while mh and mh[0][0] <= start:
                curCap -= heapq.heappop(mh)[1]
            
            curCap += passengers
            if curCap > capacity:
                return False
            
            heapq.heappush(mh, (end, passengers))
            

        return True
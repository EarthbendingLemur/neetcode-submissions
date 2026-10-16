class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        pairs = []

        for i in range(len(nums1)):
            pairs.append((nums2[i], nums1[i]))
        
        pairs.sort(key=lambda x:-x[0])
        hp = []
        cur_sm = 0
        res = 0
        for p in pairs:
            cur_min = p[0]
            cur_num = p[1]
            
            heapq.heappush(hp, cur_num)
            cur_sm += cur_num
            if len(hp) > k:
                cur_sm -= heapq.heappop(hp)
            
            if len(hp) == k:
                res = max(res, cur_sm * cur_min)


        return res





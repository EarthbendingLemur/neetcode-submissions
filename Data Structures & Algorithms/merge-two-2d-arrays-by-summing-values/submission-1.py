from collections import defaultdict
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)
        mx = 0
        for _id, val in nums1:
            mp[_id] += val
            mx = max(mx, _id)
        
        for _id, val in nums2:
            mp[_id] += val
            mx = max(mx, _id)
        
        res = []
        for i in range(mx + 1):
            if i in mp:
                res.append([i, mp[i]])
            
        
        return res
        

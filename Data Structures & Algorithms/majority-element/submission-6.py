class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        res = float('-inf')

        for n in nums:
            if res != n:
                cnt -= 1
                if cnt < 0:
                    res = n
                    cnt = 0
            else:
                cnt += 1
                
    
        return res
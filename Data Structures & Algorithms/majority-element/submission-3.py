class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        res = nums[0]

        for n in nums:
            if res != n:
                cnt -= 1
                if cnt < 0:
                    res = n
            else:
                cnt += 1
        
        return res
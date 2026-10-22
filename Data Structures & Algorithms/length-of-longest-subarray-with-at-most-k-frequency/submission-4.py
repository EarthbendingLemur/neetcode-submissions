from collections import defaultdict
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        # Expand while every items freq is below k or equal to
        # Contract while an items freq exceeds k

        # Keep track of longest window which is valid

        mp = defaultdict(int)
        L = 0
        res = 0

        for R in range(len(nums)):
            mp[nums[R]] += 1
            while mp[nums[R]] > k:
                mp[nums[L]] -= 1
                if mp[nums[L]] == 0:
                    del mp[nums[L]]
                L += 1
            
            res = max(R - L + 1, res)
    
        return res



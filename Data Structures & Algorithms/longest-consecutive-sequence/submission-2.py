class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0
        for n in nums:

            if (n - 1) not in seen:
                l = 1
                while (n + 1) in seen:
                    l += 1
                    n += 1
                res = max(res, l)
        
        return res
    
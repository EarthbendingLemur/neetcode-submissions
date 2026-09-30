class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = float('inf')
        sm = 0

        while r < len(nums):
            sm += nums[r]
            while sm >= target:
                res = min(res, r - l + 1)
                sm -= nums[l]
                l += 1
            r += 1
        
        return res if res != float('inf') else 0
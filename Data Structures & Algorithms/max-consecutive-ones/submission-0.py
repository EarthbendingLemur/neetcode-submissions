class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        L, R = 0, 0
        res = 0
        while R < len(nums):
            if nums[R] == 1:
                R += 1
            else:
                res = max(res, R - L)
                L = R + 1
                R += 1
        res = max(res, R - L)
        return res
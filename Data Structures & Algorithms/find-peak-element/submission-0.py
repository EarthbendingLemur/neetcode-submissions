class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        res = 0
        L, R = 0, len(nums) - 1
        while L < R:
            m = (L + R) // 2
            if nums[m] > nums[m + 1]:
                R = m
            else:
                L = m + 1



        return L
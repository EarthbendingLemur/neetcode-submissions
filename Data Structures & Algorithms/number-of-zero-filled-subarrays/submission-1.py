class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        L = 0
        for R, n in enumerate(nums):
            if n == 0:
                res += R - L + 1
            else:
                L = R + 1
        return res
            
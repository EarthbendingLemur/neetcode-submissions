class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0

        L = 0
        curProd = 1
        for R in range(len(nums)):
            curProd *= nums[R]
            while L <= R and curProd >= k:
                curProd /= nums[L]
                L += 1

            res += R - L + 1

        return res
        
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        L, R = 0, k - 1
        res = nums[-1] - nums[0]

        while R < len(nums):
            res = min(res, nums[R] - nums[L])
            L += 1
            R += 1

        return res

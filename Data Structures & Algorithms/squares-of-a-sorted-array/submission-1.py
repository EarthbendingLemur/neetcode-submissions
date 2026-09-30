class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        L, R = 0, len(nums) - 1
        res = [0] * len(nums)
        res_idx = len(nums) - 1

        while L <= R:
            if abs(nums[L]) > abs(nums[R]):
                res[res_idx] = nums[L] ** 2
                L += 1
            else:
                res[res_idx] = nums[R] ** 2
                R -= 1
            res_idx -= 1


        return res
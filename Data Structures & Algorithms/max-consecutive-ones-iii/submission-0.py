class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        L, R = 0, 0
        res = 0
        num_zeros = 0
        while R < len(nums):
            if nums[R] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[L] == 0:
                    num_zeros -= 1
                L += 1
            
            R += 1
            res = max(res, R - L)


        return res
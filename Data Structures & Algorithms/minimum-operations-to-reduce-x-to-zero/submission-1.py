class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        val = x
        for n in nums:
            val -= n
        if val == 0:
            return len(nums)
        print(val)
        res = len(nums)
        found = False
        L = 0
        for R in range(len(nums)):
            val += nums[R]
            while L < R and val > 0:
                val -= nums[L]
                L += 1
            if val == 0:
                found = True
                res = min(res, len(nums) - (R - L + 1))

        return res if found else -1

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        res = 0
        for i in range(len(nums)):
            this_num = nums[i]
            if (this_num - 1) not in seen:
                length = 1
                while (this_num + 1) in seen:
                    length += 1
                    this_num += 1
                res = max(length, res)
            

        return res

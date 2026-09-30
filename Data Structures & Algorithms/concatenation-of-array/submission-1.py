class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [None] * len(nums) * 2

        for i in range(len(nums)):
            res[i] = nums[i]
            res[len(nums) + i] = nums[i]
        
        return res
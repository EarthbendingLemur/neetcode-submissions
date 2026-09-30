class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for num in nums:
            corr_idx = abs(num) - 1
            if nums[corr_idx] < 0:
                return abs(num)
            nums[corr_idx] *= -1
        
        return -1
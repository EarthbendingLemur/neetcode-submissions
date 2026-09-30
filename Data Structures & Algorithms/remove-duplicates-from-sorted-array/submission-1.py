class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = R = 0

        while R < len(nums):
            nums[L] = nums[R]
            while R < len(nums) and nums[R] == nums[L]:
                R += 1
            L += 1
        
        return L


            




        
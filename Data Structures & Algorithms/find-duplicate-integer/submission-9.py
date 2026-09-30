class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # mark the index 

        for n in nums:
            if nums[abs(n) - 1] < 0:
                return abs(n)
            if nums[abs(n) - 1] > 0:
                nums[abs(n) - 1] *= -1
        
        print(nums)


        return 1
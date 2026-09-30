class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = count = 0

        for i in range(len(nums)):
            if count == 0:
                ans = nums[i]
            
            count += (1 if ans == nums[i] else -1)
        
        return ans

        


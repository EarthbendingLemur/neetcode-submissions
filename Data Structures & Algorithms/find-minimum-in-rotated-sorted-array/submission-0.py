class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0] # leftmost of array starting point

        l,r = 0, len(nums) - 1

        while l <= r:

            # We're in a sorted part of the array
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return res

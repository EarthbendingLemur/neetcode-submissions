class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while l < r:
                sm = nums[l] + nums[r] + nums[i]
                if  sm == 0:
                    res.append([nums[l], nums[r], nums[i]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif sm < 0:
                    l += 1
                else:
                    r -= 1
        
        return res
        

                
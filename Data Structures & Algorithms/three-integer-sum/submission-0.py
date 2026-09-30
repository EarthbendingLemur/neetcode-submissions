class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            
            l = i + 1
            h = len(nums) - 1
            while l < h:
                threeSum = num + nums[l] + nums[h]
                if threeSum > 0:
                    h -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    sol.append([num, nums[l], nums[h]])
                    l += 1
                    while l < h and nums[l] == nums[l - 1]:
                        l += 1
    
        return sol
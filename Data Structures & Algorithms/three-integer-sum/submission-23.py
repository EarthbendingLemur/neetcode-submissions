class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #   v   l            r
        # [-4, -1, -1, 0, 1, 2]

        sol = []
        for idx,num in enumerate(nums):
            l, r = idx + 1, len(nums) - 1
            if num > 0: 
                continue
            
            if idx > 0 and num == nums[idx - 1]:
                continue

            while l < r:
                sm = num + nums[l] + nums[r]
                if sm < 0:
                    l += 1
                elif sm > 0:
                    r -= 1
                else:
                    sol.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        
        return sol





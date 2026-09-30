class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            L, R = i + 1, len(nums) - 1
            # Skip dupes
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while L < R:
                sm = nums[i] + nums[L] + nums[R]
                if sm == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    L += 1
                    while L < len(nums) and nums[L] == nums[L - 1]:
                        L += 1
                elif sm < 0:
                    L += 1
                else:
                    R -= 1
        
        return res
            
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #   v   l            r
        # [-4, -1, -1, 0, 1, 2]
        res = []
        for i in range(len(nums)):
            n1 = nums[i]
            L, R = i + 1, len(nums) - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while L < R:
                sm = nums[L] + nums[R] + n1
                if sm == 0:
                    res.append([n1, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
                elif sm < 0:
                    L += 1
                else:
                    R -= 1

        return res


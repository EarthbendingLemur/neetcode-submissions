class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()


        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                L = j + 1
                R = len(nums) - 1
                while L < R:
                    sm = nums[i] + nums[j] + nums[L] + nums[R]
                    if sm == target:
                        res.add((nums[i], nums[j], nums[L], nums[R]))
                        R -= 1
                    elif sm < target:
                        L += 1
                    else:
                        R -= 1
        
        listres = []
        for a, b, c, d in res:
            listres.append([a, b, c, d])
        return listres


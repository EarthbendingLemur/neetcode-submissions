class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmp = {}

        for ind,num in enumerate(nums):
            if num in hmp:
                return [hmp[num], ind]
            else:
                hmp[target - num] = ind
        

        
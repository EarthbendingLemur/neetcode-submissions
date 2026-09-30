class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compl = {}

        for idx,n in enumerate(nums):
            complement = target - n
            if n in compl:
                return [compl[n], idx]
            else:
                compl[complement] = idx
        return [-1,-1]
                
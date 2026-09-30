class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ref_dict = {}

        for idx, num in enumerate(nums):
            compl = target - num
            if num in ref_dict:
                return [ref_dict[num], idx]
            else:
                ref_dict[compl] = idx
        return [-1,-1]

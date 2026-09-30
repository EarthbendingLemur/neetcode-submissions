class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        t_arr = {}

        for i,num in enumerate(nums):
            if num in t_arr:
                return [t_arr[num], i]
            else:
                compl = target - num
                t_arr[compl] = i
        
        return [-1,-1]

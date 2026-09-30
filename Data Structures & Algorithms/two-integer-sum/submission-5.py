class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i,n in enumerate(nums):
            compl = target - n
            if n in mp:
                return [mp[n], i]
            mp[compl] = i
        
        return [-1, -1]
            
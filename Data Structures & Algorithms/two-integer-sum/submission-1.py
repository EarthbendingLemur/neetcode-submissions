class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}

        for i, num in enumerate(nums):
            compl = target - num
            if compl in mp:
                return [mp[compl], i]
            else:
                mp[num] = i
        
        return [-1,-1]
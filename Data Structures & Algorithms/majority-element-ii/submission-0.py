class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        import math

        count = {}

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        
        sol = []
        for k,v in count.items():
            if v > (len(nums) // 3):
                sol.append(k)

        return sol

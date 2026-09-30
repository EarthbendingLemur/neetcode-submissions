class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        L, R = len(nums) - 2, len(nums) - 1

        while R >  0:

            jumpAchieved = False
            while L >= 0 and not jumpAchieved:
                if L < 0:
                    return False
                if nums[L] >= R - L:
                    jumpAchieved = True
                    continue
                L -= 1
                
            if not jumpAchieved:
                return False
            R = L
            L -= 1
        
        return True
        


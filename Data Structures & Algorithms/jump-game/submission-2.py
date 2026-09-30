class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        
        
        R = len(nums) - 1
        L = R - 1
        cur_jump = 1
        while R > 0:

            jumpAchieved = False
            while L >= 0 and not jumpAchieved:
                if nums[L] >= cur_jump:
                    jumpAchieved = True
                    continue    
                cur_jump += 1
                L -= 1
            
            if not jumpAchieved:
                return False
            R = L
            cur_jump = 1
            L = R - 1

        return True


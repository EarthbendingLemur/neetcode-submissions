class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        
        sides = [0] * 4
        side_length = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)

        def backtrack(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]
            
            for side in range(len(sides)):
                if sides[side] + matchsticks[i] <= side_length:
                    sides[side] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[side] -= matchsticks[i]
                
                if sides[side] == 0:
                    break
            return False
        
        return backtrack(0)
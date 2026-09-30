class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        
        sides = [0] * 4
        side_length = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        def backtrack(i):
            if i == len(matchsticks):
                return True

            for s in range(len(sides)):
                if sides[s] + matchsticks[i] <= side_length:
                    sides[s] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    sides[s] -= matchsticks[i]
                
                if sides[s] == 0:
                    break
            return False
        
        return backtrack(0)

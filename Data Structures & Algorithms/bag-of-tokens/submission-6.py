class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = sorted(tokens)
        trade = len(tokens) - 1
        curPower = power
        res = 0
        i = 0
        print(tokens)
        while i <= trade:
            if curPower >= tokens[i]:
                print('scoring at ' + str(tokens[i]))
                curPower -= tokens[i]
                i += 1
                res += 1
            else:
                if res <= 0 or i == trade:
                    break
                curPower += tokens[trade]
                trade -= 1
                res -= 1
        
        return res

            

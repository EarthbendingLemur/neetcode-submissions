class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        res = float('inf')
        num_W = 0

        L, R = 0, 0
        while R < len(blocks):
            while R - L < k and R < len(blocks):
                if blocks[R] == 'W':
                    num_W += 1
                R += 1
            
            if R - L == k:
                res = min(res, num_W)

                if blocks[L] == 'W':
                    num_W -= 1
                L += 1
            
        
        return res


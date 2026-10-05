class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        L = 0
        window_len = len(cardPoints) - k
        window = 0
        for R in range(window_len):
            window += cardPoints[R]
        
        sm = sum(cardPoints)
        res = sm - window
        R = len(cardPoints) - k - 1
        while R < len(cardPoints) - 1:
            window += cardPoints[R + 1]
            window -= cardPoints[L]
            res = max(res, sm - window)
            R += 1
            L += 1
    
        return res
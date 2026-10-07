class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        L = 0
        sm = 0
        for R in range(len(cardPoints) - k):
            sm += cardPoints[R]
        total_sm = sum(cardPoints)
        res = total_sm - sm
        L = 0
        for R in range(len(cardPoints) - k, len(cardPoints)):
            sm += cardPoints[R]
            sm -= cardPoints[L]
            L += 1
            res = max(res, total_sm - sm)


        return res

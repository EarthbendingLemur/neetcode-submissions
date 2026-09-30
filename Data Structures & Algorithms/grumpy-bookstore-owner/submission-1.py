class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        minSatisfied = 0
        for i in range(len(customers)):
            minSatisfied += customers[i] if grumpy[i] == 0 else 0
        res = 0
        L, R = 0, minutes - 1
        
        while R < len(customers):
            window_sum = 0
            for i in range(L, R + 1):
                window_sum += customers[i] if grumpy[i] == 1 else 0
            res = max(minSatisfied + window_sum, res)
            L += 1
            R += 1

        return res
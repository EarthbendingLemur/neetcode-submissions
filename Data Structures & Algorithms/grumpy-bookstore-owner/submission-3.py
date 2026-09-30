class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        minSatisfied = 0
        for i in range(len(customers)):
            minSatisfied += customers[i] if grumpy[i] == 0 else 0
        res = 0
        L, R = 0, minutes - 1
        window_sum = 0
        for i in range(L, R + 1):
            window_sum += customers[i] if grumpy[i] == 1 else 0
        res = minSatisfied + window_sum
        
        while R < len(customers) - 1:
            L += 1
            if grumpy[L - 1] == 1: 
                window_sum -= customers[L - 1]
            R += 1
            if grumpy[R] == 1:
                window_sum += customers[R]
            res = max(minSatisfied + window_sum, res)
            

        return res
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = float('inf')
        min2 = float('inf')

        for p in prices:
            if p < min1:
                min1, min2 = p, min1
            elif p < min2:
                min2 = p
        
        left_over_money = money - min1 - min2
        return left_over_money if left_over_money >= 0 else money
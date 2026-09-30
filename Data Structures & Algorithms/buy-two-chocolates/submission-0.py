class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        left_over_money = money
        left_over_money -= prices[0]
        left_over_money -= prices[1]

        return left_over_money if left_over_money >= 0 else money
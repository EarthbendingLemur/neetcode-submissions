class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        self.prices.append(price)
        pricesCopy = self.prices[:]

        stack = []
        stack.append(pricesCopy.pop())
        while pricesCopy and price >= pricesCopy[-1]:
            stack.append(pricesCopy.pop())
        
        return len(stack)

        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
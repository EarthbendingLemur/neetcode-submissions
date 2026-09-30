class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import math

        gifts_hp =[-i for i in gifts]
        heapq.heapify(gifts_hp)
        for i in range(k):
            gift_taken = abs(heapq.heappop(gifts_hp))
            gift_taken = math.floor((math.sqrt(gift_taken)))
            heapq.heappush(gifts_hp, -gift_taken)
        
        gifts_hp = [-i for i in gifts_hp]

        return sum(gifts_hp)
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s_hp = []
        for s in stones:
            s_hp.append(-s)

        heapq.heapify(s_hp)

        while len(s_hp) > 1:
            s1 = heapq.heappop(s_hp)
            s2 = heapq.heappop(s_hp)
            print('s1: ' + str(s1) + ' s2: ' + str(s2))
            # Equal Stones destroy each other
            if s1 == s2:
                continue
            new_stone = -abs(s2 - s1)
            heapq.heappush(s_hp, new_stone)


        return abs(s_hp[0]) if s_hp else 0



            
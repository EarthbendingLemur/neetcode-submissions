class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        mp = defaultdict(int)
        for h in hand:
            mp[h] += 1
        
        minheap = list(mp.keys())
        heapq.heapify(minheap)
        groups = 0
        

        while groups < (len(hand) // groupSize):
            mn_val = minheap[0]
            curGroup = []
            while len(curGroup) < groupSize:
                if mn_val not in mp:
                    return False
                curGroup.append(mn_val)
                mp[mn_val] -= 1
                if mp[mn_val] == 0:
                    heapq.heappop(minheap)
                    del mp[mn_val]
                mn_val += 1
            groups += 1

        return True



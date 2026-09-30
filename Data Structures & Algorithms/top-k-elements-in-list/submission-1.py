class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Store (count, item)
        heap = []
        heapq.heapify(heap)
        mp = defaultdict(int)

        for n in nums:
            mp[n] += 1
        
        for key, v in mp.items():
            heapq.heappush(heap, (-v, key))
        
        res = []
        print(heap)
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res

        


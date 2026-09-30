class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1

        maxheap = []
        for key, v in cnt.items():
            heapq.heappush(maxheap, (-v, key))
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(maxheap)[1])
        
        return res

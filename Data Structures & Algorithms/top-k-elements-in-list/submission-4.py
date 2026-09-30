class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)

        for n in nums:
            count_map[n] += 1
        
        hp = []
        for num, count in count_map.items():
            heapq.heappush(hp, (-count, num))
        
        res = []
        while len(res) < k:
            res.append(heapq.heappop(hp)[1])
        
        return res
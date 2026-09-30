class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        for n in nums:
            counts[n] += 1
        

        hp = []
        for val, freq in counts.items():
            heapq.heappush(hp, (freq, -val))
        

        res = []

        while hp:
            freq, val = heapq.heappop(hp)
            val = -val

            for i in range(freq):
                res.append(val)
        

        return res
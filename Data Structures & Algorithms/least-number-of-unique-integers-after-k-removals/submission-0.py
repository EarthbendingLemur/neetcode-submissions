class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        for n in arr:
            freq[n] = freq.get(n, 0) + 1
        
        hp = []
        for v, f in freq.items():
            hp.append((f, v)) 
        heapq.heapify(hp)
        for _ in range(k):
            f, val = heapq.heappop(hp)
            f -= 1
            if f == 0:
                continue
            heapq.heappush(hp, (f, val))

        return len(hp)
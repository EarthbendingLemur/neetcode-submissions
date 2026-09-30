class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        heap = [(-1 * value, key) for key, value in count.items()]

        heapq.heapify(heap)
        sol = []
        for i in range(k):
            v,k = heapq.heappop(heap)
            sol.append(k)
    
        return sol
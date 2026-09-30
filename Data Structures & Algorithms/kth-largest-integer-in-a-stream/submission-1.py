class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-n for n in nums]
        heapq.heapify(self.heap)
        self.kth = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        heapCopy = self.heap.copy()

        for i in range(self.kth - 1):
            heapq.heappop(heapCopy)

        return -heapq.heappop(heapCopy)

        

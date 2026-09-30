class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # store num value, index
        hp = []

        for i, n in enumerate(nums):
            heapq.heappush(hp, (n, i))
        
        for _ in range(k):
            val, idx = heapq.heappop(hp)
            val *= multiplier
            heapq.heappush(hp, (val, idx))

        for val, idx in hp:
            nums[idx] = val
        
        return nums
            
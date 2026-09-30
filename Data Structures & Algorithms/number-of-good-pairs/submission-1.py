class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        count = defaultdict(int)
        res = 0
        for n in nums:
            res += count[n]
            count[n] += 1
        print(count)
        return res

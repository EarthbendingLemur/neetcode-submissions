class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        pref = 0
        res = 0

        for i in range(len(nums)):
            pref += nums[i]

            if (pref - k) in prefix:
                res += prefix[(pref - k)]
            prefix[pref] += 1
        
        return res
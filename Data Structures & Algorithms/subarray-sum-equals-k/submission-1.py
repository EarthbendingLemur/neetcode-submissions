class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_mp = defaultdict(int)
        prefix_mp[0] = 1
        prefix = 0
        res = 0
        for i in range(len(nums)):
            prefix += nums[i]

            if (prefix - k) in prefix_mp:
                res += prefix_mp[prefix - k]

            prefix_mp[prefix] += 1

        return res
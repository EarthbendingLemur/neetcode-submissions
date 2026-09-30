class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mp = {0 : -1}

        total = 0

        for i in range(len(nums)):
            total += nums[i]
            rem = total % k
            if rem not in mp:
                mp[rem] = i
            elif i - mp[rem] > 1:
                return True

        return False
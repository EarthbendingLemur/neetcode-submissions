class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        subarrays = []
        res = []
        L = 0
        for R in range(k - 1, len(nums)):
            subarrays.append(nums[L:R + 1])
            L += 1
        
        def isPower(arr):
            for R in range(1, len(arr)):
                if arr[R] != arr[R - 1] + 1:
                    return -1
            return arr[-1]
        
        for subarr in subarrays:
            res.append(isPower(subarr))

        return res
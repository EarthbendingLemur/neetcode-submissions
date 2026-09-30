class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        LIS = [1] * len(nums)

        # Reverse order iteration
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                # Condition for increasing subsequence
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])



        return max(LIS)
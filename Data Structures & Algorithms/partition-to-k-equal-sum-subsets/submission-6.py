class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        nums.sort(reverse=True)

        required_sm = sum(nums) / k
        used = [False] * len(nums)

        def backtrack(i, sm, num_partitions):
            if num_partitions == 0:
                return True
            
            if sm  == required_sm:
                return backtrack(0, 0, num_partitions - 1)
            
            for idx in range(i, len(nums)):
                # Choose or not choose this idx

                # Condition to skip this
                if used[idx] or sm + nums[idx] > required_sm:
                    continue
                
                used[idx] = True
                if backtrack(idx + 1, sm + nums[idx], num_partitions):
                    return True
                used[idx] = False

            return False

        
        return backtrack(0, 0, k)
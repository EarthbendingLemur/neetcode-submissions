class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            # Pivot is in right half
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        # Pivot point (index of minimum overall entry and sep two sorted halves)
        pivot = l
        
        l, r = 0, len(nums) - 1
        if (target >= nums[pivot] and target <= nums[r]):
            l = pivot
        else:
            r = pivot - 1
        
        # Binary Search
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        return -1

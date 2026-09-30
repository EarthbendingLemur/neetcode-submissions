class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()


        l, r = 0, 0


        while r < len(nums):
            if (r - l <= k):
                if nums[r] in window:
                    return True
                window.add(nums[r])
                r += 1
            else:
                window.remove(nums[l])
                l += 1


        return False
                
        
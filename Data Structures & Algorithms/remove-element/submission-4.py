class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointer here
        l, h = 0, len(nums)

        while l < h:
            if nums[l] == val:
                h -= 1
                nums[l] = nums[h]
            else:
                l += 1
        
        return h




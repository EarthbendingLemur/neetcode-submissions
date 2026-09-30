class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # last index in nums1
        i = m - 1
        # last index in nums2
        j = n - 1
        # last index available in nums1 including end 0s
        k = m + n - 1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
    
        

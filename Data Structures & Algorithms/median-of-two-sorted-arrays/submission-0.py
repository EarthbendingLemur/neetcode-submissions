class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        n1, n2 = 0, 0

        while n1 < len(nums1) and n2 < len(nums2):
            if nums1[n1] < nums2[n2]:
                merged.append(nums1[n1])
                n1 += 1
            else:
                merged.append(nums2[n2])
                n2 += 1
        
        while n1 < len(nums1):
            merged.append(nums1[n1])
            n1 += 1
        while n2 < len(nums2):
            merged.append(nums2[n2])
            n2 += 1
        

        if len(merged) % 2 == 0:
            return float(merged[(len(merged) - 1) // 2] + merged[len(merged) // 2]) / 2
        else:
            return merged[len(merged) // 2]
        
        
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = set(nums1)
        n2 = set(nums2)

        res = []
        for n in n1:
            if n in n2:
                res.append(n)

        return res
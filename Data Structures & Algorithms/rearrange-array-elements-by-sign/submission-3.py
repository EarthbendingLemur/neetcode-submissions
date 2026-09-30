class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        res = []
        pos = []
        neg = []
        for n in nums:
            if n > 0:
                pos.append(n)
            else:
                neg.append(n)
        

        pos_ptr = 0
        neg_ptr = 0

        while pos_ptr < len(pos):
            res.append(pos[pos_ptr])
            res.append(neg[neg_ptr])
            pos_ptr += 1
            neg_ptr += 1
        
        return res
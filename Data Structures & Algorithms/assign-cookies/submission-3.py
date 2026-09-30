class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        s_ptr = 0

        res = 0
        for greed in g:

            while s_ptr < len(s) and s[s_ptr] < greed:
                s_ptr += 1
            
            if s_ptr < len(s):
                s_ptr += 1
                res += 1

        return res
            



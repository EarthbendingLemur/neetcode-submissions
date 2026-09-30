class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber > 0:
            columnNumber -= 1
            offset = columnNumber % 26
            res.append(chr(ord('A') + offset))
            columnNumber //= 26

        l,r = 0, len(res) - 1

        while l < r:
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1
        
        return ''.join(res)
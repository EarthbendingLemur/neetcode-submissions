class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        num_ones = 0
        final_one = False
        for i,c in enumerate(s):
            if c == '1':
                num_ones += 1

        num_ones -= 1
        res = ""
        for i in range(len(s) - 1):
            if num_ones > 0:
                res += "1"
                num_ones -= 1
            else:
                res += "0"
            
        res += "1"

        return res

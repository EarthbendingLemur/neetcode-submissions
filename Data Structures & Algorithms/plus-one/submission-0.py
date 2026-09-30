class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        number = 0
        numdig = len(digits)
        for i in range(numdig):
            number += pow(10, (numdig - (i + 1))) * digits[i]
        
        number += 1
        str_num = str(number)
        res = []
        for c in str_num:
            res.append(int(c))


        return res
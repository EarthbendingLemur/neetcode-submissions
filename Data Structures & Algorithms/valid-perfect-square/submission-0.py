class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, h = 1, int(num / 2)

        while l < h:
            m = (l + h) // 2
            if m * m == num:
                return True
            elif m * m < num:
                l = m + 1
            else:
                h = m
        return l * l == num
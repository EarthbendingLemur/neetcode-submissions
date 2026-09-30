class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        L, R = 0, 0
        res = 0
        curSm = 0
        while R < len(arr):

            while R - L + 1 <= k:
                curSm += arr[R]
                R += 1
                
            curAvg = curSm / k
            if curAvg >= threshold:
                res += 1

            curSm -= arr[L]
            L += 1
        

        return res
        
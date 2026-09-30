class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxSoFar = -1
        res = [0]*n
        for i in range(n - 1, -1, -1):
            res[i] = maxSoFar
            maxSoFar = max(arr[i], maxSoFar)
        
        return res
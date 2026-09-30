class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inc = defaultdict(list)
        out = defaultdict(list)

        for a,b in trust:
            inc[b].append(a)
            out[a].append(b)
        
        for i in range(1, n + 1):
            if i not in out and len(inc[i]) == n - 1:
                return i
            
        return -1
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(list)
        outgoing = defaultdict(list)
        for truster, trustee in trust:
            incoming[trustee].append(truster)
            outgoing[truster].append(trustee)
        

        for i in range(1, n + 1):
            if i not in outgoing and len(incoming[i]) == n - 1:
                return i

        return -1
        


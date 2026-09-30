class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inc = defaultdict(list)
        out = defaultdict(list)

        for a, b in trust:
            out[a].append(b)
            inc[b].append(a)

        
        print(out)
        print(inc)



        for j, v in inc.items():
            if len(v) == len(out):
                return j
                


        return -1
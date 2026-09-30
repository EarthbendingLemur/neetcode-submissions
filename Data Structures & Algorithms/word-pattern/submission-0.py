class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp_p = defaultdict(int)
        mp_s = defaultdict(int)

        for c in pattern:
            mp_p[c] += 1
        s_arr = s.split(" ")
        for w in s_arr:
            mp_s[w] += 1
        
        if len(mp_s) != len(mp_p):
            return False
        
        res_p = []
        res_s = []

        for _, v in mp_p.items():
            res_p.append(v)
        for _, v in mp_s.items():
            res_s.append(v)
        
        return res_p == res_s
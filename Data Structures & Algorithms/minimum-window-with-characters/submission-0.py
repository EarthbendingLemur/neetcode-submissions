class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = defaultdict(int)
        t_mp = defaultdict(int)
        for c in t:
            t_mp[c] += 1
        if len(t) > len(s):
            return ""
        L, R = 0, 0
        have = 0
        need = len(t_mp)
        res = [-1, -1]
        resLen = float('inf')
        while R < len(s):
            c = s[R]
            window[c] += 1
            if c in t_mp and window[c] == t_mp[c]:
                have += 1
            
            while have == need:
                if (R - L + 1) < resLen:
                    res = [L, R]
                    resLen = R - L + 1
                window[s[L]] -= 1
                if s[L] in t_mp and window[s[L]] < t_mp[s[L]]:
                    have -= 1
                L += 1
            R += 1

        return s[res[0]: res[1] + 1] if resLen != float('inf') else ""



        



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_mp = defaultdict(int)
        s2_window = defaultdict(int)

        for c in s1:
            s1_mp[c] += 1
        L, R = 0, len(s1) - 1
        # construct first window
        for i in range(len(s1)):
            s2_window[s2[i]] += 1
        
        while R < len(s2):
            print(s2_window)
            if s2_window == s1_mp:
                return True
            
            s2_window[s2[L]] -= 1
            if s2_window[s2[L]] == 0:
                del s2_window[s2[L]]
            L += 1
            R += 1
            if R < len(s2):
                s2_window[s2[R]] += 1
        
        return False

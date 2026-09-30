class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_mp = defaultdict(int)
        window = defaultdict(int)
        for c in s1:
            s1_mp[c] += 1
        

        for i in range(len(s2)):
            if s2[i] not in s1_mp:
                continue
            
            # Expand window
            r = i

            while (r - i) < len(s1) and r < len(s2):
                window[s2[r]] += 1
                r += 1
            if window == s1_mp:
                return True
            else:
                window = defaultdict(int)
        

        return False
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Fixed sliding window length of len(s1)
        # Iterate over s2

        # O(N) - time
        # O(1) - space (due to lowercase chars)
        s1_mp = defaultdict(int)
        for c in  s1:
            s1_mp[c] += 1
        
        for i in range(len(s2)):
            if s2[i] not in s1_mp:
                continue
            
            # Initiate window
            l, r = i, i + len(s1)
            # boundary condition
            if r > len(s2):
                break
            window = defaultdict(int)
            while l < r:
                window[s2[l]] += 1
                l += 1
            if window == s1_mp:
                return True
        
        return False

        
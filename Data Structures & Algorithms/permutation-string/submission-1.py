class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {}
        window_count = {}

        for i in range(26):
            s1_count[i] = 0
            window_count[i] = 0
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1

        
        for i in range(len(s2) - len(s1) + 1):
            window = s2[i:i + len(s1)]
            curr_window_count = window_count.copy()
            for j in range(len(window)):
                curr_window_count[ord(s2[i + j]) - ord('a')] += 1
            
            if s1_count == curr_window_count:
                return True

        return False
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_ptr = 0

        for s_ptr in range(len(s)):
            if s[s_ptr] == t[t_ptr]:
                t_ptr += 1
                if t_ptr == len(t): return 0
        
        return len(t) - t_ptr


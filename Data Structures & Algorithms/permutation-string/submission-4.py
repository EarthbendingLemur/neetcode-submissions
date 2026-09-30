class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        def charCount(c) -> int:
            return ord(c) - ord('a')

        def checkDictZero(window) -> bool:
            for k, v in window.items():
                if v != 0:
                    return False
            return True

        if len(s1) == 1:
            return s1 in s2

        s1_count = defaultdict(int)
        for c in s1:
            s1_count[charCount(c)] += 1
        

        for i in range(len(s2)):
            if s1_count[charCount(s2[i])] == 0:
                continue
            
            # Hit a character that is in the s1 string
            window = s1_count.copy()
            l = i
            r = i + 1
            # Copy and adjust dict for correctly identified character at i
            window[charCount(s2[l])] -= 1
            # Expand window
            while r < len(s2):
                # Not a permutation
                if s1_count[charCount(s2[r])] == 0 or window[charCount(s2[r])] == 0:
                    break
                
                window[charCount(s2[r])] -= 1
                if checkDictZero(window):
                    return True
                r += 1


        return False


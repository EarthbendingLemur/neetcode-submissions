class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        rep_m = [[0] * 26 for _ in range(len(words))]

        for i in range(len(words)):
            for c in words[i]:
               rep_m[i][ord(c) - ord('a')] += 1 
        
        sms = [0 for _ in range(26)]

        for c in range(len(rep_m[0])):
            for r in range(len(rep_m)):
                sms[c] += rep_m[r][c]

        for sm in sms:
            if sm % len(words) != 0:
                return False
        return True
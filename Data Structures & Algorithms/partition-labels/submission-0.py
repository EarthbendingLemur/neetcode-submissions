class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}

        for i,c in enumerate(s):
            mp[c] = i
        
        res = []
        cur_window = set()
        L = 0
        for i in range(len(s)):
            cur_window.add(s[i])
            partitionFound = True
            for c in cur_window:
                if i < mp[c]:
                    partitionFound = False
                    break
            if partitionFound:
                res.append(i - L + 1)
                L = i + 1
                cur_window.clear()                
                
        return res
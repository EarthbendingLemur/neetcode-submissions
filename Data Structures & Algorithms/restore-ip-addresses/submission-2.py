class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        res = []

        def backtrack(idx, sol, numdots):
            # Have used every char and have 3 dots
            if numdots == 4 and idx == len(s):
                res.append(sol[:-1])
                return
            
            if numdots > 4:
                return
            # Can only put a dot if num is between 0 and 255
            # Iterate till 3 chars or end of string
            for i in range(idx, min(idx + 3, len(s))):
                potential_ip = int(s[idx: i + 1])
                if potential_ip <= 255 and (idx == i or s[idx] != "0"):
                    backtrack(i + 1, sol + s[idx: i + 1] + ".", numdots + 1)

        
        backtrack(0, "", 0)
        return res



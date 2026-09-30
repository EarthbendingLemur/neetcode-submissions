class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return []

        def backtrack(dots, sol, idx):
            if idx == len(s) and dots == 4:
                res.append(sol[:-1])
                return
            
            if dots > 4:
                return
            
            # Choose valid place to put a dot and backtrack
            for i in range(idx, len(s)):
                potential_ip = int(s[idx: i + 1])
                if potential_ip < 256 and (idx == i or s[idx] != "0"):                 
                    backtrack(dots + 1, sol + s[idx:i + 1] + ".", i + 1)


        backtrack(0, "", 0)

        return res
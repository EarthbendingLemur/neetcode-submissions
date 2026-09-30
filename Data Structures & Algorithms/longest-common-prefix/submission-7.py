class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        res_idx = 0
        min_l = len(min(strs))
        while res_idx < min_l:
            for i in range(1, len(strs)):
                if strs[i][res_idx] != strs[i - 1][res_idx]:
                    return res
            res += strs[0][res_idx]
            res_idx += 1
        
        return res

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs[0]) == 0:
            return ""

        res = ""
        ptr = 0
        for i in range(len(min(strs))):
            for j in range(len(strs)):
                if strs[j][i] != strs[j - 1][i]:
                    return res
            res += strs[j][i]
        return res
            

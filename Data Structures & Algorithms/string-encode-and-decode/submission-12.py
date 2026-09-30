class Solution:

    global sep
    sep = "#"
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + sep + s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s): 

            j = i
            while j < len(s) and s[j] != sep:
                j += 1
            length = int(s[i: j]) 
            i = j + 1
            res.append(s[i:length + i])
            i += length
        return res

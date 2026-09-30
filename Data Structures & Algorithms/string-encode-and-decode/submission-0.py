class Solution:

    def encode(self, strs: List[str]) -> str:
        out: str = ""
        for s in strs:
            out += s
            out += ";"
        return out


    def decode(self, s: str) -> List[str]:
        out: List[str] = []
        this_s : str = ""

        for c in s:
            if c != ";":
                this_s += c
            else:
                out.append(this_s)
                this_s = ""
        return out

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chr_mp = {}

        def construct_key(s) -> List[int]:
            r = [0] * 26
            for c in s:
                r[ord(c) - ord('a')] += 1
            return tuple(r)
        
        for s in strs:
            key = construct_key(s)
            if key in chr_mp:
                chr_mp[key].append(s)
            else:
                chr_mp[key] = [s]
        
        res = []
        for k, v in chr_mp.items():
            res.append(chr_mp[k])
        
        return res



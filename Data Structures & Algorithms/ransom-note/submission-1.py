class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        mag_mp = defaultdict(int)

        for c in magazine:
            mag_mp[c] += 1
        
        for c in ransomNote:
            mag_mp[c] -= 1
            if mag_mp[c] < 0:
                return False
        
        
        return True
        
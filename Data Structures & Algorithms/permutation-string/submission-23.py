class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        # O(1) space due to lowercase letters only appearing (can be strongly typed if required)
        mp = defaultdict(int)
        for c in s1:
            mp[c] += 1
        window_mp = mp.copy()
        for i in range(len(s2)):
            # Expand when perm found
            # Contract if not found
            if s2[i] in window_mp:
                l = i
                r = i
                while r < len(s2) and (r - l) < len(s1):
                    print(r)
                    if s2[r] in window_mp and window_mp[s2[r]] > 0:
                        window_mp[s2[r]] -= 1
                        r += 1
                        continue
                    window_mp = mp.copy()
                    break
                if all(v == 0 for v in window_mp.values()):
                    return True

                
        
        return False
                

                



            

        


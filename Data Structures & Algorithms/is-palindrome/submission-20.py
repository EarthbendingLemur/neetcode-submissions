class Solution:


    def isPalindrome(self, s: str) -> bool:
        import re
        letters_only = re.sub(r'[^a-zA-z0-9]', '', s)
        letters_only = letters_only.lower()
        l,r = 0, len(letters_only) - 1

        while l <= r:
            if letters_only[l] == letters_only[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True

        

        
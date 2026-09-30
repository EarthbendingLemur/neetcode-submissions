class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = re.sub('\W+','', s)

        l = 0
        r = len(str) - 1

        while l < r:
            if str[l].lower() != str[r].lower():
                return False

            l += 1
            r -= 1
        
        return True
 


        
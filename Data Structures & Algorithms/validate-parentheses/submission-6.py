class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        stk = []

        for p in s:
            # Edge case - closing bracket with no corresponding open bracket
            if not stk and p in mp:
                return False
            # Add all opening brackets to stack
            if p not in mp:
                stk.append(p)
            
            if p in mp and stk[-1] == mp[p]:
                stk.pop()
            elif p in mp and stk[-1] != mp[p]:
                return False
            
    
            
        print(stk)

        return len(stk) == 0
            
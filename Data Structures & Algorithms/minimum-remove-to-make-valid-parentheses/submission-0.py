class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        count = 0
        open_pars = []
        for i,c in enumerate(s):
            if c != ')' and c != '(':
                res.append(c)
                continue
            if c == '(':
                res.append(c)
                count += 1
                open_pars.append(i)
            elif c == ')':
                if count > 0:
                    res.append(c)
                    count -= 1
                else:
                    res.append('')
        
        print(open_pars)
        print(count)
        num_pars = len(open_pars)
        for i in range(num_pars - 1, num_pars - 1 - count, -1):
            res[open_pars[i]] = ''



        return "".join(res)

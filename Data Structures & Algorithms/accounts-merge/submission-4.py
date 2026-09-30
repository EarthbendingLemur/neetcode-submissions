class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self,n1):
        res = n1
        while res != self.par[res]:
            self.par[res] = self.par[self.par[res]]
            res = self.par[res]
        return res
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return 0
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += 1
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return 1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailToAcc = {} # Map email to account index id

        for i, emails in enumerate(accounts):
            for e in emails[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i

        emailGroup = defaultdict(list)
        for e, i in emailToAcc.items():
            leader = uf.find(i)        
            emailGroup[leader].append(e)
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroup[i]))
        

        return res
        
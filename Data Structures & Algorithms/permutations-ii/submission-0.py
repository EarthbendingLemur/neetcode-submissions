class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        def dfs():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            
            for n in count.keys():
                if count[n] > 0:
                    sol.append(n)
                    count[n] -= 1

                    dfs()
                    count[n] += 1
                    sol.pop()
        dfs()
        return res



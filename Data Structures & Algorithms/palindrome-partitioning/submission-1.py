class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(sol, idx):
            if idx >= len(s):
                res.append(sol[:])
                return
            

            for i in range(idx + 1, len(s) + 1):
                partition_str = s[idx:i]
                if partition_str[::-1] != partition_str:
                    continue
                sol.append(partition_str)
                backtrack(sol, i)
                sol.pop()
            

        backtrack([], 0)
        return res
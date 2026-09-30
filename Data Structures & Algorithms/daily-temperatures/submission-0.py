class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = [] # value [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_T, stack_I = stack.pop()
                res[stack_I] = (i - stack_I)
            stack.append([t, i])
        return res
            
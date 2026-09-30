class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = [0] * len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, idx = stack.pop()
                sol[idx] = i - idx
            stack.append((temp, i))

        return sol



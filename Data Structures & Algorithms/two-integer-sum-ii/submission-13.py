class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            sm = numbers[L] + numbers[R]
            if sm == target:
                return [L + 1, R + 1]
            elif sm < target:
                L += 1
            else:
                R -= 1
        
        return [-1, -1]
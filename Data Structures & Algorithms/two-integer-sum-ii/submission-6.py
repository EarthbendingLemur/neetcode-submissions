class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1

        while low <= high:
            two_sum = numbers[low] + numbers[high]
            if two_sum == target:
                return [low + 1, high + 1]
            elif two_sum > target:
                high -= 1
            else:
                low += 1
        
        return [-1,-1]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1

        while low <= high:
            sm = numbers[low] + numbers[high]
            if sm == target:
                return [low + 1, high + 1]
            elif sm > target:
                high -= 1
            else:
                low += 1
        
        return [-1, -1]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,h = 0, len(numbers) - 1

        while l < h:
            sm = numbers[l] + numbers[h]
            if sm < target:
                l += 1
            elif sm > target:
                h -= 1
            else:
                return [l + 1, h + 1]

        return [-1, -1]

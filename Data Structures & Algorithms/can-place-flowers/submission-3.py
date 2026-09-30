class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        new_bed = [0] + flowerbed + [0]
        num_placed = 0
        for i in range(1, len(new_bed) - 1):
            if new_bed[i - 1] == 0 and new_bed[i] == 0 and new_bed[i + 1] == 0:
                num_placed += 1
                new_bed[i] = 1
        
        return num_placed >= n


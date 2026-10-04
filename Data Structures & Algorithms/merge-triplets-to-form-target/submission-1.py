class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = second = third = False

        for f, s, t in triplets:
            if f == target[0] and s <= target[1] and t <= target[2]:
                first = True
            
            if s == target[1] and f <= target[0] and t <= target[2]:
                second = True
            
            if t == target[2] and f <= target[0] and s <= target[1]:
                third = True
            
        

        return first and second and third
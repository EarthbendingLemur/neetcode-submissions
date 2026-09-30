class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        
        pairs.sort(reverse=True)
        print(pairs)

        fleet = []

        for p, s in pairs:
            fleet.append((target - p) / s)
            if len(fleet) >= 2 and fleet[-1] <= fleet[-2]:
                fleet.pop()

        return len(fleet)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pairs = []

        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        
        pairs.sort(reverse=True)
        print(pairs)

        fleet_stack = []
        for i in range(len(pairs)):
            time_to_target = (target - pairs[i][0]) / pairs[i][1]
            if not fleet_stack or time_to_target > fleet_stack[-1]:
                fleet_stack.append(time_to_target)
            
        return len(fleet_stack)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = []

        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        # Stack to emulate fleets        
        fleets = []
        # Sort by position
        cars.sort(key=lambda x:x[0], reverse=True)

        # car[0] is pos, car[1] is speed
        # t = d / v
        for car in cars:
            time_taken = (target - car[0]) / car[1]

            if not fleets:
                fleets.append(time_taken)
                continue
            
            if time_taken > fleets[-1]:
                fleets.append(time_taken)

        print(fleets)
        return len(fleets)
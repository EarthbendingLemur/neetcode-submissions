class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        velPos = []

        for i in range(len(position)):
            velPos.append((position[i], speed[i]))
        
        velPos.sort(key=lambda x:-x[0])
        fleets = []

        for pos, speed in velPos:
            arr_time = (target - pos) / speed
            if fleets and fleets[-1] >= arr_time:
                continue
            fleets.append(arr_time)


        return len(fleets)
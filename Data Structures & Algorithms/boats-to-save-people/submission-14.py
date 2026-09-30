class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        boats = 0

        l, r = 0, len(people) - 1
        print(people)
        while l <= r:
            wght = people[l] + people[r]
            if wght > limit:
                boats += 1
                r -= 1
                continue
            boats += 1
            l += 1
            r -= 1
        return boats

        
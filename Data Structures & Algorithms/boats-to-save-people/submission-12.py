class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people) - 1
        people.sort()
        res = 0
        while l <= r:
            sm = people[l] + people[r]
            if sm <= limit:
                l += 1
            
            r -= 1
            res += 1
        
        return res

        
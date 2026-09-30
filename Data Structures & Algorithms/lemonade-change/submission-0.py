class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num_fives = 0
        num_tens = 0


        for b in bills:
            if b == 5:
                num_fives += 1
            
            if b == 10:
                num_tens += 1
            
            change = b - 5
            if change == 5:
                if num_fives > 0:
                    num_fives -= 1
                else:
                    return False
            elif change == 15:
                if num_fives > 0 and num_tens > 0:
                    num_fives, num_tens = num_fives - 1, num_tens - 1
                elif num_fives >= 3:
                    num_fives -= 3
                else:
                    return False
            
        return True

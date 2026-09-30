class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            
            # No collision
            if not stack or stack[-1] < 0 or a > 0:
                stack.append(a)
                continue
            
            incoming_destroyed = False
            while stack and stack[-1] > 0 and not incoming_destroyed:
                diff = stack[-1] - abs(a)

                if diff == 0:
                    stack.pop()
                    incoming_destroyed = True
                elif diff > 0:
                    incoming_destroyed = True
                else:
                    stack.pop()


            if not incoming_destroyed:
                stack.append(a)
        
        return stack

                

            


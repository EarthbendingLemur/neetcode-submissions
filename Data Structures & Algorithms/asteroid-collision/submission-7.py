class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
 
        for a in asteroids:
            # Collision Loop
            while stack and stack[-1] > 0 and a < 0:
                if abs(stack[-1]) > abs(a):
                    a = 0
                elif abs(stack[-1]) < abs(a):
                    stack.pop()
                else:
                    a = 0
                    stack.pop()
            
            if a != 0:
                stack.append(a) 

        return stack

                

            

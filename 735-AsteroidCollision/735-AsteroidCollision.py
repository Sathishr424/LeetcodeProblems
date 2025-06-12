# Last updated: 12/6/2025, 5:47:17 am
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if a < 0:
                a *= -1
                append = True
                while stack:
                    if stack[-1] < 0:
                        append = True
                        break
                    elif stack[-1] == a: 
                        stack.pop()
                        append = False
                        break
                    elif stack[-1] > a:
                        append = False
                        break
                    else:
                        append = True
                        stack.pop()
                if append: stack.append(-a)
            else:
                stack.append(a)
        
        return stack

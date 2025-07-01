# Last updated: 1/7/2025, 7:35:53 am
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        stack = deque([(0, 0)])

        visited = {}
        while stack:
            a, b = stack.popleft()
            if (a, b) in visited: continue

            # print(a, b)
            if a + b == target:
                return True
            
            visited[(a, b)] = 1
            stack.append((min(x, a + x), b))
            stack.append((a, min(y, b + y)))

            stack.append((0, b))
            stack.append((a, 0))
            
            a_cap = x - a
            b_cap = y - b

            stack.append((min(x, a + b), max(0, b - a_cap)))
            stack.append((max(0, a - b_cap), min(y, b + a)))
        
        return False

# Last updated: 8/5/2025, 6:13:36 pm
class Solution:
    def isFascinating(self, n: int) -> bool:
        found = [0] * 10

        def process(x):
            while x:
                found[x%10] += 1
                x //= 10
        
        process(n)
        process(n*2)
        process(n*3)

        for i in range(1, 10):
            if found[i] != 1: return False
        
        return found[0] == 0
        
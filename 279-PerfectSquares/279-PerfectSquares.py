# Last updated: 12/6/2025, 5:50:55 am
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        s = 1
        add = 3
        while s <= n:
            squares.append(s)
            s += add
            add += 2
        
        stack = [(n, 0)]
        while True:
            newStack = []
            while stack:
                total, cnt = stack.pop()
                for num in squares:
                    if total-num >= 0:
                        if total-num == 0: return cnt + 1
                        else: newStack.append((total-num, cnt+1))
            stack = newStack
            

            
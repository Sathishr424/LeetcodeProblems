# Last updated: 5/8/2025, 2:12:21 am
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def calc(x, y, op):
            if op == '+':
                return x + y
            elif op == '-':
                return x - y
            else:
                return x * y
            
        n = len(expression)
        ret = []
        
        nums = []
        ops = []
        i = 0
        while i < n:
            dig = 0
            while i < n and expression[i] not in '-+*':
                dig = dig * 10 + int(expression[i])
                i += 1
            nums.append(dig)
            if i < n:
                ops.append(expression[i])
                i += 1

        def rec(l, r):
            if l == r: return [nums[l]]
            arr = []
            for i in range(l + 1, r + 1):
                for x in rec(l, i-1):
                    for y in rec(i, r):
                        arr.append(calc(x, y, ops[i - 1]))
            return arr

        return rec(0, len(nums) - 1)
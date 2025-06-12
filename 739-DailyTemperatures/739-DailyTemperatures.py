# Last updated: 12/6/2025, 5:47:15 am
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        
        stack = []
        ret = [0] * n

        for i in range(n-1, -1, -1):
            while stack and temp[stack[-1]] <= temp[i]:
                stack.pop()
            if len(stack) > 0:
                ret[i] = stack[-1] - i
            stack.append(i)
        
        return ret

                

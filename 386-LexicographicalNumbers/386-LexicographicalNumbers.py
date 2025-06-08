# Last updated: 8/6/2025, 7:47:25 pm
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ret = []
        # 1, 10, 100, 101, 102, 103, 104, ... 109
        # 1, 10, 100, 101, 102, 110

        # 10, 100, 1000, 

        # 1000, 1009, 1010, 11
        # 1

        ret = []
        num = 1
        stack = []
        used = []
        total_used = 0
        while num <= n:
            stack.append(num)
            used.append(0)
            ret.append(num)
            num *= 10
        
        def checkSmaller(x,  y):
            x = str(x)
            y = str(y)

            for i in range(min(len(x), len(y))):
                if x[i] < y[i]: return True
                elif y[i] < x[i]: return False
            
            return x[i] < y[i]

        for i in range(len(stack)):
            stack[i] += 1
            if stack[i] > min(n, 10**(i+1) - 1):
                used[i] = 1
                total_used += 1
        
        m = len(stack)
        while total_used < len(stack):
            smaller = 0
            for i in range(m):
                if used[i] == 0:
                    smaller = i
                    break;
            
            for i in range(1, m):
                if used[i] == 0 and checkSmaller(stack[i], stack[smaller]):
                    smaller = i
            
            ret.append(stack[smaller])
            # print(stack, smaller, ret[-5:])
            stack[smaller] += 1
            

            if stack[smaller] > min(n, 10**(smaller+1) - 1):
                used[smaller] = 1
                total_used += 1
        
        return ret


            
            
# Last updated: 23/9/2025, 3:30:55 am
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        
        def isGood(k):
            stack = deque([])
            s = 0
            for i in range(k):
                s += runningCosts[i]

                while stack and chargeTimes[stack[-1]] < chargeTimes[i]:
                    stack.pop()
                
                stack.append(i)

            max_charge = chargeTimes[stack[0]]
            total_cost = max_charge + k * s

            if total_cost <= budget: return True
            
            for i in range(k, n):
                s -= runningCosts[i - k]
                s += runningCosts[i]
                
                while stack and chargeTimes[stack[-1]] < chargeTimes[i]:
                    stack.pop()

                stack.append(i)

                while stack and stack[0] <= i - k:
                    stack.popleft()
                
                max_charge = chargeTimes[stack[0]]
                total_cost = max_charge + k * s
            
                if total_cost <= budget: return True
            
            return False
        
        l = 0
        r = n

        while l < r:
            mid = (l + r + 1) // 2
            if isGood(mid):
                l = mid
            else:
                r = mid - 1

        return l
                
# Last updated: 30/9/2025, 7:52:20 pm
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        N = 0
        Y = customers.count('Y')

        min_hour = 0
        min_cost = inf
        for i in range(n):
            cost = Y + N
            if cost < min_cost:
                min_hour = i
                min_cost = cost
            if customers[i] == 'N':
                N += 1
            else:
                Y -= 1
        
        cost = Y + N
        if cost < min_cost:
            min_hour = n
            min_cost = cost
        
        return min_hour
# Last updated: 17/5/2025, 1:30:17 pm
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        n = len(pizzas)
        m = n // 4

        pizzas.sort()
        
        oddDay = ceil(m / 2)
        evenDay = m // 2
        ret = 0

        # print(m, oddDay, evenDay)

        for i in range(oddDay):
            ret += pizzas.pop()

        pizzas.pop()

        for i in range(evenDay):
            ret += pizzas.pop()
            pizzas.pop()
        
        return ret
# Last updated: 17/5/2025, 1:32:45 pm
class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        n = len(pizzas)
        m = n // 4

        pizzas.sort()
        evens = m // 2
        odds = (m + 1) // 2
        ret = 0

        for i in range(odds):
            ret += pizzas.pop()

        pizzas.pop()

        for i in range(evens):
            ret += pizzas.pop()
            pizzas.pop()
        
        return ret

# Last updated: 12/6/2025, 5:34:23 am
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

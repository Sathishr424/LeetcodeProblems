# Last updated: 24/9/2025, 2:52:44 am
class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        n = len(transactions)
        
        max_profit = 0
        loss = []

        for c, cashback in transactions:
            if cashback >= c:
                max_profit = max(max_profit, c)
            else:
                loss.append((c, cashback))

        loss.sort(key=lambda x: (x[1], x[0]))

        cost = 0
        max_cost = inf

        for c, cashback in loss:
            cost -= c
            max_cost = min(cost, max_cost)
            cost += cashback

        cost -= max_profit
        max_cost = min(max_cost, cost)
        
        return -max_cost
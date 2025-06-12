# Last updated: 12/6/2025, 5:40:15 am
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        prev = customers[0][0]
        cnt = 0
        for a, t in customers:
            prev = max(prev, a) + t
            cnt += prev - a
        return cnt / len(customers)
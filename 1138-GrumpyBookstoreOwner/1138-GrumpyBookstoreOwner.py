# Last updated: 12/6/2025, 5:43:54 am
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        ret = 0
        for i in range(n):
            if grumpy[i] == 0:
                ret += customers[i]

        arr = 0
        tmp = 0
        for i in range(minutes):
            arr += customers[i]
            tmp += customers[i] if grumpy[i] == 0 else 0
        ans = max(ret, ret-tmp+arr)

        for i in range(1, n-minutes+1):
            arr -= customers[i-1]
            tmp -= customers[i-1] if grumpy[i-1] == 0 else 0

            val = i+minutes-1
            arr += customers[val]
            tmp += customers[val] if grumpy[val] == 0 else 0
            ans = max(ans, ret-tmp+arr)
  
        return ans